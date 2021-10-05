# MyFinancesPython
Project designed to help organize my personal finances


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
- Array de meses que tem que ser pago(Array de Month) - Calculado

## Use Cases

- Quero saber quanto eu tenho de dívida nos próximos meses
- Quero saber quanto eu tenho de dívida nesse mês atual
- Precisa conseguir marcar uma dívida como paga para o mês atual
- Deletar um débito
- Adicionar um novo débito
- Atualizar um débito

## TODO
- Testar erros nos casos de uso
- Adicionar array de meses
- Criar casos de uso:
    - Deletar um débito
    - Buscar pelos débitos em aberto
    - Buscar pelas dívidas para um determinado mês

- Adicionar o Mongo
- Criar Adapter para o Flask
- Criar validações com o cerberus
- Implementar Docker-Compose