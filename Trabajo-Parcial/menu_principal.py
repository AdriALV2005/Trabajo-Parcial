import os  # para limpiar la pantalla despues de usar alguna opcion del menu principal
from crear_producto import crear_producto
from listado_inventario import listado_inventario
from editar_producto import editar_producto as actualizar_producto
from eliminar_producto import eliminar_producto
from inventario_global import cargar_inventario, guardar_inventario


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
    cargar_inventario()
    while True:  # inicia el bucle hasta que le des opción 5
        limpiar()            # limpia la pantalla antes de dibujar el menú
        mostrar_menu()
        opcion = input("Opción (1-5): ").strip()

        if opcion == "1":
            limpiar()
            crear_producto()            # variable michael
            guardar_inventario()
            pausar()
        elif opcion == "2":
            limpiar()
            listado_inventario()        # variable sergio
            pausar()
        elif opcion == "3":
            limpiar()
            actualizar_producto()       # variable adri
            guardar_inventario()
            pausar()
        elif opcion == "4":
            limpiar()
            eliminar_producto()         # variable michael
            guardar_inventario()
            pausar()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            pausar()


if __name__ == "__main__":
    main()
