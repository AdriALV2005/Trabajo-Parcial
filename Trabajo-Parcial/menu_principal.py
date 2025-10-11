import os  # para limpiar la pantalla despues de usar alguna opcion del menu principal


def limpiar():
    # Windows es cls ---- Linux/Mac es clear
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1) Agregar producto")
    print("2) Mostrar inventario")
    print("3) Actualizar producto")
    print("4) Eliminar producto")
    print("5) Salir")


def pausar():
    input("\nPresiona Enter para volver al menú...")


def main():
    while True:  # inicia el bucle hasta que le des opción 5
        limpiar()            # limpia la pantalla antes de dibujar el menú
        mostrar_menu()
        opcion = input("Opción (1-5): ").strip()

        if opcion == "1":
            crear_producto()            # variable michael
            pausar()
        elif opcion == "2":
            listado_inventario()        # variable sergio
            pausar()
        elif opcion == "3":
            actualizar_producto()       # variable adri
            pausar()
        elif opcion == "4":
            eliminar_producto()         # variable michael
            pausar()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            pausar()


if __name__ == "__main__":
    main()
