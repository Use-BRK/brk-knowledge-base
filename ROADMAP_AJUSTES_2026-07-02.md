# Roadmap — Ajustes KB Beka (2026-07-02)

Origem: varredura de 5 auditorias (triagem/sac/ecommerce/receptivo/ativo+F01).
Padrão-raiz: chunks de era antiga contradizem os system prompts atuais dos nós → RAG injeta comportamento errado no agente live.
Deploy: editar `.md` → commit → push `main` → GH Action → n8n reingere via PGVector.
Prioridade: agentes LIVE = Triagem, SAC, Receptivo (E-commerce e Ativo estão DESABILITADOS no flow).

## 🔴 CRÍTICO (contradiz prompt, agente live)
- [x] C1 — `sac/SAC02`: remover Script 7 (consulta/rastreio via Shopify) + Scripts 1,2 + Passo 8 → converter em triagem (motivo/titular/cpf/pedido/descrição) + escala humano
- [x] C2 — `sac/SAC01` l.24,31: 1ª ação = triagem objetiva; pedido opcional; "rastrear" não é lookup
- [x] C3 — `receptivo/RE02`,`RE04`: recusa de e-mail = seguir + flag `[SEM_EMAIL]` (hoje diz "sem flag")
- [x] C4 — `receptivo/RE02`,`RE04`,`RE05`: handoff ecommerce via ferramenta `Transferir Atendimento` destino='ecommerce' (hoje usa tag `[TROCA_ASSUNTO: true]`)
- [x] C5 — `triagem/T01`: formato de saída = 3 tags `[NOME][INTENCAO][SETOR]` + incluir INDEFINIDO (hoje 1 tag, sem INDEFINIDO)
- [x] C6 — `ativo/AT02` Script 4: remover "prazo ~7 dias úteis" (proibido; só humano confirma)

## 🟠 LACUNAS (prompt roteia, chunk não cobre)
- [x] L1 — `triagem/T06` + `triagem/T00`: add casos parceria/influencer (→WhatsApp 34 99718-3473) e fornecedor/novo negócio (→contato@/financeiro@usebrk.com.br)
- [x] L2 — `triagem/T02`: add sinais SAC "horário de atendimento/funcionamento, endereço, localização"
- [x] L3 (arrependimento CDC + portal com URL; garantia sem prazo inventado) — `sac/SAC04`: add política de arrependimento (7 dias/CDC) + garantia legal defeito **(precisa validar termos exatos)**
- [x] L4 (portal https://brk.troque.app.br/ em SAC04/SAC05) — `sac`: link do portal de trocas **(URL desconhecida — precisa do time)**
- [x] L5 (novo chunk ecommerce/EC06_trocas_devolucoes + link política) — `ecommerce`: chunk troca/devolução **(precisa política; agente desabilitado — baixa)**

## 🟡 PLACEHOLDERS / formatação errada em exemplos
- [x] P1 — `triagem/T03:26`: remover resposta substantiva de marketplace + `[LINKS A ADICIONAR]` (triagem só classifica)
- [x] P2 — `ecommerce/EC04:37-42`: preencher `[LINK A ADICIONAR]` a partir do EC05 (ou deferir ao EC05)
- [x] P3 — `ecommerce/EC05`,`EC04`,`EC02`: exemplos com `•`, parênteses em URL, traço longo `—` → corrigir p/ regra F01
- [x] P4 — `ecommerce/EC02:45`: `search_catalog` → nome real (tools Shopify Fishing/Agro/Motors)
- [x] P5 — `ecommerce/EC02:77-80`: remover "mais vendidos abril 2026" (stale/volátil; usar Shopify ao vivo)

## 🟢 F01 DRIFT / convenção / redundância
- [x] F1 — `triagem/F01`: restaurar seção "Links" + bullet "sem eco de confirmação" (perdidos no drift)
- [x] F2 — padronizar wording do emoji nas 5 cópias F01
- [x] F3 — `sac/SAC05`: `intencao: horarios_funcionamento` → `sac05_horarios_funcionamento`
- [x] F4 — remover regras de formatação duplicadas em SAC02 e RE02/04/05 (deixar só no F01)
- [x] AT — `ativo/AT02` Script 4 + `ativo/AT01`: prazo/arte = confirmação via humano; `ativo/AT00`: add mecanismo de handoff + 1 exemplo
- [x] SYNC — `triagem/T00` sincronizar com node (casos especiais) — coberto por L1

## 📌 Melhorias estruturais (FEITAS 2026-07-02)
- [x] Gerador `scripts/build_f01.py`: 5 cópias F01 de fonte canônica única + overrides por canal (elimina drift). README documenta.
- [x] `sync_chunk.py`: log SKIP explícito (sem frontmatter=intencional) + AVISO (frontmatter incompleto=possível erro)
- [ ] E-commerce: reabilitar nós ou remover chunks órfãos do RAG (pendente — decisão de produto)
- [x] Ativo: setor extinto em 2026-08-10. Roteamento `Canal[ativo]` → `Agente Beka (Receptivo)`, ramo de
      transferência do ativo desabilitado, triagem não emite mais `[SETOR: ATIVO]` e os chunks de triagem
      que mandavam classificar ATIVO foram corrigidos. Chunks em `ativo/` seguem órfãos no PGVector (inertes).
