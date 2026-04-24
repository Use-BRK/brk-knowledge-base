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
    headers={'Content-Type': 'application/json'}
)

try:
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        print(f"DELETED: {filepath} | status={resp.status} | response={body}")
except urllib.error.HTTPError as e:
    print(f"ERRO ao deletar {filepath}: status={e.code} | {e.reason}", file=sys.stderr)
    sys.exit(1)