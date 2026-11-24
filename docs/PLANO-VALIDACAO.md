# Plano de validação Mini Lead

1. Fixar revisão upstream FMini-1 e referência Custom V022. Identificar SDK/toolchain e licenças; registrar hashes e versões. Não publicar SDK proprietário.
2. Compilar baseline sem alterações; registrar comandos, logs, mapa de memória e artefatos privados. Se falhar, isolar dependência antes de alterar síntese.
3. Integrar BLE MIDI em mudança isolada. Verificar APIs reais, RX/TX, filas, reconexão, Note Off, CC, pitch bend e coexistência USB/TRS. Não copiar offsets binários entre versões.
4. Comparar baseline e candidato: motores, presets, polifonia, efeitos, memória e latência. Preparar recuperação e preservar calibração. Teste físico somente com autorização e candidato validado.
5. Em paralelo, especificar presets gospel, pads, interface e site sem alterar baseline. Integrar individualmente após aprovação dos testes.

Estado: plano de testes, não execução. Solicitar ao usuário apenas dependências, permissões ou testes físicos específicos quando necessários.
