inventario = {}

def crear_producto():
    print("----- Registrar nuevo producto -----")
    nombre = input("Nombre del producto: ").strip().title()

    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe en el inventario.")
        return

    while True:
        try:
            cantidad = int(input("Cantidad disponible: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Ingrese un número entero válido para la cantidad.")

    while True:
        try:
            precio = float(input("Precio unitario (S/): "))
            if precio < 0:
                print("El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Ingrese un valor numérico válido para el precio.")

    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    print(f"Producto '{nombre}' agregado correctamente.")
crear_producto()
