# Neon Performance Pads — proposta técnica

Estado: especificação, não implementação validada. Base FMini-1; preservar todos os recursos originais.

Banco 1: 16 posições lógicas. Banco 2: manter comportamento original ou MIDI externo configurável. Confirmar quantidade física e mapeamento no hardware.

## Kits propostos
1. Drum: Kick, Snare, Clap, Tom (P01–04).
2. Percussion: Hi-Hat, Open Hat, Crash, Reverse (P05–08).
3. Worship Transition: Riser, Downlifter, Impact, Swell (P09–12).
4. Atmosphere: Shimmer, Heaven (P13–14).
5. FX: Sparkle, Sub Drop (P15–16).

## Edição
Selecionar pad sem disparo acidental; editar volume, afinação, ataque, decay, release, cutoff, ressonância e envio de reverb/delay conforme suporte real. Priorizar reverb. Efeitos independentes por envio a barramentos compartilhados se possível, sem alterar parâmetros do timbre principal; tempos e feedback podem ser globais ao barramento. Shimmer real depende de processamento de pitch disponível. Salvar ajustes explicitamente, preservar originais.

## Interface
Português brasileiro, rolagem, fonte legível, indicador P01–P16 e banco na barra superior. Proposta de submenu Global > Pads; PARA/FX somente em contexto explícito de edição de pads, sem substituir atalhos originais. Volume de pads independente, master comum. Pads não entram no detector de acordes das teclas. Roteamento interno/MIDI externo configurável.

## Validação
Verificar arquitetura multitímbrica, RAM, flash, CPU, polifonia, latência, saturação, caudas de efeitos, notas travadas, persistência e regressões. Preferir síntese leve e barramentos compartilhados; não reduzir recursos originais sem autorização. Se inviável, manter pads MIDI externos. Nenhum firmware liberado por esta especificação.
