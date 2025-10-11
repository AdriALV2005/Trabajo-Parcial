from inventario_global import inventario

# Función para mostrar el inventario


def listado_inventario():
    print("=== Inventario ===")
    valor_total = 0

    for producto, datos in inventario.items():
        cantidad = datos["cantidad"]
        precio = datos["precio"]
        subtotal = cantidad * precio
        valor_total += subtotal
        print(
            f"{producto}: Cantidad = {cantidad}, Precio = S/ {precio:.2f}, Subtotal = S/ {subtotal:.2f}")

    print("==================")
    print(f"Valor total del inventario: ${valor_total:.2f}")


# Ejecutar la función
if __name__ == "__main__":
    listado_inventario()
