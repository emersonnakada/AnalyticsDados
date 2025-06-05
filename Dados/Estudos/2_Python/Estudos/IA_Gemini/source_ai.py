import os  
import google.generativeai as genai
from dotenv import load_dotenv

# Carregar o arquivo .env
load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

chat_session = model.start_chat(
   history=[
         {
             "role": "user",
             "parts": [genai.upload_file("2.png", mime_type="image/png")],

         }])



