# BRK Knowledge Base

Base de conhecimento RAG da BRK — alimenta os agentes de IA (Beka) via PGVector no n8n.

## Estrutura

```
ecommerce/   → chunks do agente Beka E-commerce
triagem/     → chunks do agente Beka Triagem
ativo/       → chunks do agente Beka Ativo
receptivo/   → chunks do agente Beka Receptivo
sac/         → chunks do agente Beka SAC
```

## Como atualizar um chunk

1. Edite o arquivo `.md` correspondente
2. Faça commit e push para a branch `main`
3. O GitHub Actions detecta a mudança automaticamente
4. O n8n deleta o chunk antigo e reingerida o novo via PGVector

## Estrutura de cada arquivo

Todo arquivo `.md` deve ter o frontmatter:

```yaml
---
agente: ecommerce  # ecommerce | triagem | ativo | receptivo | sac
intencao: ec01_guia_tamanhos  # identificador único do chunk
---
```

## Configuração necessária

No repositório GitHub, configure o secret:
- `N8N_WEBHOOK_URL` → URL do webhook do fluxo de sincronização no n8n

