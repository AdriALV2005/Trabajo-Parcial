# Inventario de productos (nombre: [cantidad, precio])
inventario = {
    "Manzanas": [10, 1.5],
    "Peras": [5, 2.0],
    "Plátanos": [8, 1.2],
    "Naranjas": [12, 1.8]
}


def READ():
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
    READ()
READ()
