import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


def enviar_alerta(producto, precio, tienda, url):
    mensaje = (
        f"🚨 ¡Oferta encontrada!\n\n"
        f"🎮 {producto}\n"
        f"💰 ${precio:,}\n"
        f"🏪 {tienda}\n\n"
        f"🔗 {url}"
    )

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": mensaje,
        },
    )
