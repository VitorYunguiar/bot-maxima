/*
  Uso:
  1. Abra o JIRA no mesmo domínio em que você já está autenticado.
  2. Pressione F12 e cole este script no console.
  3. Ajuste o bloco CONFIG se os nomes dos campos/status no seu JIRA forem diferentes.

  Saída:
  - Um arquivo .zip com:
    - 1 .md por issue encontrada
    - 1 index.csv resumido
    - 1 manifest.json com os metadados da execução

  Observação:
  - O filtro é feito pelo histórico do issue (changelog), não só pelos campos atuais.
  - Como o JIRA pode usar nomes diferentes para o fluxo, os termos de N3/Erro/Dúvida
    ficam configuráveis no bloco CONFIG.
*/

(async () => {
  const CONFIG = {
    projectKey: "MXPEDDV",
    baseJql: 'project = MXPEDDV ORDER BY updated DESC',
    maxIssuesToScan: 400,
    searchPageSize: 100,
    issueRequestDelayMs: 80,
    zipNamePrefix: "mxpeddv_n3_erro_voltou_duvida",
    apiBase: "/rest/api/2",
    includeComments: false,
    n3Terms: [
      /(^|[^a-z])n3([^a-z]|$)/i,
      /encaminh[a-z]*.*n3/i,
      /desenvolvimento.*n3/i
    ],
    erroTerms: [
      /^erro$/i,
      /bug/i,
      /falha/i
    ],
    duvidaTerms: [
      /^d[uú]vida$/i,
      /questionamento/i
    ]
  };

  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  function normalizeText(value) {
    return String(value || "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/\s+/g, " ")
      .trim()
      .toLowerCase();
  }

  function regexListMatches(value, regexList) {
    const raw = String(value || "");
    const normalized = normalizeText(value);
    return regexList.some((regex) => regex.test(raw) || regex.test(normalized));
  }

  function safeArray(value) {
    return Array.isArray(value) ? value : [];
  }

  function sanitizeFileName(value) {
    return String(value || "sem-titulo")
      .replace(/[<>:"/\\|?*\x00-\x1F]/g, " ")
      .replace(/\s+/g, " ")
      .trim()
      .slice(0, 120);
  }

  function plainTextFromDescription(description) {
    if (!description) return "";
    if (typeof description === "string") return description.trim();

    const chunks = [];

    function walk(node) {
      if (!node) return;
      if (typeof node === "string") {
        chunks.push(node);
        return;
      }

      if (node.type === "text" && node.text) {
        chunks.push(node.text);
      }

      safeArray(node.content).forEach(walk);

      if (["paragraph", "heading", "listItem"].includes(node.type)) {
        chunks.push("\n");
      }
    }

    walk(description);

    return chunks
      .join("")
      .replace(/\n{3,}/g, "\n\n")
      .trim();
  }

  function summarizeComments(issue) {
    const comments = safeArray(issue.fields?.comment?.comments);
    if (!comments.length) return [];

    return comments.map((comment) => ({
      author: comment.author?.displayName || "Sem autor",
      created: comment.created || "",
      body: plainTextFromDescription(comment.body)
    }));
  }

  function itemSnapshot(item) {
    return {
      field: item.field || "",
      from: item.fromString || "",
      to: item.toString || ""
    };
  }

  function historyMatches(history, regexList) {
    return safeArray(history.items).some((item) => {
      return regexListMatches(item.field, regexList)
        || regexListMatches(item.fromString, regexList)
        || regexListMatches(item.toString, regexList);
    });
  }

  function currentIssueMatches(issue, regexList) {
    const fields = issue.fields || {};
    const candidates = [
      fields.summary,
      fields.description,
      fields.status?.name,
      fields.issuetype?.name,
      fields.resolution?.name,
      ...(fields.labels || []),
      ...(fields.components || []).map((item) => item.name),
      ...(fields.fixVersions || []).map((item) => item.name)
    ];

    return candidates.some((candidate) => regexListMatches(candidate, regexList));
  }

  function buildTransitionReport(issue) {
    const histories = safeArray(issue.changelog?.histories)
      .slice()
      .sort((a, b) => new Date(a.created) - new Date(b.created));

    const checkpoints = histories.map((history) => ({
      created: history.created,
      author: history.author?.displayName || "Sem autor",
      changedToN3: historyMatches(history, CONFIG.n3Terms),
      changedToErro: historyMatches(history, CONFIG.erroTerms),
      changedToDuvida: historyMatches(history, CONFIG.duvidaTerms),
      items: safeArray(history.items).map(itemSnapshot)
    }));

    const firstN3Index = checkpoints.findIndex((entry) => entry.changedToN3);
    if (firstN3Index === -1) {
      return {
        matched: false,
        reason: "Nao passou por N3 no historico analisado.",
        checkpoints
      };
    }

    const hadErroBeforeOrAtN3 =
      currentIssueMatches(issue, CONFIG.erroTerms)
      || checkpoints.slice(0, firstN3Index + 1).some((entry) => entry.changedToErro);

    if (!hadErroBeforeOrAtN3) {
      return {
        matched: false,
        reason: "Passou por N3, mas nao encontrei indicio de erro antes ou no momento dessa mudanca.",
        checkpoints
      };
    }

    const duvidaIndex = checkpoints.findIndex(
      (entry, index) => index > firstN3Index && entry.changedToDuvida
    );

    if (duvidaIndex === -1 && !currentIssueMatches(issue, CONFIG.duvidaTerms)) {
      return {
        matched: false,
        reason: "Passou por N3 como erro, mas nao voltou como duvida no historico analisado.",
        checkpoints
      };
    }

    return {
      matched: true,
      reason: "Passou por N3 com indicio de erro e voltou com indicio de duvida.",
      firstN3At: checkpoints[firstN3Index]?.created || "",
      firstN3Index,
      duvidaAt: duvidaIndex >= 0 ? checkpoints[duvidaIndex]?.created || "" : "",
      duvidaIndex,
      checkpoints
    };
  }

  function downloadBlob(blob, fileName) {
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    setTimeout(() => {
      URL.revokeObjectURL(url);
      link.remove();
    }, 1000);
  }

  async function ensureJsZip() {
    if (window.JSZip) return window.JSZip;

    await new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = "https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js";
      script.onload = resolve;
      script.onerror = () => reject(new Error("Nao foi possivel carregar o JSZip do CDN."));
      document.head.appendChild(script);
    });

    return window.JSZip;
  }

  async function jiraFetch(path, options = {}) {
    const response = await fetch(path, {
      method: options.method || "GET",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
        ...(options.headers || {})
      },
      credentials: "same-origin",
      body: options.body ? JSON.stringify(options.body) : undefined
    });

    if (!response.ok) {
      const text = await response.text();
      throw new Error(`Falha HTTP ${response.status} em ${path}: ${text.slice(0, 500)}`);
    }

    return response.json();
  }

  async function searchIssueKeys() {
    const keys = [];
    let startAt = 0;
    let total = Infinity;

    while (startAt < total && keys.length < CONFIG.maxIssuesToScan) {
      const payload = {
        jql: CONFIG.baseJql,
        startAt,
        maxResults: Math.min(CONFIG.searchPageSize, CONFIG.maxIssuesToScan - keys.length),
        fields: ["summary"]
      };

      const data = await jiraFetch(`${CONFIG.apiBase}/search`, {
        method: "POST",
        body: payload
      });

      total = data.total || 0;
      const pageIssues = safeArray(data.issues);
      if (!pageIssues.length) break;

      pageIssues.forEach((issue) => keys.push(issue.key));
      startAt += pageIssues.length;
      console.log(`Busca paginada: ${keys.length}/${Math.min(total, CONFIG.maxIssuesToScan)} issues listadas.`);
    }

    return keys;
  }

  async function fetchIssueDetail(issueKey) {
    const fields = [
      "summary",
      "description",
      "status",
      "issuetype",
      "labels",
      "components",
      "fixVersions",
      "resolution",
      "reporter",
      "assignee",
      "created",
      "updated"
    ];

    if (CONFIG.includeComments) {
      fields.push("comment");
    }

    const query = new URLSearchParams({
      expand: "changelog",
      fields: fields.join(",")
    });

    return jiraFetch(`${CONFIG.apiBase}/issue/${encodeURIComponent(issueKey)}?${query.toString()}`);
  }

  function markdownForIssue(issue, report) {
    const fields = issue.fields || {};
    const description = plainTextFromDescription(fields.description);
    const comments = summarizeComments(issue);

    const lines = [
      `# ${issue.key} - ${fields.summary || "Sem titulo"}`,
      "",
      `- Projeto: ${CONFIG.projectKey}`,
      `- Tipo atual: ${fields.issuetype?.name || "N/A"}`,
      `- Status atual: ${fields.status?.name || "N/A"}`,
      `- Resolucao: ${fields.resolution?.name || "N/A"}`,
      `- Criado em: ${fields.created || "N/A"}`,
      `- Atualizado em: ${fields.updated || "N/A"}`,
      `- Responsavel: ${fields.assignee?.displayName || "N/A"}`,
      `- Solicitante: ${fields.reporter?.displayName || "N/A"}`,
      `- Labels: ${(fields.labels || []).join(", ") || "N/A"}`,
      `- Componentes: ${(fields.components || []).map((item) => item.name).join(", ") || "N/A"}`,
      "",
      "## Motivo da selecao",
      "",
      report.reason
    ];

    if (report.firstN3At) {
      lines.push(`- Primeiro indicio de N3: ${report.firstN3At}`);
    }

    if (report.duvidaAt) {
      lines.push(`- Primeiro indicio de volta para duvida: ${report.duvidaAt}`);
    }

    lines.push("", "## Descricao", "", description || "Sem descricao.");

    lines.push("", "## Historico relevante", "");
    report.checkpoints.forEach((checkpoint, index) => {
      if (!checkpoint.changedToN3 && !checkpoint.changedToErro && !checkpoint.changedToDuvida) {
        return;
      }

      const flags = [
        checkpoint.changedToN3 ? "N3" : "",
        checkpoint.changedToErro ? "Erro" : "",
        checkpoint.changedToDuvida ? "Duvida" : ""
      ].filter(Boolean).join(", ");

      lines.push(`### ${index + 1}. ${checkpoint.created} | ${checkpoint.author} | ${flags}`);
      lines.push("");
      checkpoint.items.forEach((item) => {
        lines.push(`- Campo: ${item.field || "N/A"} | De: ${item.from || "vazio"} | Para: ${item.to || "vazio"}`);
      });
      lines.push("");
    });

    if (comments.length) {
      lines.push("## Comentarios", "");
      comments.forEach((comment, index) => {
        lines.push(`### ${index + 1}. ${comment.created} | ${comment.author}`);
        lines.push("");
        lines.push(comment.body || "Sem texto.");
        lines.push("");
      });
    }

    return lines.join("\n").trim() + "\n";
  }

  function csvEscape(value) {
    return `"${String(value || "").replace(/"/g, '""')}"`;
  }

  async function main() {
    console.clear();
    console.log("Iniciando busca no JIRA...");
    console.log("JQL base:", CONFIG.baseJql);

    const issueKeys = await searchIssueKeys();
    console.log(`Total de issues listadas para varredura: ${issueKeys.length}`);

    const matched = [];
    const rejected = [];

    for (let index = 0; index < issueKeys.length; index += 1) {
      const issueKey = issueKeys[index];
      console.log(`Analisando ${index + 1}/${issueKeys.length}: ${issueKey}`);

      try {
        const issue = await fetchIssueDetail(issueKey);
        const report = buildTransitionReport(issue);

        if (report.matched) {
          matched.push({ issue, report });
          console.log(`Selecionado: ${issueKey}`);
        } else {
          rejected.push({ key: issueKey, reason: report.reason });
        }
      } catch (error) {
        rejected.push({ key: issueKey, reason: error.message });
        console.error(`Falha ao analisar ${issueKey}:`, error);
      }

      if (CONFIG.issueRequestDelayMs > 0) {
        await sleep(CONFIG.issueRequestDelayMs);
      }
    }

    console.log(`Finalizado. ${matched.length} issues encontradas.`);
    console.table(
      matched.map(({ issue, report }) => ({
        key: issue.key,
        summary: issue.fields?.summary || "",
        status: issue.fields?.status?.name || "",
        tipo: issue.fields?.issuetype?.name || "",
        primeiroN3: report.firstN3At || "",
        voltouDuvida: report.duvidaAt || ""
      }))
    );

    const JSZip = await ensureJsZip();
    const zip = new JSZip();

    const manifest = {
      generatedAt: new Date().toISOString(),
      projectKey: CONFIG.projectKey,
      baseJql: CONFIG.baseJql,
      scannedIssues: issueKeys.length,
      matchedIssues: matched.length,
      rejectedIssues: rejected
    };

    const csvHeader = [
      "key",
      "summary",
      "tipo_atual",
      "status_atual",
      "primeiro_n3",
      "voltou_duvida",
      "updated"
    ];

    const csvRows = [csvHeader.map(csvEscape).join(",")];

    matched.forEach(({ issue, report }) => {
      const fileName = `${issue.key} - ${sanitizeFileName(issue.fields?.summary)}.md`;
      zip.file(fileName, markdownForIssue(issue, report));

      csvRows.push([
        issue.key,
        issue.fields?.summary || "",
        issue.fields?.issuetype?.name || "",
        issue.fields?.status?.name || "",
        report.firstN3At || "",
        report.duvidaAt || "",
        issue.fields?.updated || ""
      ].map(csvEscape).join(","));
    });

    zip.file("index.csv", csvRows.join("\n") + "\n");
    zip.file("manifest.json", JSON.stringify(manifest, null, 2));

    const stamp = new Date().toISOString().slice(0, 19).replace(/[:T]/g, "-");
    const blob = await zip.generateAsync({ type: "blob" });
    downloadBlob(blob, `${CONFIG.zipNamePrefix}_${stamp}.zip`);

    console.log("Download iniciado.");
    return { matched, rejected, manifest };
  }

  try {
    await main();
  } catch (error) {
    console.error("Execucao interrompida:", error);
  }
})();
