from config import PRODUCTOS
from providers import buscar_producto
from telegram import enviar_alerta


def main():

    for producto in PRODUCTOS:

        resultado = buscar_producto(producto["busqueda"])

        if resultado["precio"] <= producto["precio_objetivo"]:

            enviar_alerta(
                resultado["producto"],
                resultado["precio"],
                resultado["tienda"],
                resultado["url"],
            )

        else:

            print(
                f'{resultado["producto"]}: '
                f'${resultado["precio"]:,} '
                f'(objetivo ${producto["precio_objetivo"]:,})'
            )


if __name__ == "__main__":
    main()
