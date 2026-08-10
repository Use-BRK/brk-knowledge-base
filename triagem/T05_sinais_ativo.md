---
agente: triagem
intencao: t05_sinais_ativo
---
## Setor ATIVO — Desativado-10.08.2026 (não use)

**O setor ATIVO foi desativado em 10.08.2026.** A operação é toda receptiva agora. Este chunk existe só para anular a instrução antiga: se você recuperar qualquer orientação sobre "classificar como ATIVO", ela está obsoleta.

> Nota de manutenção: o nome do arquivo e o campo `intencao: t05_sinais_ativo` foram mantidos de
> propósito. A ingestão do PGVector deleta e reinsere por `agente+intencao`, então manter a chave é o
> que garante que este texto SOBRESCREVA o chunk antigo em vez de criar um novo e deixar o antigo
> órfão no vetor, ainda mandando classificar ATIVO.

### Regra atual
- É PROIBIDO emitir `[SETOR: ATIVO]`. Os únicos valores válidos são SAC, ECOMMERCE, RECEPTIVO e INDEFINIDO.
- Cliente recorrente de personalizado — "quero repetir o pedido", "refazer o mesmo", "segunda remessa", "a arte que aprovei", "o layout que vocês têm", "quero renovar o uniforme da equipe", "faço pedido todo ano", "já sou cliente", "meu atendente era X" → **[SETOR: RECEPTIVO]**.
- Referência a pedido JÁ FEITO em que o cliente quer status, prazo de produção ou rastreio → **[SETOR: SAC]** (isso não mudou).

### Pergunta que saiu de uso
NÃO pergunte mais "você já fez algum pedido personalizado com a BRK antes?" nem qualquer variação sobre ser cliente novo ou recorrente. O roteamento não distingue mais os dois, então a pergunta só gasta um turno do cliente.

### Classificação: RECEPTIVO (nunca ATIVO)
