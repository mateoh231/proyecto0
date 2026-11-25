import funciones_sql

def agregar_producto():
    # Se ingresa el nombre
    nombre = input("Ingresa el nombre del producto: ").lower().strip()
    descripcion = input("Ingrese la descripcion del producto: ").lower().strip()
    categoria = input("Ingrese la categoria del producto: ").lower().strip()

    while nombre == "":
        print("El nombre no puede estar vacio")
        nombre = input("Ingresa el nombre del producto: ").lower().strip()

    while descripcion == "":
        print("La descripcion del producto no puede quedar vacia")
        descripcion = input("Ingrese la descripcion del producto: ").lower().strip()


    while categoria == "":
        print("La categoria no puede estar vacia")
        categoria = input("Ingrese la categoria del producto: ").lower().strip()

    while True:
        try:
            cantidad = int(input("Ingrese el stock del producto: "))

            if cantidad <= 0:
                print("El valor ingresado no puede ser negativo")
                continue
            else:
                break
        except ValueError:
            print("El valor ingresado debe ser un numero entero")

    while True:
        try:
            precio = int(input("Ingrese el precio del producto: "))

            if precio <= 0:
                print("El precio ingresado debe ser mayor a 0")
                continue
            else:
                break
        except ValueError:
            print("Error: debe ingresar un numero entero")

    funciones_sql.registrar_producto(nombre,descripcion,categoria,cantidad,precio)

    print(f"El producto {nombre} ha sido agregado correctamente.")

def obtener_productos(lista):
    if len(lista) == 0:
        print("No hay productos.")
    else:
        print("----- PRODUCTOS -----")

        for indice in range(len(lista)):
            producto = lista[indice]

            print(f"ID: {producto[0]}. Nombre: {producto[1]}")
            print(f"   Descripcion: {producto[2]}")
            print(f"   Categoria: {producto[3]}")
            print(f"   Cantidad: {producto[4]}")
            print(f"   Precio: {producto[5]}")
            print("\n")


def mostrar_todos_los_productos():
    lista_productos= funciones_sql.obtener_datos()
    obtener_productos(lista_productos)

def buscar_producto_por_id():
    try: 
        id = input("Ingrese el id del producto: ")
        producto = funciones_sql.obtener_producto_por_id(id)

        if producto:
            obtener_productos([producto])
            return producto
        else: 
            print("El producto no existe.")
            return None
    except ValueError:
        print("Error: el id debe ser un numero entero")

def actualizar_producto_por_id():
    producto = buscar_producto_por_id()

    if producto:
        print("Campos para actualizar:")
        print("1. Actualizar nombre")
        print("2. Actualizar descripcion")
        print("3. Actualizar categoria")
        print("4. Actualizar cantidad")
        print("5. Actualizar precio")

        opcion = int(input("Seleccione la opcion que quiere cambiar: "))

        match opcion:
            case 1:
                nombre = input("Ingrese el nuevo nombre: ").lower().strip()
                while nombre == "":
                    print("El nombre no puede quedar vacio.")
                    nombre = input("Ingrese el nuevo nombre: ").lower().strip()

                funciones_sql.actualizar_nombre(producto[0],nombre)
                print("El nombre del producto ha sido actualizado correctamente.")
            case 2:
                descripcion = input("Ingrese la descripcion del producto: ").lower().strip()

                funciones_sql.actualizar_descripcion(producto[0],descripcion)
                print("La descripcion ha sido actualizada correctamente.")
            case 3:
                categoria = input("Ingresa la categoria del producto: ").lower().strip()
                while categoria == "":
                    print("La categoria no puede quedar vacia.")
                    categoria = input("Ingrese el categoria del producto: ").lower().strip()

                funciones_sql.actualizar_categoria(producto[0],categoria)
                print("La categoria ha sido actualizada correctamente.")
            case 4:
                while True:
                    try:
                        cantidad = int(input("Ingresa el stock del producto: "))

                        if cantidad < 0:
                            print("El stock no puede ser negativo.")
                            continue
                        else:
                            break
                    except ValueError:
                        print("El valor debe ser un numero entero")

                funciones_sql.actualizar_cantidad(producto[0],cantidad)
                print("La cantidad del stock ha sido actualizada correctamente.")
            case 5:
                while True:
                    try:
                        precio = int(input("Ingrese el precio del producto: "))

                        if precio < 0:
                            print("El precio no puede ser negativo.")
                            continue

                        break
                    except ValueError:
                        print("El precio debe ser un numero entero")

                funciones_sql.actualizar_precio(producto[0],precio)
                print("El precio ha sido actualizado correctamente.")
            case _:
                print("La opcion ingresada no es valida.")

def eliminar_producto():
    try: 
        id_del_producto = int(input("Ingrese el id del producto: "))

        if id_del_producto <= 0:
            print("El id del producto debe ser un numero entero positivo")
            return

        producto = funciones_sql.obtener_producto_por_id(id_del_producto)

        if not producto:
            print("El producto ingresado no existe")
            return

        confirmacion = input(f"Estas seguro de eliminar {producto}? y/n: ").lower().strip()

        if confirmacion != "y":
            print("Eliminacion cancelada")
            return

        if funciones_sql.eliminar_producto(id_del_producto):
            print(f"El producto {producto[1]} ha sido eliminado")
        else:
            print("El producto no pudo eliminarse")
    except Exception as error:
        print("El id debe ser un numero positivo")

def reportar_stock():
    while True:
        try:
            limite = int(input("Ingrese el limite de la cantidad: "))

            if limite < 0:
                print("El limite no puede ser negativo")
                continue

            break
        except ValueError:
            print("Error: el numero debe ser entero")

    productos = funciones_sql.productos_bajo_stock(limite)

    if not productos:
        print(f"No hay productos con la cantidad inferior o igual a {limite}.")
    else:
        print(f"Reporte de stock (cantidad <= {limite})")
        obtener_productos(productos)
        