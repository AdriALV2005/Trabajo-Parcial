inventario = {}


def editar_producto():
    print("----- Actualizar producto -----")
    nombre = input("Nombre del producto a actualizar: ").strip().title()

    if nombre not in inventario:
        print(f"El producto '{nombre}' no existe en el inventario.")
        return

    print(f"\nProducto actual: {nombre}")
    print(f"Cantidad: {inventario[nombre]['cantidad']}")
    print(f"Precio: S/ {inventario[nombre]['precio']:.2f}")

    print("\n¿Qué desea actualizar?")
    print("1) Cantidad")
    print("2) Precio")
    print("3) Ambos")
    opcion = input("Opción (1-3): ").strip()

    if opcion == "1":
        while True:
            try:
                nueva_cantidad = int(input("Nueva cantidad: "))
                if nueva_cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue
                inventario[nombre]['cantidad'] = nueva_cantidad
                print(f"Cantidad actualizada correctamente.")
                break
            except ValueError:
                print("Ingrese un número entero válido.")

    elif opcion == "2":
        while True:
            try:
                nuevo_precio = float(input("Nuevo precio (S/): "))
                if nuevo_precio < 0:
                    print("El precio no puede ser negativo.")
                    continue
                inventario[nombre]['precio'] = nuevo_precio
                print(f"Precio actualizado correctamente.")
                break
            except ValueError:
                print("Ingrese un valor numérico válido.")

    elif opcion == "3":
        while True:
            try:
                nueva_cantidad = int(input("Nueva cantidad: "))
                if nueva_cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue
                break
            except ValueError:
                print("Ingrese un número entero válido.")

        while True:
            try:
                nuevo_precio = float(input("Nuevo precio (S/): "))
                if nuevo_precio < 0:
                    print("El precio no puede ser negativo.")
                    continue
                break
            except ValueError:
                print("Ingrese un valor numérico válido.")

        inventario[nombre]['cantidad'] = nueva_cantidad
        inventario[nombre]['precio'] = nuevo_precio
        print(f"Producto '{nombre}' actualizado correctamente.")

    else:
        print("Opción inválida.")


editar_producto()