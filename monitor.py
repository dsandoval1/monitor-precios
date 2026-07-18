from config import PRODUCTOS
from providers import buscar_producto
from telegram import enviar_alerta


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

        except Exception as e:

            print(e)


if __name__ == "__main__":
    main()
