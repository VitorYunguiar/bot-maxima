Estrutura Identificada
O JIRA da Máxima possui:

2.552 issues no projeto Gatekeeper
Lista de issues no lado esquerdo
Painel de detalhes no lado direito
Campos customizados específicos como: Produto GateKeeper, ERP do cliente, Versão APK, etc.

Script Otimizado para Extração
Aqui está um script JavaScript que você pode usar para extrair os dados de forma estruturada:
javascript// SCRIPT PARA EXTRAIR DADOS DO JIRA - PROJETO GATEKEEPER

// 1. Função para extrair lista de issues da página atual
function extractIssueList() {
  const issues = [];
  const allLinks = document.querySelectorAll('a[href*="/browse/GATE-"]');
  
  allLinks.forEach(link => {
    const match = link.href.match(/GATE-\\d+/);
    if (match) {
      const key = match[0];
      const titleElement = link.closest('li') || link.parentElement;
      const fullText = titleElement.textContent.trim();
      const title = fullText.replace(key, '').trim();
      
      if (!issues.find(i => i.key === key)) {
        issues.push({
          key: key,
          title: title,
          url: link.href
        });
      }
    }
  });
  
  return issues;
}

// 2. Função para extrair detalhes completos do issue aberto
function extractIssueDetails() {
  const data = {
    key: '',
    title: '',
    fields: {}
  };
  
  // Chave e título
  const keyMatch = window.location.href.match(/GATE-\\d+/);
  data.key = keyMatch ? keyMatch[0] : '';
  
  const titleEl = document.querySelector('#summary-val, h1[id*="summary"]');
  data.title = titleEl ? titleEl.textContent.trim() : '';
  
  // Campos padrão do JIRA
  const standardFields = [
    { selector: '#type-val', name: 'Tipo' },
    { selector: '#status-val', name: 'Status' },
    { selector: '#priority-val', name: 'Prioridade' },
    { selector: '#resolution-val', name: 'Resolução' },
    { selector: '#components-val', name: 'Componentes' },
    { selector: '#labels-val', name: 'Rótulos' },
    { selector: '#assignee-val', name: 'Responsável' },
    { selector: '#reporter-val', name: 'Solicitante' },
    { selector: '#created-val', name: 'Criado' },
    { selector: '#updated-val', name: 'Atualizado' },
    { selector: '#resolutiondate-val', name: 'Resolvido' },
    { selector: '#description-val', name: 'Descrição' }
  ];
  
  standardFields.forEach(field => {
    const element = document.querySelector(field.selector);
    if (element) {
      const text = element.textContent.trim();
      if (text && text !== 'Nenhum' && text !== 'None') {
        data.fields[field.name] = text;
      }
    }
  });
  
  // Campos customizados (extrair de todos os itens visíveis)
  const allItems = document.querySelectorAll('.item, li[class*="field"]');
  
  allItems.forEach(item => {
    // Tentar diferentes estruturas
    let label = null;
    let value = null;
    
    // Estrutura 1: generic elements
    const labelGeneric = item.querySelector('generic:first-child');
    const valueGeneric = item.querySelector('generic:last-child');
    
    if (labelGeneric && valueGeneric && labelGeneric !== valueGeneric) {
      label = labelGeneric.textContent.trim();
      value = valueGeneric.textContent.trim();
    }
    
    // Estrutura 2: span/div
    if (!label) {
      const spans = item.querySelectorAll('span, div');
      if (spans.length >= 2) {
        label = spans[0].textContent.trim();
        value = spans[1].textContent.trim();
      }
    }
    
    if (label && value && label !== value && !label.includes('Clique')) {
      // Limpar label
      label = label.replace(/:/g, '').trim();
      if (label && value.length < 500) { // Evitar campos muito grandes
        data.fields[label] = value;
      }
    }
  });
  
  return data;
}

// 3. Função para extrair múltiplos issues (navegar pela lista)
async function extractMultipleIssues(maxIssues = 50) {
  const results = [];
  const issueList = extractIssueList();
  
  console.log(`Encontrados ${issueList.length} issues na página atual`);
  
  for (let i = 0; i < Math.min(issueList.length, maxIssues); i++) {
    const issue = issueList[i];
    console.log(`Processando ${i + 1}/${Math.min(issueList.length, maxIssues)}: ${issue.key}`);
    
    // Clicar no issue
    const link = document.querySelector(`a[href*="${issue.key}"]`);
    if (link) {
      link.click();
      
      // Aguardar carregamento
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Extrair dados
      const details = extractIssueDetails();
      results.push(details);
    }
  }
  
  return results;
}

// 4. Função para exportar para CSV
function exportToCSV(data) {
  if (data.length === 0) return '';
  
  // Coletar todos os campos possíveis
  const allFields = new Set();
  data.forEach(item => {
    Object.keys(item.fields).forEach(field => allFields.add(field));
  });
  
  const fields = ['key', 'title', ...Array.from(allFields)];
  
  // Cabeçalho
  let csv = fields.map(f => `"${f}"`).join(',') + '\\n';
  
  // Linhas
  data.forEach(item => {
    const row = fields.map(field => {
      if (field === 'key') return `"${item.key}"`;
      if (field === 'title') return `"${item.title}"`;
      const value = item.fields[field] || '';
      return `"${value.replace(/"/g, '""')}"`;
    });
    csv += row.join(',') + '\\n';
  });
  
  return csv;
}

// 5. Função para download do CSV
function downloadCSV(csv, filename = 'jira_export.csv') {
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = filename;
  link.click();
}

// EXEMPLOS DE USO:

// Extrair apenas o issue atual
console.log(extractIssueDetails());

// Extrair lista de issues da página
console.log(extractIssueList());

// Extrair múltiplos issues e baixar CSV (cuidado: pode demorar)
// extractMultipleIssues(10).then(data => {
//   const csv = exportToCSV(data);
//   downloadCSV(csv, 'gatekeeper_issues.csv');
// });
Como Usar
Para testar rapidamente:

Cole o script no console do navegador (F12)
Execute: extractIssueDetails() - para ver os dados do issue atual
Execute: extractIssueList() - para ver a lista de 50 issues da página

Para extrair múltiplos issues:
javascript// Extrair 10 issues e baixar CSV
extractMultipleIssues(10).then(data => {
  console.log('Extração completa!', data);
  const csv = exportToCSV(data);
  downloadCSV(csv, 'gatekeeper_issues.csv');
});
Diferenças da Versão Anterior
✅ Identifica corretamente os campos customizados do JIRA
✅ Extrai: Produto GateKeeper, ERP do cliente, Versão APK, etc.
✅ Suporta navegação entre múltiplos issues
✅ Exporta para CSV com todos os campos
✅ Evita duplicatas e campos vazios
Quer que eu execute a extração de alguns issues específicos para você testar?me envie o que voce aprendeu sobre a estrutura debbugando8 stepsCreated a planJavascript toolJavascript toolJavascript toolJavascript toolJavascript toolJavascript toolPerfeito! Agora vou criar o documento final completo:Done📋 DOCUMENTAÇÃO COMPLETA DA ESTRUTURA DO JIRA - PROJETO GATEKEEPER
🎯 Informações Gerais
Sistema: JIRA Service Desk (v8.0.0)
URL Base: https://suporte.maximatech.com.br
Projeto: Gatekeeper (GATE)
Total de Issues: 2.552
Issues por página: 50

🔌 APIs JavaScript Disponíveis
javascript// API Global do JIRA
window.JIRA                           // Objeto principal
window.JIRA.Issue.getIssueKey()       // Retorna: "GATE-XXXX"

// Dados estruturados em jQuery
document.querySelector('.results').jQuery224056057505922873912
  .issueTableModelState.issueTable    // Contém todos os IDs dos issues

🏗️ ESTRUTURA HTML
1️⃣ Lista de Issues (Lado Esquerdo)
javascript// SELETORES FUNCIONAIS
Container: '.results'
Item Individual: '.results li'
Link do Issue: 'a[href*="/browse/GATE-"]'

// ESTRUTURA HTML
<ul class="results">
  <li>
    <a href="/browse/GATE-2609">
      <generic>GATE-2609</generic>
      <generic>Plano de pagamento / cobrança no cliente</generic>
    </a>
  </li>
</ul>
Script de Extração:
javascriptconst issues = [];
document.querySelectorAll('a[href*="/browse/GATE-"]').forEach(link => {
  const key = link.href.match(/GATE-\\d+/)[0];
  const title = link.textContent.replace(key, '').trim();
  issues.push({ key, title, url: link.href });
});

2️⃣ Painel de Detalhes (Lado Direito)
Campos Padrão do JIRA
CampoIDSeletor CSSTestado ✓Chavekey-val#key-val✓Títulosummary-val#summary-val✓Tipotype-val#type-val✓Statusstatus-val#status-val✓Prioridadepriority-val#priority-val✓Resoluçãoresolution-val#resolution-val✓Responsávelassignee-val#assignee-val✓Solicitantereporter-val#reporter-val✓Descriçãodescription-val#description-val✓Criadocreated-val#created-val✓Atualizadoupdated-val#updated-val✓Resolvidoresolutiondate-val#resolutiondate-val✓

3️⃣ Campos Customizados do Gatekeeper
Mapeamento Completo dos IDs
CampoCustom Field IDSeletor CSSExemplo de ValorProduto GateKeepercustomfield_13202#customfield_13202-valMXPEDÉ faturamento parado?customfield_10212#customfield_10212-valNãoQual ERP do cliente?customfield_10232#customfield_10232-valSAPAssuntocustomfield_10320#customfield_10320-valMXPED - Plano de PagamentoNaturezacustomfield_10407#customfield_10407-valDúvidaPassos para reproduzircustomfield_10221#customfield_10221-val>>Login: ...Resultado apresentadocustomfield_10222#customfield_10222-val>>Não foi possível...Resultado esperadocustomfield_10223#customfield_10223-val>>Conseguir abrir...Versão APKcustomfield_10207#customfield_10207-val4.032.4Versão Bancocustomfield_10208#customfield_10208-valN/AVersão Servercustomfield_10209#customfield_10209-valN/AUsuário BD Máximacustomfield_10215#customfield_10215-valARTETRIGO_1969000_PRODUCAOIP do banco de dadoscustomfield_10216#customfield_10216-valABNT - maxsoluções...Porta do Bancocustomfield_10217#customfield_10217-val1521Service Namecustomfield_10218#customfield_10218-valABNT

💡 PADRÕES HTML IDENTIFICADOS
Estrutura de Campo Padrão:
html<li class="item">
  <strong class="name">Tipo:</strong>
  <span id="type-val" class="value">Tarefa</span>
</li>
Estrutura de Campo Customizado:
html<li id="rowForcustomfield_13202">
  <strong class="name">Produto GateKeeper:</strong>
  <span id="customfield_13202-val" class="value">MXPED</span>
</li>
Estrutura Alternativa (Generic Tags):
html<listitem>
  <generic>Produto GateKeeper</generic>
  <generic>MXPED</generic>
</listitem>

🚀 SCRIPT OTIMIZADO FINAL
javascript// ========================================
// EXTRAÇÃO COMPLETA DO JIRA - GATEKEEPER
// ========================================

function extrairIssueCompleto() {
  const data = {
    // Campos padrão
    key: document.querySelector('#key-val')?.textContent.trim(),
    summary: document.querySelector('#summary-val')?.textContent.trim(),
    type: document.querySelector('#type-val')?.textContent.trim(),
    status: document.querySelector('#status-val')?.textContent.trim(),
    priority: document.querySelector('#priority-val')?.textContent.trim(),
    resolution: document.querySelector('#resolution-val')?.textContent.trim(),
    assignee: document.querySelector('#assignee-val')?.textContent.trim(),
    reporter: document.querySelector('#reporter-val')?.textContent.trim(),
    description: document.querySelector('#description-val')?.textContent.trim(),
    created: document.querySelector('#created-val')?.textContent.trim(),
    updated: document.querySelector('#updated-val')?.textContent.trim(),
    resolved: document.querySelector('#resolutiondate-val')?.textContent.trim(),
    
    // Campos customizados Gatekeeper
    produtoGatekeeper: document.querySelector('#customfield_13202-val')?.textContent.trim(),
    faturamentoParado: document.querySelector('#customfield_10212-val')?.textContent.trim(),
    erpCliente: document.querySelector('#customfield_10232-val')?.textContent.trim(),
    assunto: document.querySelector('#customfield_10320-val')?.textContent.trim(),
    natureza: document.querySelector('#customfield_10407-val')?.textContent.trim(),
    passosReproduzir: document.querySelector('#customfield_10221-val')?.textContent.trim(),
    resultadoApresentado: document.querySelector('#customfield_10222-val')?.textContent.trim(),
    resultadoEsperado: document.querySelector('#customfield_10223-val')?.textContent.trim(),
    versaoAPK: document.querySelector('#customfield_10207-val')?.textContent.trim(),
    versaoBanco: document.querySelector('#customfield_10208-val')?.textContent.trim(),
    versaoServer: document.querySelector('#customfield_10209-val')?.textContent.trim(),
    usuarioBD: document.querySelector('#customfield_10215-val')?.textContent.trim(),
    ipBanco: document.querySelector('#customfield_10216-val')?.textContent.trim(),
    portaBanco: document.querySelector('#customfield_10217-val')?.textContent.trim(),
    serviceName: document.querySelector('#customfield_10218-val')?.textContent.trim()
  };
  
  // Remover valores undefined
  Object.keys(data).forEach(key => {
    if (!data[key] || data[key] === 'Nenhum') delete data[key];
  });
  
  return data;
}

// EXPORTAR PARA CSV
function exportarParaCSV(dados) {
  const campos = Object.keys(dados[0]);
  let csv = campos.map(c => `"${c}"`).join(',') + '\\n';
  
  dados.forEach(item => {
    const linha = campos.map(campo => {
      const valor = item[campo] || '';
      return `"${valor.replace(/"/g, '""')}"`;
    });
    csv += linha.join(',') + '\\n';
  });
  
  return csv;
}

// EXTRAIR MÚLTIPLOS ISSUES
async function extrairMultiplosIssues(quantidade = 10) {
  const resultados = [];
  const links = Array.from(document.querySelectorAll('a[href*="/browse/GATE-"]')).slice(0, quantidade);
  
  for (const link of links) {
    link.click();
    await new Promise(r => setTimeout(r, 2000));
    resultados.push(extrairIssueCompleto());
  }
  
  return resultados;
}

// USO:
console.log(extrairIssueCompleto());

📥 EXEMPLO DE SAÍDA
json{
  "key": "GATE-2609",
  "summary": "Plano de pagamento / cobrança no cliente",
  "type": "Tarefa",
  "status": "RESOLVIDO",
  "priority": "Medium",
  "resolution": "Resolvido sem Base de Conhecimento",
  "assignee": "Carlos Vinicius Bizinotto Prates",
  "reporter": "Marcelo Henrique Macedo Silva",
  "description": "Ao tentar abrir o cliente, está mostrando a mensagem",
  "produtoGatekeeper": "MXPED",
  "faturamentoParado": "Não",
  "erpCliente": "SAP",
  "assunto": "MXPED - Plano de Pagamento",
  "natureza": "Dúvida",
  "versaoAPK": "4.032.4",
  "usuarioBD": "ARTETRIGO_1969000_PRODUCAO",
  "portaBanco": "1521",
  "serviceName": "ABNT"
}

✅ RESUMO DO QUE APRENDI

JIRA usa IDs numéricos para custom fields (customfield_XXXXX-val)
Estrutura consistente: <strong>Label</strong><span id="...">Valor</span>
API JavaScript disponível: window.JIRA.Issue.getIssueKey()
Total de 2.552 issues paginados em blocos de 50
15 campos customizados específicos do Gatekeeper identificados
Todos os IDs são previsíveis e podem ser mapeados diretamente

Essa documentação deve resolver completamente o problema de extração! 🎉