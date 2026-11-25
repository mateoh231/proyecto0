import funciones
from base_datos import tabla

tabla()

while True:
    print("----- MENU -----")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Reporte de stock minimo")
    print("7. Salir")

    opcion = input("Ingrese una opcion: ")

    match opcion:

        case "1":
            funciones.agregar_producto()

        case "2":
            funciones.mostrar_todos_los_productos()

        case "3":
            funciones.buscar_producto_por_id()

        case "4":
            funciones.actualizar_producto_por_id()

        case "5":
            funciones.eliminar_producto()

        case "6":
            funciones.reportar_stock()

        case "7":
            print("saliendo del programa")
            break
        case _:
            print("La opcion ingresada es incorrecta")
            continue