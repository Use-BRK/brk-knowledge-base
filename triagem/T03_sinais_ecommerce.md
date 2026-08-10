---
agente: triagem
intencao: t03_sinais_ecommerce
---
## Sinais de intenção — E-commerce

**Quem é:** cliente pesquisando ou prestes a comprar no site. Não tem intenção de personalizar.

### Classificar como ECOMMERCE quando mencionar:
- "qual a diferença entre", "qual camisa é melhor para"
- "qual tamanho", "tenho X cm de tórax"
- "quanto custa", "qual o preço" — SEM mencionar personalização
- "aceitam boleto", "posso parcelar"
- "qual o prazo", "quanto custa o frete"
- "quero comprar no site", "como faço para comprar"
- "cupom não funciona", "não consigo finalizar"
- "tem em estoque", "tem disponível"
- "Mercado Livre", "Shopee", "Amazon", "Magazine Luiza", "Americanas"
- "marketplace", "loja virtual", "loja online"
- "vocês vendem no", "posso comprar pelo", "têm loja no"
- "achei no ML", "vi no marketplace"

### Perguntas sobre marketplaces
Pergunta sobre comprar em marketplace (Mercado Livre, Shopee, Amazon) → classificar como ECOMMERCE. A triagem NÃO envia links nem responde o conteúdo — apenas classifica; os links oficiais são entregues pelo agente de E-commerce (chunk ec05_canais_venda_marketplaces).

### Suporte para compras em marketplaces
Problema com pedido já feito em marketplace → classificar como SAC (segue o fluxo normal de suporte).

### NÃO classificar como ECOMMERCE quando mencionar:
- "personalizado", "personalizar", "uniforme", "logo", "bordado"
- "mínimo de peças", "orçamento para personalizar"
- "quero colocar minha marca", "camisa com o nome da empresa"
- Qualquer intenção de customização → usar RECEPTIVO

### Perfil emocional típico
Curioso (primeira compra), indeciso (compara modelos), presenteando.

### Quando transferir para humano
- Site com erro técnico persistente
- Cobrança realizada mas pedido não gerado

### Classificação: ECOMMERCE
