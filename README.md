# MyFinancesPython
Project designed to help organize my personal finances

---
### Linting:

-  To see lint-errors:
```bash
    pycodestyle .
```

-  To correct lint-errors:
```bash
    autopep8 --in-place --recursive .
```

---

### Testing
```bash
    python3 -m unittest
```


# DEBT
## Entities
- Description (String) - Recebido
- Valor da Parcela (Float) - Recebido
- Quantidade totais de parcelas(Int) - Recebido
- Valor Total do débito (Float) - Calculado
- Número de parcelas pagas (Int) - Recebido
- Número de parcelas restantes (Int) - Calculado
- Valor restante (float) - Calculado
- Mês que começou/Ano (Month) - Recebido

## Use Cases

- Quero saber quanto eu tenho de dívida nos próximos meses
- Quero saber quanto eu tenho de dívida nesse mês atual
- Precisa conseguir marcar uma dívida como paga para o mês atual

## TODO
- Criar casos de uso:
    - Buscar pelos débitos em aberto
    - Buscar pelas dívidas para um determinado mês

- Implementar Docker-Compose