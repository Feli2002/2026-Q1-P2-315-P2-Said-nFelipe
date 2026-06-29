import json

def cargar_productos():
    with open("productos.json","r",encoding="utf-8") as productos_json:
        return json.load(productos_json)

def menu_supermercado():
    print("1. Listar productos")
    print("2. Agregar producto")
    print("3. Buscar producto por nombre")
    print("4. Modificar stock")
    print("5. Eliminar producto")
    print("6. Mostrar productos por categoría")
    print("7. Mostrar estadísticas")
    print("8. Exportar reporte CSV")
    print("9. Guardar y salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion

def listar_productos(productos):
    if len(productos) == 0:
        print("No hay productos cargados")
    else:
        print("Productos cargados")
        for producto in productos:
            id = producto["id"]
            nombre = producto["nombre"]
            print(f"ID: {id} | Nombre: {nombre}")
            categoria = producto["categoria"]
            print(f"Categoria: {categoria}")
            precio = producto["precio"]
            print(f"Precio: {precio}")
            stock = producto["stock"]
            print(f"Stock: {stock}")

def agregar_producto(productos):
    id = int(input("Ingrese id del producto: "))
    while id <= 0 :
        print("Por favor, ingrese un id válido")
        id = int(input("Ingrese id del producto: "))

    for producto in productos:
        if producto["id"] == id:
            print("El producto ya estaba cargado")
            stock_a_agregar = int(input("Ingrese stock a agregar: "))
            while stock_a_agregar <= 0:
                print("Por favor, ingrese un stock válido")
                stock_a_agregar = int(input("Ingrese stock a agregar: "))
            producto["stock"] += stock_a_agregar 
            print("Producto cargado correctamente") 
            return
        
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoria del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))

    nuevo_producto = {
        "id": id,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }

    productos.append(nuevo_producto)
    print("Producto cargado correctamente")

def buscar_producto_por_nombre(productos):
    nombre = input("Ingrese nombre del producto: ")

    for producto in productos:
        if producto["nombre"] == nombre:
            print("Producto encontrado")
            id = producto["id"]
            print(f"ID: {id}")
            categoria = producto["categoria"]
            print(f"Categoría: {categoria}")
            precio = producto["precio"]
            print(f"Precio: {precio}")
            stock = producto["stock"]
            print(f"Stock: {stock}")
            return
    print("Producto no encontrado")

def modificar_stock(productos):
    id = int(input("Ingrese id del producto a modificar stock: "))
    for producto in productos:
        if producto["id"] == id:
            stock_a_modificar = int(input("Ingrese stock a modificar: "))
            while (stock_a_modificar < 0) & (producto["stock"] == 0):
                print("Por favor, ingrese un stock válido")
                stock_a_modificar = int(input("Ingrese stock a modificar: "))
            producto["stock"] += stock_a_modificar
            print("Stock del producto modificado")
            return
    print("Producto no encontrado")

def eliminar_producto(productos):
    id = int(input("Ingrese id del producto a eliminar: "))
    for producto in productos:
        if producto["id"] == id:
            productos.remove(producto)
            print("Producto eliminado")
            return
    print("Producto no encontrado")

def mostrar_producto_por_categoria(productos):
    categoria = input("Ingrese una categoria: ")
    
    for producto in productos:
        if producto["categoria"] == categoria:
            id = producto["id"]
            print(f"ID: {id}")
            nombre = producto["nombre"]
            print(f"Nombre: {nombre}")
            precio = producto["precio"]
            print(f"Precio: {precio}")
            stock = producto["stock"]
            print(f"Stock: {stock}")
            return
    print("Categoria no disponible")


def mostrar_cant_productos(productos):
    cant_productos = len(productos)
    print(f"Cantidad de productos: {cant_productos}")

def mostrar_stock_total(productos):
     stock_total = 0
     for producto in productos:
        stock_total += producto["stock"]
     print(f"Stock total: {stock_total}")

def mostrar_producto_mas_caro(productos):
    producto_mas_caro = productos[0]["nombre"]
    precio_del_producto_mas_caro = productos[0]["precio"]
    for producto in productos:
        if producto["precio"] > precio_del_producto_mas_caro:
            producto_mas_caro = producto["nombre"]
            precio_del_producto_mas_caro = producto["precio"]
    print(f"Producto más caro: {producto_mas_caro}({precio_del_producto_mas_caro})")   

def mostrar_categorias(productos):
     categorias = {}
     for producto in productos:
        if producto["categoria"] in categorias.keys():
            categorias[producto["categoria"]] += 1
        else:
            nueva_categoria = producto["categoria"]
            categorias[nueva_categoria] = 1
     print("Productos por categoría")

     for categoria in categorias:
        print(f"{categoria}: {categorias[categoria]}")

def mostrar_estadisticas(productos):
    if len(productos) == 0:
        print("No hay productos cargados")
    else:
        mostrar_cant_productos(productos)

        mostrar_stock_total(productos)

        mostrar_producto_mas_caro(productos)
        
        mostrar_categorias(productos)

def exportar_reporte_csv(productos):
     columnas = ["id", "nombre", "categoria", "precio", "stock"]

     with open("reporte_productos.csv", "w", encoding="utf-8") as reporte_productos:
        
        encabezado = ",".join(columnas)
        reporte_productos.write(encabezado + "\n")
        print(encabezado)
        
        for producto in productos:
           
            valores = [
                str(producto["id"]),
                producto["nombre"],
                producto["categoria"],
                str(producto["precio"]), 
                str(producto["stock"]),
            ]

           
            linea = ",".join(valores)
               
            reporte_productos.write(linea + "\n")
            print(linea) 
        print("Reporte CSV exportado correctamente.")


def guardar_cambios(productos):
    with open("productos.json","w",encoding="utf-8") as productos_json:
        json.dump(productos,productos_json,indent=4,ensure_ascii=False)

def main(): 
    productos = cargar_productos()
    opcion = menu_supermercado()

    while opcion != 9:
        match opcion:
            case 1:
                listar_productos(productos)
            case 2:
                agregar_producto(productos)
            case 3:
                buscar_producto_por_nombre(productos)
            case 4:
                modificar_stock(productos)
            case 5:
                eliminar_producto(productos)
            case 6:
                mostrar_producto_por_categoria(productos)
            case 7:
                mostrar_estadisticas(productos)
            case 8:
                exportar_reporte_csv(productos)
            case _:
                print("Por favor, ingresa una opción válida(del 1 al 9)")
        opcion = menu_supermercado()
    guardar_cambios(productos)
    print("Saliste del supermercado")
main()
