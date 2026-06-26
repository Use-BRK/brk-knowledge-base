import sys
import json
import urllib.request
import os

if len(sys.argv) < 2:
    print("Uso: python3 delete_chunk.py <filepath>", file=sys.stderr)
    sys.exit(1)

filepath = sys.argv[1]

payload = json.dumps({"file": filepath}).encode('utf-8')

url = os.environ['N8N_DELETE_WEBHOOK_URL']
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

try:
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        print(f"DELETED: {filepath} | status={resp.status} | response={body}")
except urllib.error.HTTPError as e:
    print(f"ERRO ao deletar {filepath}: status={e.code} | {e.reason}", file=sys.stderr)
    sys.exit(1)