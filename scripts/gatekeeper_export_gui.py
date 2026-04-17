import json
import os
import queue
import shutil
import sys
import threading
import traceback
from datetime import datetime
from pathlib import Path

import tkinter as tk
from tkinter import filedialog, messagebox, ttk


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from jira_gatekeeper_pipeline import (  # noqa: E402
    DEFAULT_JQL,
    GatekeeperDatasetPipeline,
    GatekeeperLlmProcessor,
    JiraApiClient,
    JiraCredentials,
    parse_assignee_aliases,
)


SETTINGS_PATH = ROOT_DIR / "runtime" / "gatekeeper_export_settings.json"
RUNS_DIR = ROOT_DIR / "runtime" / "gatekeeper_export_runs"
DEFAULT_MARKDOWN_DIR = ROOT_DIR / "documentos" / "gatekeeper_markdowns"


def _load_settings() -> dict:
    if not SETTINGS_PATH.exists():
        return {}
    try:
        return json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _save_settings(data: dict) -> None:
    SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    SETTINGS_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _copy_markdowns(source_dir: Path, destination_dir: Path) -> int:
    destination_dir.mkdir(parents=True, exist_ok=True)
    for old_md in destination_dir.glob("*.md"):
        try:
            old_md.unlink()
        except OSError:
            pass

    copied = 0
    for markdown_path in sorted(source_dir.glob("*.md")):
        shutil.copy2(markdown_path, destination_dir / markdown_path.name)
        copied += 1
    return copied


def _sync_markdowns_incremental(source_dir: Path, destination_dir: Path) -> int:
    if not source_dir.exists():
        return 0
    destination_dir.mkdir(parents=True, exist_ok=True)
    copied = 0
    for markdown_path in sorted(source_dir.glob("*.md")):
        destination_path = destination_dir / markdown_path.name
        try:
            if not destination_path.exists() or markdown_path.stat().st_mtime > destination_path.stat().st_mtime:
                shutil.copy2(markdown_path, destination_path)
                copied += 1
        except OSError:
            continue
    return copied


class ExportApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Extrator Gatekeeper")
        self.root.geometry("900x700")
        self.root.minsize(760, 620)

        self._worker_thread: threading.Thread | None = None
        self._messages: queue.Queue[tuple[str, str]] = queue.Queue()
        self._settings = _load_settings()
        self._active_runtime_output_dir: Path | None = None
        self._active_output_markdown_dir: Path | None = None
        self._last_synced_count = 0

        self._build_ui()
        self._load_form()
        self.root.after(150, self._drain_messages)
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _build_ui(self) -> None:
        frame = ttk.Frame(self.root, padding=16)
        frame.pack(fill=tk.BOTH, expand=True)
        frame.columnconfigure(1, weight=1)

        row = 0
        ttk.Label(frame, text="Jira URL").grid(row=row, column=0, sticky="w", pady=(0, 8))
        self.jira_url_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.jira_url_var).grid(row=row, column=1, sticky="ew", pady=(0, 8))

        row += 1
        ttk.Label(frame, text="Cookie da sessao").grid(row=row, column=0, sticky="nw", pady=(0, 8))
        self.cookie_text = tk.Text(frame, height=5, wrap="word")
        self.cookie_text.grid(row=row, column=1, sticky="ew", pady=(0, 8))

        row += 1
        ttk.Label(frame, text="Usuario").grid(row=row, column=0, sticky="w", pady=(0, 8))
        self.username_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.username_var).grid(row=row, column=1, sticky="ew", pady=(0, 8))

        row += 1
        ttk.Label(frame, text="API Token").grid(row=row, column=0, sticky="w", pady=(0, 8))
        self.api_token_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.api_token_var, show="*").grid(row=row, column=1, sticky="ew", pady=(0, 8))

        row += 1
        ttk.Label(frame, text="Senha").grid(row=row, column=0, sticky="w", pady=(0, 8))
        self.password_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.password_var, show="*").grid(row=row, column=1, sticky="ew", pady=(0, 8))

        row += 1
        ttk.Label(frame, text="JQL").grid(row=row, column=0, sticky="w", pady=(0, 8))
        self.jql_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.jql_var).grid(row=row, column=1, sticky="ew", pady=(0, 8))

        row += 1
        ttk.Label(frame, text="Pasta dos markdowns").grid(row=row, column=0, sticky="w", pady=(0, 8))
        output_row = ttk.Frame(frame)
        output_row.grid(row=row, column=1, sticky="ew", pady=(0, 8))
        output_row.columnconfigure(0, weight=1)
        self.output_dir_var = tk.StringVar()
        ttk.Entry(output_row, textvariable=self.output_dir_var).grid(row=0, column=0, sticky="ew")
        ttk.Button(output_row, text="Escolher", command=self._pick_output_dir).grid(row=0, column=1, padx=(8, 0))

        row += 1
        small_row = ttk.Frame(frame)
        small_row.grid(row=row, column=1, sticky="w", pady=(0, 8))
        ttk.Label(frame, text="Limite").grid(row=row, column=0, sticky="w", pady=(0, 8))
        self.limit_var = tk.StringVar()
        ttk.Entry(small_row, textvariable=self.limit_var, width=12).grid(row=0, column=0, sticky="w")

        row += 1
        ttk.Label(frame, text="Aliases do assignee").grid(row=row, column=0, sticky="w", pady=(0, 8))
        self.aliases_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.aliases_var).grid(row=row, column=1, sticky="ew", pady=(0, 8))

        row += 1
        self.no_llm_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(frame, text="Extrair sem LLM (mais rapido)", variable=self.no_llm_var).grid(
            row=row, column=1, sticky="w", pady=(0, 8)
        )

        row += 1
        button_row = ttk.Frame(frame)
        button_row.grid(row=row, column=1, sticky="w", pady=(4, 12))
        self.extract_button = ttk.Button(button_row, text="Extrair tickets", command=self._start_export)
        self.extract_button.grid(row=0, column=0)
        ttk.Button(button_row, text="Abrir pasta", command=self._open_output_dir).grid(row=0, column=1, padx=(8, 0))

        row += 1
        ttk.Label(
            frame,
            text="Uso simples: cole o header Cookie inteiro da sessao do Jira e clique em Extrair tickets.",
        ).grid(row=row, column=1, sticky="w", pady=(0, 8))

        row += 1
        self.status_var = tk.StringVar(value="Pronto.")
        ttk.Label(frame, textvariable=self.status_var).grid(row=row, column=1, sticky="w", pady=(0, 8))

        row += 1
        ttk.Label(frame, text="Log").grid(row=row, column=0, sticky="nw")
        self.log_text = tk.Text(frame, height=16, wrap="word", state=tk.DISABLED)
        self.log_text.grid(row=row, column=1, sticky="nsew")
        frame.rowconfigure(row, weight=1)

    def _load_form(self) -> None:
        self.jira_url_var.set(self._settings.get("jira_url", "https://suporte.maximatech.com.br"))
        self.cookie_text.insert("1.0", self._settings.get("session_cookie", ""))
        self.username_var.set(self._settings.get("username", ""))
        self.api_token_var.set(self._settings.get("api_token", ""))
        self.password_var.set(self._settings.get("password", ""))
        self.jql_var.set(self._settings.get("jql", DEFAULT_JQL))
        self.output_dir_var.set(self._settings.get("output_dir", str(DEFAULT_MARKDOWN_DIR)))
        self.limit_var.set(self._settings.get("limit", ""))
        self.aliases_var.set(
            self._settings.get("assignee_aliases", "Filipe do Amaral Padilha|Felipe do Amaral Padilha")
        )
        self.no_llm_var.set(bool(self._settings.get("no_llm", True)))

    def _collect_settings(self) -> dict:
        return {
            "jira_url": self.jira_url_var.get().strip(),
            "session_cookie": self.cookie_text.get("1.0", tk.END).strip(),
            "username": self.username_var.get().strip(),
            "api_token": self.api_token_var.get().strip(),
            "password": self.password_var.get().strip(),
            "jql": self.jql_var.get().strip() or DEFAULT_JQL,
            "output_dir": self.output_dir_var.get().strip() or str(DEFAULT_MARKDOWN_DIR),
            "limit": self.limit_var.get().strip(),
            "assignee_aliases": self.aliases_var.get().strip(),
            "no_llm": bool(self.no_llm_var.get()),
        }

    def _pick_output_dir(self) -> None:
        selected = filedialog.askdirectory(initialdir=self.output_dir_var.get() or str(DEFAULT_MARKDOWN_DIR))
        if selected:
            self.output_dir_var.set(selected)

    def _open_output_dir(self) -> None:
        output_dir = Path(self.output_dir_var.get().strip() or str(DEFAULT_MARKDOWN_DIR))
        output_dir.mkdir(parents=True, exist_ok=True)
        os.startfile(str(output_dir))

    def _append_log(self, text: str) -> None:
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.insert(tk.END, text.rstrip() + "\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state=tk.DISABLED)

    def _set_busy(self, busy: bool) -> None:
        if busy:
            self.extract_button.configure(state=tk.DISABLED)
        else:
            self.extract_button.configure(state=tk.NORMAL)

    def _sync_live_markdowns(self) -> None:
        if not self._active_runtime_output_dir or not self._active_output_markdown_dir:
            return
        source_dir = self._active_runtime_output_dir / "review" / "markdown"
        copied_now = _sync_markdowns_incremental(source_dir, self._active_output_markdown_dir)
        current_count = len(list(source_dir.glob("*.md"))) if source_dir.exists() else 0
        if copied_now or current_count != self._last_synced_count:
            self._last_synced_count = current_count
            suffix = f"{current_count} markdown(s) ja disponiveis em {self._active_output_markdown_dir}"
            if self._worker_thread and self._worker_thread.is_alive():
                self.status_var.set(f"Extraindo tickets... {suffix}")
            else:
                self.status_var.set(suffix)

    def _drain_messages(self) -> None:
        self._sync_live_markdowns()
        while True:
            try:
                kind, payload = self._messages.get_nowait()
            except queue.Empty:
                break
            if kind == "log":
                self._append_log(payload)
            elif kind == "status":
                self.status_var.set(payload)
            elif kind == "done":
                self._sync_live_markdowns()
                self._set_busy(False)
                self.status_var.set(payload)
                messagebox.showinfo("Extrator Gatekeeper", payload)
            elif kind == "error":
                self._sync_live_markdowns()
                self._set_busy(False)
                self.status_var.set("Falha na extracao.")
                self._append_log(payload)
                messagebox.showerror("Extrator Gatekeeper", payload)
        self.root.after(150, self._drain_messages)

    def _validate_form(self, settings: dict) -> str | None:
        if not settings["jira_url"]:
            return "Preencha o Jira URL."
        if not settings["session_cookie"] and not (
            settings["username"] and (settings["api_token"] or settings["password"])
        ):
            return "Preencha o Cookie da sessao ou Usuario + API Token/Senha."
        if settings["limit"]:
            try:
                int(settings["limit"])
            except ValueError:
                return "O limite precisa ser um numero inteiro."
        return None

    def _start_export(self) -> None:
        if self._worker_thread and self._worker_thread.is_alive():
            return

        settings = self._collect_settings()
        error = self._validate_form(settings)
        if error:
            messagebox.showerror("Extrator Gatekeeper", error)
            return

        _save_settings(settings)
        self._set_busy(True)
        self.status_var.set("Extraindo tickets...")
        self._append_log("Iniciando extracao.")
        self._last_synced_count = 0

        self._worker_thread = threading.Thread(target=self._run_export, args=(settings,), daemon=True)
        self._worker_thread.start()

    def _run_export(self, settings: dict) -> None:
        run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        runtime_output_dir = RUNS_DIR / run_id
        output_markdown_dir = Path(settings["output_dir"]).expanduser()
        self._active_runtime_output_dir = runtime_output_dir
        self._active_output_markdown_dir = output_markdown_dir

        credentials = JiraCredentials(
            base_url=settings["jira_url"],
            username=settings["username"] or None,
            password=settings["password"] or None,
            api_token=settings["api_token"] or None,
            session_cookie=settings["session_cookie"] or None,
        )

        self._messages.put(("log", f"Saida de trabalho: {runtime_output_dir}"))
        self._messages.put(("log", f"Markdowns finais: {output_markdown_dir}"))

        client = JiraApiClient(credentials)
        try:
            llm_processor = None if settings["no_llm"] else GatekeeperLlmProcessor()
            runner = GatekeeperDatasetPipeline(
                jira_client=client,
                output_dir=runtime_output_dir,
                review_threshold=0.75,
                llm_processor=llm_processor,
                no_llm=bool(settings["no_llm"]),
                assignee_aliases=parse_assignee_aliases(settings["assignee_aliases"]),
            )
            manifest = runner.run(
                jql=settings["jql"],
                full_refresh=False,
                since_updated=None,
                limit=int(settings["limit"]) if settings["limit"] else None,
            )

            markdown_source_dir = runtime_output_dir / "review" / "markdown"
            copied = _copy_markdowns(markdown_source_dir, output_markdown_dir)
            self._messages.put(("log", json.dumps(manifest, ensure_ascii=False, indent=2)))
            self._messages.put(
                (
                    "done",
                    f"Extracao concluida. {copied} markdown(s) foram gravados em:\n{output_markdown_dir}",
                )
            )
        except Exception:
            self._messages.put(("error", traceback.format_exc()))
        finally:
            client.close()

    def _on_close(self) -> None:
        _save_settings(self._collect_settings())
        self.root.destroy()


def main() -> int:
    root = tk.Tk()
    style = ttk.Style()
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass
    ExportApp(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
