# Preservação do FMini-1

Requisito de desenvolvimento: preservar integralmente os motores, presets, efeitos, interface, arpejador, sequenciador e controles existentes. Não substituir módulos funcionais sem necessidade.

## Controles a verificar e preservar
PATCH, PARA, FX, GLOBE/GLOBAL, ARP, SEQUENCE REC, SEQUENCE PLAY, oitavas, modulation, pitch bend, FADER BANK 1 e 2, knobs, faders e pads. Confirmar no código original todas as funções, atalhos e bancos antes de modificar. Os nomes e funções relatados pelo usuário são requisitos preliminares, não resultados de teste.

## Exceções propostas
Bluetooth: recuperar BLE MIDI bidirecional; verificar conflito com salvamento de presets e alternativa sem sacrificar atalhos. Global: acrescentar Operating Mode (Synthesizer/MIDI Controller), preservando navegação existente. Modo controlador deve preservar controles MIDI e evitar notas travadas. Não assumir disponibilidade de SHIFT ou atribuição de knobs sem verificar.

## Aceitação
Comparar cada controle e combinação antes/depois, em ambos os modos quando aplicável. Testar arpejador, sequenciador, bancos de faders, modulação, pitch, oitavas, edição, efeitos, presets, USB/TRS/BLE e recuperação. Registrar resultados reais e testes físicos pendentes. Não liberar firmware sem validação.

Base: https://github.com/ruppert/fmini-1 . Outros firmwares são referências complementares, não substitutos da base.
