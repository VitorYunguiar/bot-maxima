/*
  Script para colar no console do navegador dentro do JIRA.

  Objetivo:
  - Usar o filtro base informado:
      project = "maxPedido Dev" AND Natureza = "Dúvida" AND type = Dúvida ORDER BY created DESC
  - Ler a descrição do chamado como a dúvida do analista
  - Ler os comentários como a resposta/explicação do dev
  - Baixar um .zip com um .md por issue, além de index.csv e manifest.json

  Como usar:
  1. Abra o JIRA já autenticado
  2. Pressione F12
  3. Vá em Console
  4. Cole este script inteiro
  5. Aguarde o download
*/

(async () => {
  const CONFIG = {
    apiBase: "/rest/api/2",
    jql: 'project = "maxPedido Dev" AND Natureza = "Dúvida" AND type = Dúvida ORDER BY created DESC',
    maxIssuesToScan: 500,
    pageSize: 100,
    requestDelayMs: 60,
    zipNamePrefix: "maxpedido_dev_duvidas",
    explanationTerms: [
      /porque/i,
      /por causa/i,
      /devido/i,
      /motivo/i,
      /ocorre/i,
      /acontece/i,
      /comportamento esperado/i,
      /esperado/i,
      /regra/i,
      /fluxo/i,
      /tribut/i,
      /parametr/i,
      /configur/i,
      /taxa/i
    ],
    answerFieldNames: [
      "Detalhes",
      "O que foi feito N3"
    ]
  };

  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

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

  function normalizeText(value) {
    return String(value || "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/\s+/g, " ")
      .trim()
      .toLowerCase();
  }

  function extractText(node) {
    if (!node) return "";
    if (typeof node === "string") return node;
    if (Array.isArray(node)) return node.map(extractText).join("");

    const type = node.type || "";
    const content = safeArray(node.content);

    if (type === "text") return node.text || "";
    if (type === "hardBreak") return "\n";

    const text = content.map(extractText).join("");

    if (["paragraph", "heading", "blockquote", "listItem"].includes(type)) {
      return `${text}\n`;
    }

    if (["bulletList", "orderedList", "doc"].includes(type)) {
      return text;
    }

    return text;
  }

  function plainText(value) {
    if (!value) return "";
    if (typeof value === "string") return value.trim();

    return extractText(value)
      .replace(/\n{3,}/g, "\n\n")
      .replace(/[ \t]+\n/g, "\n")
      .trim();
  }

  function cleanQuestionText(text) {
    if (!text) return "";

    const lines = String(text)
      .replace(/\r/g, "")
      .split("\n")
      .map((line) => line.trimEnd());

    const cleaned = [];
    let skippingCriticaBlock = false;

    for (const rawLine of lines) {
      const line = rawLine.trim();
      const normalized = normalizeText(line);

      if (!line) {
        if (!skippingCriticaBlock && cleaned.length && cleaned[cleaned.length - 1] !== "") {
          cleaned.push("");
        }
        continue;
      }

      if (/^critica$/i.test(line)) {
        skippingCriticaBlock = true;
        continue;
      }

      if (skippingCriticaBlock) {
        if (/^(login|senha|analista|cliente)\b/i.test(line)) {
          skippingCriticaBlock = false;
        } else {
          continue;
        }
      }

      if (/^(login|senha)\b/i.test(line)) {
        continue;
      }

      if (/^analista\b/i.test(line) && line.split(/\s+/).length <= 4) {
        continue;
      }

      if (/^cliente\b/i.test(line) && line.length < 120) {
        continue;
      }

      if (/^!.*!$/.test(line)) {
        continue;
      }

      if (normalized === "bom dia" || normalized === "boa tarde" || normalized === "boa noite") {
        continue;
      }

      cleaned.push(rawLine.trim());
    }

    return cleaned
      .join("\n")
      .replace(/\n{3,}/g, "\n\n")
      .trim();
  }

  function csvEscape(value) {
    return `"${String(value || "").replace(/"/g, '""')}"`;
  }

  function matchesExplanation(text) {
    return CONFIG.explanationTerms.some((regex) => regex.test(String(text || "")));
  }

  function looksLikePlaceholder(text) {
    const normalized = normalizeText(text);
    return !normalized
      || normalized === "vazio"
      || normalized === "falha: defeito: solucao:"
      || normalized === "falha:defeito:solucao:";
  }

  function toCommentRecord(comment) {
    const body = plainText(comment.body);
    return {
      id: comment.id || "",
      author: comment.author?.displayName || "Sem autor",
      created: comment.created || "",
      updated: comment.updated || "",
      body,
      looksLikeExplanation: matchesExplanation(body)
    };
  }

  async function ensureJsZip() {
    if (window.JSZip) return window.JSZip;

    await new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = "https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js";
      script.onload = resolve;
      script.onerror = () => reject(new Error("Nao foi possivel carregar o JSZip."));
      document.head.appendChild(script);
    });

    return window.JSZip;
  }

  async function jiraFetch(path, options = {}) {
    const response = await fetch(path, {
      method: options.method || "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        ...(options.headers || {})
      },
      credentials: "same-origin",
      body: options.body ? JSON.stringify(options.body) : undefined
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Falha HTTP ${response.status} em ${path}: ${errorText.slice(0, 500)}`);
    }

    return response.json();
  }

  async function searchIssues() {
    const issues = [];
    let startAt = 0;
    let total = Infinity;

    while (startAt < total && issues.length < CONFIG.maxIssuesToScan) {
      const payload = {
        jql: CONFIG.jql,
        startAt,
        maxResults: Math.min(CONFIG.pageSize, CONFIG.maxIssuesToScan - issues.length),
        fields: ["summary"]
      };

      const data = await jiraFetch(`${CONFIG.apiBase}/search`, {
        method: "POST",
        body: payload
      });

      total = data.total || 0;
      const pageIssues = safeArray(data.issues);
      if (!pageIssues.length) break;

      issues.push(...pageIssues);
      startAt += pageIssues.length;

      console.log(`Busca: ${issues.length}/${Math.min(total, CONFIG.maxIssuesToScan)} issues listadas.`);
    }

    return issues;
  }

  async function fetchIssue(issueKey) {
    const fields = [
      "summary",
      "description",
      "comment",
      "status",
      "resolution",
      "issuetype",
      "labels",
      "components",
      "created",
      "updated",
      "assignee",
      "reporter"
    ];

    const query = new URLSearchParams({
      fields: fields.join(","),
      expand: "changelog"
    });

    return jiraFetch(`${CONFIG.apiBase}/issue/${encodeURIComponent(issueKey)}?${query.toString()}`);
  }

  function extractAnswerFromHistory(issue) {
    const acceptedFieldNames = CONFIG.answerFieldNames.map(normalizeText);
    const candidates = [];

    safeArray(issue.changelog?.histories).forEach((history) => {
      safeArray(history.items).forEach((item) => {
        const normalizedField = normalizeText(item.field || "");
        const answerText = plainText(item.toString || "");

        if (!acceptedFieldNames.includes(normalizedField)) return;
        if (looksLikePlaceholder(answerText)) return;

        candidates.push({
          source: item.field || "",
          author: history.author?.displayName || "Sem autor",
          created: history.created || "",
          text: answerText
        });
      });
    });

    return candidates
      .sort((a, b) => new Date(a.created) - new Date(b.created))
      .pop() || null;
  }

  function extractAnswerFromComments(issue, assigneeName) {
    const comments = safeArray(issue.fields?.comment?.comments)
      .map(toCommentRecord)
      .filter((comment) => comment.body && !/^!.*!$/m.test(comment.body));

    const preferred = comments.filter((comment) => {
      const isAssignee = assigneeName && comment.author === assigneeName;
      return isAssignee || comment.looksLikeExplanation;
    });

    return (preferred.length ? preferred : comments).slice().pop() || null;
  }

  function extractBestAnswer(issue) {
    const assigneeName = issue.fields?.assignee?.displayName || "";
    return extractAnswerFromHistory(issue) || extractAnswerFromComments(issue, assigneeName);
  }

  function buildIssueRecord(issue) {
    const fields = issue.fields || {};
    const description = cleanQuestionText(plainText(fields.description));
    const answer = extractBestAnswer(issue);

    return {
      key: issue.key,
      summary: fields.summary || "",
      analystQuestion: description,
      answer: answer?.text || "",
      answerSource: answer?.source || "",
      answerAuthor: answer?.author || "",
      answerCreated: answer?.created || ""
    };
  }

  function renderIssueMarkdown(record) {
    const lines = [
      `# ${record.key} - ${record.summary}`,
      "",
      "## Dúvida do Analista",
      "",
      record.analystQuestion || "Sem descrição."
    ];

    lines.push("", "## Resposta", "", record.answer || "Sem resposta identificada.");

    return `${lines.join("\n").trim()}\n`;
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

  async function main() {
    console.clear();
    console.log("Executando busca de dúvidas técnicas...");
    console.log("JQL:", CONFIG.jql);

    const baseIssues = await searchIssues();
    console.log(`Total listado: ${baseIssues.length}`);

    const records = [];
    const failures = [];

    for (let i = 0; i < baseIssues.length; i += 1) {
      const issueKey = baseIssues[i].key;
      console.log(`Lendo ${i + 1}/${baseIssues.length}: ${issueKey}`);

      try {
        const issue = await fetchIssue(issueKey);
        records.push(buildIssueRecord(issue));
      } catch (error) {
        failures.push({ key: issueKey, error: error.message });
        console.error(`Falha em ${issueKey}:`, error);
      }

      if (CONFIG.requestDelayMs > 0) {
        await sleep(CONFIG.requestDelayMs);
      }
    }

    console.table(records.map((record) => ({
      key: record.key,
      summary: record.summary,
      temPergunta: Boolean(record.analystQuestion),
      temResposta: Boolean(record.answer),
      origemResposta: record.answerSource
    })));

    const JSZip = await ensureJsZip();
    const zip = new JSZip();

    const manifest = {
      generatedAt: new Date().toISOString(),
      jql: CONFIG.jql,
      scanned: baseIssues.length,
      exported: records.length,
      failures
    };

    const csvRows = [[
      "key",
      "summary",
      "tem_pergunta",
      "tem_resposta",
      "origem_resposta",
      "autor_resposta",
      "data_resposta"
    ].map(csvEscape).join(",")];

    records.forEach((record) => {
      const fileName = `${record.key} - ${sanitizeFileName(record.summary)}.md`;
      zip.file(fileName, renderIssueMarkdown(record));

      csvRows.push([
        record.key,
        record.summary,
        record.analystQuestion ? "sim" : "nao",
        record.answer ? "sim" : "nao",
        record.answerSource,
        record.answerAuthor,
        record.answerCreated
      ].map(csvEscape).join(","));
    });

    zip.file("index.csv", `${csvRows.join("\n")}\n`);
    zip.file("manifest.json", JSON.stringify(manifest, null, 2));

    const stamp = new Date().toISOString().slice(0, 19).replace(/[:T]/g, "-");
    const blob = await zip.generateAsync({ type: "blob" });
    downloadBlob(blob, `${CONFIG.zipNamePrefix}_${stamp}.zip`);

    console.log("Download iniciado.");
  }

  try {
    await main();
  } catch (error) {
    console.error("Execucao interrompida:", error);
  }
})();
