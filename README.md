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

## F01 (formatação de mensagens) — NÃO editar à mão

Cada agente tem seu próprio `F01_formatacao_mensagens.md` (o retrieval filtra por `agente`, então cada um precisa da sua cópia). Para evitar drift por copy-paste, as 5 cópias são **geradas** de uma fonte canônica única:

- Fonte: `scripts/build_f01.py` (CORE = regras universais; `AGENTES` = só as diferenças legítimas de canal).
- Regenerar: `python3 scripts/build_f01.py` → sobrescreve os 5 `<agente>/F01_formatacao_mensagens.md`.
- **NUNCA edite os `F01_formatacao_mensagens.md` diretamente** — edite o `build_f01.py` e rode o gerador.

## Configuração necessária

No repositório GitHub, configure o secret:
- `N8N_WEBHOOK_URL` → URL do webhook do fluxo de sincronização no n8n

## Notas de operação (gotchas)

- **Squash antes de push:** a GH Action detecta mudanças via `git diff HEAD~1 HEAD` (checkout `fetch-depth: 2`), então enxerga apenas o ÚLTIMO commit. Push com múltiplos commits sincroniza só o commit do topo. Junte tudo em UM commit antes do push.
- **Renomear `intencao` órfã o chunk antigo:** a ingestão deleta por `agente+intencao`. Mudar o `intencao:` cria um chunk novo e deixa o antigo órfão no PGVector. Se renomear, limpe o antigo.
- Arquivos sem frontmatter (`*_system_prompt.md`, README, ROADMAP) são pulados pelo sync de propósito (log `SKIP`).

