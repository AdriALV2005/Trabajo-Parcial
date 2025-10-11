# Inventario de productos (nombre: [cantidad, precio])
inventario = {}

# Función para mostrar el inventario


def listado_inventario():
    print("=== Inventario ===")
    valor_total = 0

    for producto, datos in inventario.items():
        cantidad = datos[0]
        precio = datos[1]
        subtotal = cantidad * precio
        valor_total += subtotal
        print(
            f"{producto}: Cantidad = {cantidad}, Precio = ${precio:.2f}, Subtotal = ${subtotal:.2f}")

    print("==================")
    print(f"Valor total del inventario: ${valor_total:.2f}")


# Ejecutar la función
if __name__ == "__main__":
    listado_inventario()
