def cargar_productos():
    
    # Carga por teclado los nombres y precios de 5 productos en una lista de tuplas
    
    productos = []

    for i in range(5):
        nombre = input(f"Ingrese el nombre del producto {i+1}: ")
        precio = float(input(f"Ingrese el precio del producto {i+1}: "))
        productos.append((nombre, precio))

    return productos

def listar_productos(productos):
    
    # Listo los productos y sus precios.
    
    print("Productos y precios:")
    for nombre, precio in productos:
        print(f"{nombre}: ${precio}")

def imprimir_producto(productos, min_precio, max_precio):
    
    # Imprimo los productos con precios entre el precio mínimo y el precio máximo
    
    print(f"\nProductos con precios entre {min_precio} y {max_precio}:")
    for nombre, precio in productos:
        if min_precio <= precio <= max_precio:
            print(f"{nombre}: ${precio}")

# Ejemplo
productos = cargar_productos()
listar_productos(productos)
imprimir_producto(productos, 10, 15)
