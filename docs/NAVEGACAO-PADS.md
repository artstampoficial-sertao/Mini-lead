# Navegação do editor de pads

Proposta, não implementada. Complementa PERFORMANCE-PADS.md.

- PATCH retorna à tela principal de timbres, sem interromper notas ou alterar o timbre principal.
- Atalho candidato: PAD 1 + PAD 9 por aproximadamente 1 segundo. Validar disposição física, conflitos, latência e disparos acidentais. Alternativa preferível se houver conflito: GLOBAL + PAD 1, desde que compatível com a navegação original.
- Editor permite selecionar posição lógica P01–P16 do banco, atribuir som de um dos 3–5 kits auxiliares, ajustar volume e parâmetros.
- PARA e FX editam o pad selecionado apenas no contexto explícito do editor. Fora dele preservam comportamento original FMini-1.
- Knobs seguem convenções existentes após verificação do código. Seleção sem disparo acidental, opção de audição e salvamento explícito.
- PATCH sai do contexto de edição; definir política de alterações não salvas sem bloquear performance.
- Preservar identificação de acorde, estado Bluetooth, volume master, modo e indicador de pad.
- Testar notas simultâneas, latência, troca de banco, efeitos, persistência e regressão de todos os atalhos originais.
- Nenhuma funcionalidade de firmware foi implementada por este documento.
