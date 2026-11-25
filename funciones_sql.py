from base_datos import conectar

def registrar_producto(nombre,descripcion,categoria,cantidad,precio):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO productos (nombre,descripcion,categoria,cantidad,precio)
            VALUES (?,?,?,?,?)
        """,(nombre,descripcion,categoria,cantidad,precio))

        conexion.commit()

    except Exception as error:
        print(f"Error al registrar el producto: {error}")
    finally:
        conexion.close()

def obtener_producto_por_id(id_producto):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM productos WHERE id = ?",(id_producto,))
        return cursor.fetchone()
    except Exception as error:
        print(f"Error al buscar el producto: {error}")
        return None
    finally:
        conexion.close() 

def actualizar_nombre(id_producto,nombre_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos
            SET nombre = ?
            WHERE id = ?
        """,(nombre_nuevo,id_producto))

        conexion.commit()
    except Exception as error:
        print(f"Error al actualizar el nombre {error}")
    finally:
        conexion.close()

def actualizar_descripcion(id_producto,descripcion_nueva):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos
            SET descripcion = ?
            WHERE id = ?
        """,(descripcion_nueva,id_producto))

        conexion.commit()
    except Exception as error:
        print(f"Error al actualizar la descripcion del producto {error}")
    finally:
        conexion.close()

def actualizar_categoria(id_producto,nueva_categoria):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos
            SET categoria = ?
            WHERE id = ?
        """,(nueva_categoria,id_producto))

        conexion.commit()
    except Exception as error:
        print(f"Error al actualizar la categoria del producto {error}")
    finally:
        conexion.close()

def actualizar_cantidad(id_producto,cantidad_nueva):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos
            SET cantidad = ?
            WHERE id = ?
        """,(cantidad_nueva,id_producto))

        conexion.commit()
    except Exception as error:
        print(f"Error al actualizar la cantidad del producto {error}")
    finally:
        conexion.close()

def actualizar_precio(id_producto,nuevo_precio):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos
            SET precio = ?
            WHERE id = ?
        """,(nuevo_precio,id_producto))

        conexion.commit()
    except Exception as error:
        print(f"Error al actualizar el precio del producto {error}")
    finally:
        conexion.close()

def obtener_datos():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * from productos")
        return cursor.fetchall()
    except Exception as error:
        print(f"Error al obtener los datos {error}")
        return []
    finally:
        conexion.close()

def eliminar_producto(id_producto):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("DELETE from productos WHERE id = ?",(id_producto,))
        
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as error:
        print(f"Error al eliminar el producto {error}")
        return False
    finally:
        conexion.close()

def productos_bajo_stock(limite):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT * FROM productos
            WHERE cantidad <= ?
            ORDER BY cantidad ASC, id ASC
        """,(limite,))
        return cursor.fetchall()
    except Exception as error:
        print(f"Error al generar el reporte del stock {error}")
        return []
    finally:
        conexion.close()