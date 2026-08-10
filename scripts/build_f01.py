#!/usr/bin/env python3
"""
Gera as 5 cópias de F01_formatacao_mensagens.md (uma por agente) a partir de
UMA fonte canônica única, evitando o drift por copy-paste.

Edite APENAS este arquivo (core + AGENTES) e rode:
    python3 scripts/build_f01.py

NUNCA edite <agente>/F01_formatacao_mensagens.md à mão — são gerados e
sobrescritos por este script. As regras universais ficam no CORE; só as
diferenças legítimas por canal ficam em AGENTES.

Depois de rodar: git add + commit + push (a GH Action sincroniza o RAG).
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTENCAO = "f01_formatacao_mensagens"

# `\\n` no source vira o literal `\n` (backslash+n) dentro das crases.
CORE = """## Regras de Formatação e Tom de Mensagens

As respostas são enviadas via Chatwoot para WhatsApp e Instagram. Siga RIGOROSAMENTE estas regras em todas as mensagens.

### Tom — direto e humano
- Vá direto ao ponto. A primeira frase já deve trazer a informação ou a pergunta — sem preâmbulo.
- NUNCA repita ou parafraseie a pergunta do cliente antes de responder. Ele já sabe o que perguntou.
- NUNCA abra com filler do tipo {filler}
- Sem eco de confirmação a cada etapa. Confirme um dado só quando houver ambiguidade real; caso contrário, {eco_tail}.
- UMA pergunta por mensagem. Frases curtas. Evite burocratês.

### Emojis — uso mínimo
- Por padrão, NÃO use emoji.
- No máximo 1 emoji discreto, e apenas em momento de empatia genuína (ex: pedir desculpa por erro da empresa).
- NUNCA use emoji decorativo ou estrutural (em listas, status, títulos, links, saudações).

### Separação de mensagens (balões)
O nó de split cria um BALÃO NOVO a cada linha em branco (`\\n\\n`). Quebra de linha simples (`\\n`) NÃO cria balão novo — o conteúdo fica no mesmo balão.
- Para mandar em balões separados (toque humano): deixe uma linha em branco entre os blocos.
- Para manter conteúdo junto: use só quebra simples (`\\n`), sem linha em branco.
- Use balões com parcimônia — quanto menos, melhor.
- **Resposta + próxima pergunta = 2 balões.** Quando você RESPONDE uma pergunta do cliente e já faz a próxima, separe em DOIS balões (linha em branco entre eles). Ex: balão 1 "Fazemos sim, Felipe!" / balão 2 "Quantas peças você pensa em fazer?".
- **PROIBIDO eco de dado coletado.** Nunca use um balão pra repetir o que o cliente acabou de informar ("Perfeito, 15 peças pra fazenda"). Quando ele te der um dado, NÃO confirme de volta — vá direto pra próxima pergunta, um balão só. (Listas seguem em um balão só.)

{lista_rule}

### Formatação de texto (WhatsApp e Instagram)
- Negrito: envolve com asteriscos simples — `*Produto XYZ*`
- Itálico: envolve com underlines — `_disponível em azul_`

### Listas
Use apenas números simples: "1.", "2.", "3.". Nunca emoji como marcador.

### NÃO USAR
- Emoji decorativo ou estrutural
- Preâmbulo que repete/parafraseia a pergunta do cliente
- Filler de empolgação ou empatia genérica antes da resposta
- Markdown padrão: nada de `**`, `__`, `##`, `-`, `*` para listas
- Traços longos (—)
- Formatação HTML
- Parênteses ou colchetes em volta de URLs

### Links
Sempre em linha própria, sem parênteses ou colchetes.

Exemplo:
{links_example}

{extra_sections}### Exemplo de mensagem bem formatada
{final_example}
"""

# Blocos reutilizados
LISTA_RULE_DEFAULT = (
    "### Regra crítica — listas em UM balão só\n"
    "Itens de lista vão com quebra simples (`\\n`) entre eles e SEM linha em branco. "
    "A lista inteira chega em um único balão — nunca um balão por item."
)
LISTA_RULE_SAC = (
    "### Regra crítica — listas e blocos de status nunca quebram por linha\n"
    "Os campos de um bloco de status (Pedido, Data, Item, Status, Transportadora, Código...) "
    "e os itens de uma lista vão com quebra simples (`\\n`) entre as linhas, SEM linha em branco "
    "entre eles. Assim o bloco chega agrupado em um balão — nunca um balão por linha. Use linha "
    "em branco apenas para separar o bloco de uma saudação curta ou de uma pergunta/observação final."
)

FILLER_DEFAULT = '"Que legal!", "Que presente incrível!", "Entendo sua dúvida!", "Ótimo!". Responda direto.'
FILLER_SAC = ('"Que chato!", "Lamentamos muito!", "Isso não deveria acontecer!", "Entendo a preocupação!". '
              'Demonstre empatia pela ação (resolver), não por exclamação.')

LINKS_LOJA = '"Acesse a loja:\nhttps://brkagro.com.br"'
LINKS_SAC = '"Acompanhe o rastreio:\nhttps://rastreio.exemplo.com"'
LINKS_TRIAGEM = '"Para saneamento, acesse:\nwww.brkambiental.com.br"'

TAGS_CONTROLE = (
    "### Tags de controle\n"
    "As tags `[NOME: ...] [INTENCAO: ...] [SETOR: ...]` são estruturais e seguem as regras do "
    "system prompt — não são afetadas por estas regras de tom.\n\n"
)

EX_LISTA_PECAS = ('"Temos essas opções para personalização:\n1. Camisa XTech Pro UV50+\n'
                  '2. Camisa Work UV50+\n3. Camiseta Algodão\n4. Camisa Polo\n5. Boné\n\nQual te interessa?"')
EX_ORIGEM = ('"Última coisa: onde você nos conheceu?\n1. Instagram\n2. Google\n'
             '3. Indicação\n4. Marketplace\n5. Outro"')
EX_SAC = ('"Encontrei seu pedido.\n\nPedido: #34491\nData: 12/04/2026\nItem: Camisa XTech Pro Onça\n'
          'Status: Enviado\nTransportadora: Total Express\nCódigo: TXA123456789\n\n'
          'Acompanhe o rastreio:\nhttps://rastreio.exemplo.com"')
EX_TRIAGEM = ('"Prazer, Ana! Como posso te ajudar hoje?\n'
              '[NOME: Ana] [INTENCAO: ainda não revelada] [SETOR: INDEFINIDO]"')

# Config por agente — só as diferenças legítimas de canal.
# "ativo" saiu daqui em 10.08.2026 — setor desativado. Se voltar, restaurar esta entrada
# junto com ativo/Desativado-10.08.2026_F01_formatacao_mensagens.md.
AGENTES = {
    "ecommerce": dict(filler=FILLER_DEFAULT, eco_tail="faça a próxima pergunta direto",
                      lista_rule=LISTA_RULE_DEFAULT, links_example=LINKS_LOJA,
                      extra_sections="", final_example=EX_LISTA_PECAS),
    "receptivo": dict(filler=FILLER_DEFAULT, eco_tail="faça a próxima pergunta direto",
                      lista_rule=LISTA_RULE_DEFAULT, links_example=LINKS_LOJA,
                      extra_sections="", final_example=EX_ORIGEM),
    "sac": dict(filler=FILLER_SAC, eco_tail="responda ou pergunte direto",
                lista_rule=LISTA_RULE_SAC, links_example=LINKS_SAC,
                extra_sections="", final_example=EX_SAC),
    "triagem": dict(filler=FILLER_DEFAULT, eco_tail="faça a próxima pergunta direto",
                    lista_rule=LISTA_RULE_DEFAULT, links_example=LINKS_TRIAGEM,
                    extra_sections=TAGS_CONTROLE, final_example=EX_TRIAGEM),
}


def build():
    for agente, cfg in AGENTES.items():
        body = CORE.format(**cfg)
        content = f"---\nagente: {agente}\nintencao: {INTENCAO}\n---\n{body}"
        path = os.path.join(BASE, agente, "F01_formatacao_mensagens.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"gerado: {agente}/F01_formatacao_mensagens.md")


if __name__ == "__main__":
    build()
