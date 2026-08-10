# BRK Knowledge Base

Base de conhecimento RAG da BRK — alimenta os agentes de IA (Beka) via PGVector no n8n.

## Estrutura

```
ecommerce/   → chunks do agente Beka E-commerce
triagem/     → chunks do agente Beka Triagem
ativo/       → SETOR DESATIVADO — chunks órfãos, ver abaixo
receptivo/   → chunks do agente Beka Receptivo
sac/         → chunks do agente Beka SAC
```

### Setor Ativo desativado

O setor **Ativo** foi extinto: a operação é toda receptiva. No `[Webhook] Beka com RAG` a saída `ativo`
do switch `Canal` foi reapontada para o `Agente Beka (Receptivo)`, e todo o ramo de transferência do
ativo (`Idem Transf Ativo` → `1a vez Ativo?` → `Msg Transferência Ativo` → `Prep Transf Ativo (zSI0)` →
`Atribui Time Ativo`) está desabilitado. A triagem não emite mais `[SETOR: ATIVO]`.

Os arquivos de `ativo/` foram renomeados com o prefixo `Desativado-10.08.2026_` em vez de apagados —
fica o rastro de quando saíram. Eles seguem no PGVector como `agente: ativo`, mas nenhum agente os
recupera (o retrieval filtra por `agente`). Para limpar o vetor de verdade, delete os arquivos em UM
commit e confirme antes que o secret `N8N_DELETE_WEBHOOK_URL` esteja configurado — é ele que dispara o
`scripts/delete_chunk.py`.

Já `triagem/T05_sinais_ativo.md` **não** foi renomeado: ele é chunk de um agente vivo, e manter o nome
e a `intencao` é o que faz o texto novo sobrescrever o antigo no vetor. Renomear ali criaria um chunk
novo e deixaria o antigo órfão, ainda mandando a triagem classificar ATIVO.

## Como atualizar um chunk

1. Edite o arquivo `.md` correspondente
2. Faça commit e push para a branch `main`
3. O GitHub Actions detecta a mudança automaticamente
4. O n8n deleta o chunk antigo e reingerida o novo via PGVector

## Estrutura de cada arquivo

Todo arquivo `.md` deve ter o frontmatter:

```yaml
---
agente: ecommerce  # ecommerce | triagem | receptivo | sac  (ativo: desativado 10.08.2026)
intencao: ec01_guia_tamanhos  # identificador único do chunk
---
```

## F01 (formatação de mensagens) — NÃO editar à mão

Cada agente tem seu próprio `F01_formatacao_mensagens.md` (o retrieval filtra por `agente`, então cada um precisa da sua cópia). Para evitar drift por copy-paste, as 4 cópias são **geradas** de uma fonte canônica única:

- Fonte: `scripts/build_f01.py` (CORE = regras universais; `AGENTES` = só as diferenças legítimas de canal).
- Regenerar: `python3 scripts/build_f01.py` → sobrescreve os 4 `<agente>/F01_formatacao_mensagens.md`.
- O `ativo` saiu do dict `AGENTES` em 10.08.2026 (setor desativado) — por isso o gerador não recria mais `ativo/F01_formatacao_mensagens.md`.
- **NUNCA edite os `F01_formatacao_mensagens.md` diretamente** — edite o `build_f01.py` e rode o gerador.

## Configuração necessária

No repositório GitHub, configure o secret:
- `N8N_WEBHOOK_URL` → URL do webhook do fluxo de sincronização no n8n

## Notas de operação (gotchas)

- **Squash antes de push:** a GH Action detecta mudanças via `git diff HEAD~1 HEAD` (checkout `fetch-depth: 2`), então enxerga apenas o ÚLTIMO commit. Push com múltiplos commits sincroniza só o commit do topo. Junte tudo em UM commit antes do push.
- **Renomear `intencao` órfã o chunk antigo:** a ingestão deleta por `agente+intencao`. Mudar o `intencao:` cria um chunk novo e deixa o antigo órfão no PGVector. Se renomear, limpe o antigo.
- Arquivos sem frontmatter (`*_system_prompt.md`, README, ROADMAP) são pulados pelo sync de propósito (log `SKIP`).

