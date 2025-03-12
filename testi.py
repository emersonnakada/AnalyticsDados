import pandas as pd
import random

# Gerar dados fictícios para um estoque de mercado
produtos = ["Arroz", "Feijão", "Macarrão", "Açúcar", "Café", "Óleo", "Farinha", "Leite", "Pão", "Manteiga"]
categorias = ["Grãos", "Massas", "Açúcares", "Bebidas", "Laticínios"]

dados = {
    "ID": list(range(1, 11)),
    "Produto": produtos,
    "Categoria": [randwom.choice(categorias) for _ in range(10)],
    "Quantidade": [random.randint(10, 100) for _ in range(10)],
    "Preço Unitário (R$)": [round(random.uniform(2.5, 15.0), 2) for _ in range(10)]
}

# Criar um DataFrame
df = pd.DataFrame(dados)

# Salvar em um arquivo Excel
df.to_excel("estoque.xlsx", index=False)

print("Arquivo 'estoque.xlsx' criado com sucaesso!")
