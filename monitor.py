from config import PRODUCTOS
from providers import buscar_producto
from telegram import enviar_alerta

print("VERSION NUEVA DEL MONITOR")


def main():

    for producto in PRODUCTOS:

        try:

            resultado = buscar_producto(producto["busqueda"])

            print("RESULTADO DEL BUSCADOR:")
            print(resultado)

            if resultado["precio"] <= producto["precio_objetivo"]:

                enviar_alerta(
                    resultado["producto"],
                    resultado["precio"],
                    resultado["tienda"],
                    resultado["url"],
                )

            else:
                print(
                    f'No hay oferta: {resultado["precio"]} '
                    f'> objetivo {producto["precio_objetivo"]}'
                )

        except Exception as e:

            print("ERROR:")
            print(e)


if __name__ == "__main__":
    main()
