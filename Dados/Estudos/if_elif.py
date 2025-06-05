meta = 50  # Meta ajustada para um valor mais realista
vendas = 0.00
quantidade_vendida = 24
preco_venda = 100.00  # Adicionado um preço de venda para cálculo

# Validação de entrada
if quantidade_vendida < 0 or preco_venda < 0:
    print("Erro: Quantidade vendida e preço de venda devem ser valores positivos.")
else:
    vendas = quantidade_vendida * preco_venda  # Cálculo do total de vendas

    if quantidade_vendida > meta:
        print(f"Batemos a meta este mês! Vendemos {quantidade_vendida} unidades, totalizando R${vendas:.2f}.")
    else:
        print(f"Não atingimos a meta. Vendemos apenas {quantidade_vendida} unidades, totalizando R${vendas:.2f}.")

print("Fim do programa!")
