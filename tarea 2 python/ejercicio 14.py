def cargar():
    productos = {}
    continua = "s"
    while continua == "s":
        codigo = int(input("Ingrese el codigo del producto: "))
        descripcion = input("Ingrese la descripcion: ")
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock actual: "))
        productos[codigo] = (descripcion, precio, stock)
        continua = input("¿Desea cargar otro producto [s/n]? ").lower()
    return productos


def imprimir(productos):
    print("Listado completo de productos:")
    for codigo in productos:
        print(f"Código: {codigo}, Descripción: {productos[codigo][0]}, Precio: {productos[codigo][1]}, Stock: {productos[codigo][2]}")


def consulta(productos):
    codigo = int(input("Ingrese el código del producto a consultar: "))
    if codigo in productos:
        print(f"Descripción: {productos[codigo][0]}, Precio: {productos[codigo][1]}, Stock: {productos[codigo][2]}")
    else:
        print("El código no existe en el inventario.")


def listado_stock_cero(productos):
    print("Listado de artículos con stock en cero:")
    for codigo in productos:
        if productos[codigo][2] == 0:
            print(f"Código: {codigo}, Descripción: {productos[codigo][0]}, Precio: {productos[codigo][1]}, Stock: {productos[codigo][2]}")


# Bloque principal
productos = cargar()
imprimir(productos)
consulta(productos)
listado_stock_cero(productos)
