# Teste de serialização FMini-1 — 2026-11-26

Upstream fixado: ruppert/fmini-1@c39e186699a6478502267210579bda81480e3823, web/editor_fmini.html.

Executadas as funções originais objectToSnap e validSound em JavaScript, extraídas diretamente do arquivo upstream, com fixture sintética serializada e desserializada em JSON. Quatro casos passaram: remapeamento E1–E7 e exclusão SLOT para pe0=95,103,111 (contagens sintéticas, não identificação de versões reais), e rejeição de patch de comprimento 1. Patch de 32 bytes preservado. Não houve comunicação USB nem teste sonoro.

O run 45617573739 retornou lista de artefatos vazia; nenhum FWSC recuperado. Nenhum binário alterado.

Próximo passo: usar exportação real Save Sound e descritores do dispositivo para gerar variantes com limites reais, sem modificar globais nem slots. Backup integral antes de gravar.
