import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

mensaje = "✅ ¡Price Sentinel está funcionando!\n\nEsta es una prueba desde GitHub."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": mensaje
    }
)

print("Mensaje enviado.")
