inventario = {}

def eliminar_producto():
    print("--- Eliminar producto del inventario ---")
    nombre = input("Nombre del producto a eliminar: ").strip().title()

    if nombre in inventario:
        confirmacion = input(f"¿Desea eliminar '{nombre}' del inventario? (s/n): ").strip().lower()
        if confirmacion == "s":
            del inventario[nombre]
            print(f"Producto '{nombre}' eliminado correctamente.")
        else:
            print("Operación cancelada. El producto no fue eliminado.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")
eliminar_producto()
