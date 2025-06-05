import os  
import google.generativeai 
from dotenv import load_dotenv

# Carregar o arquivo .env
load_dotenv()

# Configurar a chave da API
google.generativeai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Enviar uma mensagem diretamente ao modelo (sem usar ChatSession)
response = google.generativeai.generate_text(
    model="models/gemini-1.5-pro-latest",  # Substitua com o nome correto do modelo
    prompt="Olá, como você está hoje?"
)

# Imprimir a resposta
print(response)





# model_name = "models/gemini-1.5-pro-latest"
