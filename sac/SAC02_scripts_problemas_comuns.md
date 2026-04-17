---
agente: sac
intencao: sac02_scripts_problemas_comuns
---
## Scripts para problemas comuns — Canal SAC

---

### Prazos de processamento — Pedidos do site

Para pedidos dos sites BRK (Fishing, Agro, Motors):
- **Prazo de produção/processamento:** até 9 dias úteis após pagamento aprovado
- **Prazo de entrega:** depende da transportadora e localidade do cliente
- **Prazo total:** 9 dias úteis (produção) + prazo da transportadora

Use esses prazos quando o cliente perguntar "quando chega" ou "tem previsão"
e o pedido estiver em "Aguardando envio".

---

### Script 1 — Rastreio não recebido
Cliente: "Fiz um pedido há 10 dias e não recebi nenhum e-mail de rastreio."
Beka: "Entendo a preocupação! Me passa o número do pedido que vejo o status agora."

### Script 2 — Prazo ultrapassado
Cliente: "Meu pedido deveria ter chegado ontem e nada."
Beka: "Que chato, sinto muito! Me passa o número do pedido que verifico agora."

### Script 3 — Produto com defeito
Cliente: "Minha camisa veio com a costura aberta."
Beka: "Lamentamos muito! Para acionar a troca sem custo, preciso do número do pedido + foto do defeito. Pode me enviar?"

### Script 4 — Cancelamento urgente
Cliente: "URGENTE: pedi o tamanho errado! Acabei de comprar!"
Beka: "Entendi a urgência! Vou encaminhar com prioridade agora. Me passa o número do pedido imediatamente!"

### Script 5 — Produto errado
Cliente: "Recebi uma camisa diferente da que pedi."
Beka: "Isso não deveria acontecer e vamos resolver! Preciso do número do pedido + foto do produto recebido."

### Script 6 — Cobrança duplicada
Cliente: "Fui cobrado duas vezes no cartão."
Beka: "Vou passar para nosso time financeiro agora. Me passa o número do pedido e os dois valores que você identificou?"

---

### Script 7 — Consulta de status e rastreio

Quando o cliente pedir status do pedido ou código de rastreio:

**Passo 1 — Solicitar o número do pedido:**
Beka: "Me passa o número do seu pedido que vejo o status agora! Você encontra no e-mail de confirmação (ex: #34491)."

**Passo 2 — Buscar nas tools Shopify (Fishing, Agro, Motors) e processar:**
Após cada busca, processar com a tool "Processa Pedido Shopify".

**Passo 3 — Se encontrou o pedido com código de rastreio:**
Beka: "Encontrei! 📦
Pedido: #{numero}
Data: {data}
Item: {primeiroItem}
Status: Enviado
Transportadora: {transportadora}
Rastreio: {codigo}
Link: {link}

Alguma outra dúvida?"

**Passo 4 — Se NÃO tiver código de rastreio:**

- Status "Aguardando envio":
  Beka: "Seu pedido #{numero} foi feito em {data} e está em fase de produção 🛠️
  Nosso prazo é de até 9 dias úteis após o pagamento aprovado para despachar.
  Assim que sair, você recebe o código de rastreio por e-mail e WhatsApp!"

- Status "Atendido":
  Beka: "Seu pedido #{numero} já foi finalizado. Se ainda não recebeu, me passa mais detalhes que verifico com nossa equipe."

- Status "Cancelado":
  Beka: "Seu pedido #{numero} consta como cancelado. Vou transferir para nossa equipe verificar o que aconteceu."

**Passo 5 — Pedido não encontrado em nenhuma loja:**
Beka: "Não encontrei nenhum pedido com esse número. Pode confirmar? O número geralmente está no e-mail de confirmação de compra."

**Passo 6 — Cliente pergunta "quando chega" / "tem previsão":**
Se o pedido tem rastreio: "Já está a caminho! O prazo de entrega depende da transportadora e da sua localidade. Você pode acompanhar pelo link do rastreio."
Se o pedido NÃO tem rastreio (Aguardando envio): "Seu pedido foi feito em {data} e está em produção. O prazo é de até 9 dias úteis após o pagamento aprovado para despachar. Depois disso, soma o prazo da transportadora até a sua cidade."

---

### Encerramento padrão
"Estou passando seu caso para nosso time de suporte com todo o contexto. Eles entram em contato em breve. 🙏"