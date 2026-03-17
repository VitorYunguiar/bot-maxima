import json
import glob
import re

# arquivos json
files = sorted(glob.glob("json_gates_*.json"))

def slug(text):
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text

entries = []

for f in files:
    with open(f, encoding="utf-8") as file:
        entries.extend(json.load(file))

md = []

md.append("# Casos Resolvidos — Gatekeeper maxPedido\n")
md.append("**Sistema:** maxPedido\n")
md.append("**Área:** Suporte Técnico / Diagnóstico\n")
md.append("\n---\n")

for i, item in enumerate(entries, start=1):

    contexto = slug(item["contexto"])
    resposta = slug(item["resposta"])

    md.append(f"## Caso {i}\n")

    md.append("**Contexto**\n")
    md.append(contexto + "\n")

    md.append("\n**Solução / Diagnóstico**\n")
    md.append(resposta + "\n")

    md.append("\n---\n")

with open("07-GATEKEEPER-CASOS-RESOLVIDOS.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md))

print("Documento gerado: 07-GATEKEEPER-CASOS-RESOLVIDOS.md")