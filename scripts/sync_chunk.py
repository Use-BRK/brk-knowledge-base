import sys
import re
import json
import urllib.request
import os

if len(sys.argv) < 2:
    print("Uso: python3 sync_chunk.py <filepath>", file=sys.stderr)
    sys.exit(1)

filepath = sys.argv[1]

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Extrai frontmatter
fm_match = re.match(r'^---\s*\n([\s\S]*?)\n---\s*\n', content)
if not fm_match:
    print(f"Sem frontmatter: {filepath}", file=sys.stderr)
    sys.exit(0)

fm = fm_match.group(1)
agente_match = re.search(r'^agente:\s*(.+)$', fm, re.MULTILINE)
intencao_match = re.search(r'^intencao:\s*(.+)$', fm, re.MULTILINE)

if not agente_match or not intencao_match:
    print(f"Frontmatter incompleto em: {filepath}", file=sys.stderr)
    sys.exit(0)

agente = agente_match.group(1).strip()
intencao = intencao_match.group(1).strip()

# Remove frontmatter do conteúdo
clean = re.sub(r'^---[\s\S]*?---\s*\n', '', content, count=1).strip()

payload = json.dumps({
    "file": filepath,
    "agente": agente,
    "intencao": intencao,
    "content": clean
}).encode('utf-8')

url = os.environ['N8N_WEBHOOK_URL']
req = urllib.request.Request(
    url,
    data=payload,
    # UA explícito: o Cloudflare na frente do n8n bloqueia o User-Agent
    # padrão do urllib ("Python-urllib/x.y") com 403 Forbidden.
    headers={
        'Content-Type': 'application/json',
        'User-Agent': 'brk-knowledge-base-sync/1.0',
    }
)

with urllib.request.urlopen(req) as resp:
    print(f"OK: {filepath} | agente={agente} | intencao={intencao} | status={resp.status}")
