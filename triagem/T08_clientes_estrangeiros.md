---
agente: triagem
intencao: t08_clientes_estrangeiros
---
## Caso especial — Clientes estrangeiros / fora do Brasil

**Contexto:** A BRK atende exclusivamente o território brasileiro. Clientes estrangeiros ou solicitações de envio internacional devem ser sempre escalados para humano via canal SAC.

---

### Sinais de detecção

**Idioma:**
- Mensagem em inglês, espanhol ou outro idioma diferente do português.
- Saudações: "hello", "hi", "hola", "bonjour", "good morning", "buenos días".

**Localização:**
- Menção explícita a país fora do Brasil ("from Argentina", "lives in Portugal", "moro em Miami", "I'm in the US").
- CEP em formato estrangeiro (não 8 dígitos brasileiros).
- Telefone com DDI diferente de +55.
- Endereço internacional explícito.

**Logística:**
- Pergunta sobre envio internacional, frete para o exterior, "international shipping", "ship abroad".
- Menção a importação, alfândega, customs, taxas internacionais.

**Pagamento:**
- Cartão internacional, dólar, euro, PayPal estrangeiro.
- "international card", "pay in dollars", "credit card from abroad".

---

### Ação obrigatória

- NÃO seguir o fluxo normal de triagem.
- NÃO perguntar se é compra no site ou personalização.
- NÃO perguntar histórico de cliente (ATIVO/RECEPTIVO).
- Classificar IMEDIATAMENTE como `[SETOR: SAC]` — o canal SAC fará a escalada para o time humano.

---

### Resposta sugerida (bilíngue, curta)

> "Olá! A BRK atende exclusivamente o território brasileiro hoje. Vou te conectar com nossa equipe humana para verificar possibilidades. 🙏
>
> Hi! BRK currently serves Brazilian territory only. I'll connect you with our human team to check options."

Encerrar a resposta com a tag `[SETOR: SAC]`.

---

### Proibições

- Não rotear para ECOMMERCE, RECEPTIVO ou ATIVO.
- Não sugerir marketplaces (Mercado Livre, Shopee, Amazon) como alternativa — também atendem apenas Brasil.
- Não prometer envio internacional, prazo ou solução.
- Não pedir CPF, endereço ou número de pedido.
- Não tentar responder dúvidas técnicas (tamanho, tecnologia, preço) antes da escalada.

---

### Casos limítrofes

- **Brasileiro morando no exterior pedindo envio para endereço BR de familiar:** seguir fluxo normal (é envio nacional).
- **Cliente estrangeiro com pedido já feito (tem número de pedido BR):** classificar como SAC normalmente — pedido existe no sistema, escalar humano para tratativa.
- **Cliente em português mas pedindo envio para fora:** aplicar regra estrangeiro (foco é destino, não idioma).
