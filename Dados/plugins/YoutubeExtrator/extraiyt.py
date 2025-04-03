from dotenv import load_dotenv
import os
from pytubefix import YouTube


load_dotenv("Dados/plugins/YoutubeExtrator/files/.env")

url = os.getenv("URL")

if not url:
    print("Erro: A variável URL não foi carregada corretamente.")
else:
    print(f"URL carregada: {url}")

# URL=https://www.youtube.com/watch?v=7QU1nvuxaMA

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()

stream.download("Dados/plugins/YoutubeExtrator/files")

print("Download concluido")
