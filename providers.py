import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/137.0 Safari/537.36"
    )
}


def buscar_producto(nombre):
    """
    Devuelve el mejor precio encontrado.

    De momento consulta SoloTodo.
    """

    url = "https://www.solotodo.cl/search"

    respuesta = requests.get(
        url,
        params={"search": nombre},
        headers=HEADERS,
        timeout=15,
    )

    respuesta.raise_for_status()

    soup = BeautifulSoup(respuesta.text, "lxml")

    enlace = soup.select_one("a[href*='/products/']")

    if enlace is None:
        raise Exception("No se encontró el producto.")

    return {
        "producto": nombre,
        "precio": 999999999,
        "tienda": "SoloTodo",
        "url": "https://www.solotodo.cl" + enlace["href"],
    }
