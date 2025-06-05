import tkinter as tk

def executar_codigo():
    entrada = codigo_texto.get("1.0", tk.END)  # Obtém o código do jogador
    try:
        exec(entrada)
        resultado["text"] = "Código executado com sucesso!"
    except Exception as e:
        resultado["text"] = f"Erro: {e}"

# Cria janela do Tkinter
janela = tk.Tk()
janela.title("Function Master")

# Campo de texto para o código
codigo_texto = tk.Text(janela, height=10, width=40)
codigo_texto.pack()

# Botão para executar o código
botao = tk.Button(janela, text="Executar Código", command=executar_codigo)
botao.pack()

# Rótulo para mostrar o resultado
resultado = tk.Label(janela, text="")
resultado.pack()

def calcular_energia(casas):
    return casas * 100  # 100 é o consumo de energia por casa


janela.mainloop()
