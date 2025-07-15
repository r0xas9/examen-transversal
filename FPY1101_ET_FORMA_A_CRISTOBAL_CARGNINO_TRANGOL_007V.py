productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
    'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

def stock_marca(marca):
    total = 0
    for modelo in productos:
        if productos[modelo][0].lower() == marca.lower():
            if modelo in stock:
                total += stock[modelo][1]
    print (f"El stock de {marca} es de: {total}.")
    
#stock_marca("hp")
    
                

def busqueda_precio(precio_min,precio_max):
    encontrado = []
    for modelo in productos:
        if modelo in stock and stock[modelo][0] > 0:
            cantidad = stock[modelo][0]
            precio = int(stock[modelo][1])
            if precio_min <= precio <= precio_max and cantidad > 0:
                encontrado.append(productos[modelo])
    
    if encontrado:
        for productos in encontrado:
            print(productos)
        print (f"Los notebooks entre los precios consultas son: {encontrado} ")
    else:
        print ("No hay notebooks en ese rango de precios.")


def actualizar_precio(modelo,p):
    if modelo in stock:
        stock[modelo][1] = p
        return True
    else:
        return False
        

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print ("Debe ingresar valores enteros.")
    


def main():
    while True:
        print ("\n***MENU PRINCIPAL***")
        print ("1.- Stock marca.")
        print ("2.- Busqueda por precio.")
        print ("3.- Actualizar precio.")
        print ("4.- Salir.")

        op = (input("Ingrese una opcion: "))

        if op == "1":
            consultar = input("Ingrese marca a consultar: ")
            stock_marca(consultar)
        elif op == "2":
            precio_min = pedir_entero("Ingrese precio minimo: ")
            precio_max = pedir_entero("Ingrese precio maximo: ")
            busqueda_precio(precio_min,precio_max)
        elif op == "3":
            actualizar = input("Ingrese modelo a actualizar: ")
            actualizar_precio(actualizar)
        elif op == "4":
            print("Programa finalizado.")
            break
        else:
            print ("Debe seleccionar una opcion valida!!")


main()
            








