Estes códigos são usados para formatar o texto no terminal (ANSI escape sequences). A sintaxe geral é `\\033[ESTILO;TEXTO;FUNDOm`.

## Tabela de Referência

| Estilo | Descrição |
| :--- | :--- |
| 0 | Normal (None) |
| 1 | Negrito (Bold) |
| 4 | Sublinhado (Underline) |
| 7 | Negativo (Inverte cores) |

### Códigos de Cor (Texto: 30-37, Fundo: 40-47)

| Cor | Texto | Fundo |
| :--- | :--- | :--- |
| Branco | 30 | 40 |
| Vermelho | 31 | 41 |
| Verde | 32 | 42 |
| Amarelo | 33 | 43 |
| Azul | 34 | 44 |
| Magenta | 35 | 45 |
| Ciano | 36 | 46 |
| Cinza/Preto | 37 | 47 |

---

## Exemplos em Python

Para usar, você deve seguir a estrutura: `print('\\033[ESTILO;COR_TEXTO;COR_FUNDO m TEXTO \\033[m')`. O final `\\033[m` é essencial para "limpar" a formatação.
