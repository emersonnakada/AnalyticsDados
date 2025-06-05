import pandas as pd
import random
import faker

# Criando a instância do Faker
fake = faker.Faker()

# Número de dados a serem criados
n = 45000

# Gerando a tabela de clientes
clientes = pd.DataFrame({
    'customer_id': range(1, n + 1),
    'nome': [fake.name() for _ in range(n)],
    'email': [fake.email() for _ in range(n)],
    'telefone': [fake.phone_number() for _ in range(n)],
    'idade': [random.randint(18, 70) for _ in range(n)],
})

# # Gerando a tabela de produtos
produtos = pd.DataFrame({
    'product_id': range(1, n + 1),
    'nome_do_produto': [fake.word() for _ in range(n)],
    'categoria': [random.choice(['Eletrônicos', 'Roupas', 'Livros', 'Móveis']) for _ in range(n)],
    'preço': [round(random.uniform(10.0, 1000.0), 2) for _ in range(n)],
    'estoque': [random.randint(0, 100) for _ in range(n)]
})

# # Gerando a tabela de pedidos
pedidos = pd.DataFrame({
    'order_id': range(1, n + 1),
    'customer_id': [random.randint(1, n) for _ in range(n)],
    'product_id': [random.randint(1, n) for _ in range(n)],
    'quantidade': [random.randint(1, 5) for _ in range(n)],
    'preço_total': [round(random.uniform(20.0, 2000.0), 2) for _ in range(n)],
    'data_pedido': [fake.date_this_year() for _ in range(n)],
    'status': [random.choice(['enviado', 'pendente', 'entregue', 'cancelado']) for _ in range(n)]
})

# # Gerando a tabela de pagamentos
pagamentos = pd.DataFrame({
    'payment_id': range(1, n + 1),
    'order_id': [random.randint(1, n) for _ in range(n)],
    'tipo_pagamento': [random.choice(['cartao_credito', 'boleto', 'pix', 'paypal']) for _ in range(n)],
    'data_pagamento': [fake.date_this_year() for _ in range(n)],
    'valor_pago': [round(random.uniform(20.0, 2000.0), 2) for _ in range(n)]
})

# Salvando as tabelas em arquivos CSV para posterior uso
clientes_path = 'F:/1 - Estudos Emerson/Estudos/Clientes Join/clientes.csv'
produtos_path = 'F:/1 - Estudos Emerson/Estudos/Clientes Join/produtos.csv'
pedidos_path = 'F:/1 - Estudos Emerson/Estudos/Clientes Join/pedidos.csv'
pagamentos_path = 'F:/1 - Estudos Emerson/Estudos/Clientes Join/pagamentos.csv'

clientes.to_csv(clientes_path, index=False)
produtos.to_csv(produtos_path, index=False)
pedidos.to_csv(pedidos_path, index=False)
pagamentos.to_csv(pagamentos_path, index=False)

clientes_path, produtos_path, pedidos_path, pagamentos_path
