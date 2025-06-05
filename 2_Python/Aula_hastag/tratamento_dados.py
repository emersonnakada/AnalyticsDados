import pandas   
import os

tabela = pandas.read_csv("cancelamentos.csv")

print(tabela)





















# Obtém o diretório atual
diretorio_atual = os.getcwd()

# Exibe o diretório
print(f"O código está rodando no diretório: {diretorio_atual}")