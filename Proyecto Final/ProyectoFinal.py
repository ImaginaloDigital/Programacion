import os


#Lista de productos e invetario disponible

productos=[
    {"nombre" : "Anillo de diamante", "precio" : 10000, "cantidad" : 5},
    {"nombre" : "Anillo de Curso", "precio" : 4000, "cantidad" : 8},
    {"nombre" : "Anillo de esmeralda", "precio" : 20000, "cantidad" : 12},
    {"nombre" : "Anillo de oro", "precio" : 5000, "cantidad" : 7}
]

carrito = []

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls') #limpiar terminal en windows
    else:
        os.system('clear') #limpiar terminal en linux o mac


def mostrar_productos():
    limpiar_pantalla()
    print("------------------- Menú de productos -----------------------")
    for i, producto in enumerate(productos):
        print(f"{i+1}.{producto['nombre']} - precio: ${producto['precio']} - cantidad: {producto['cantidad']}")


def agregar_carrito():
    limpiar_pantalla()
    mostrar_productos()
    try:
        opcion = int(input("Dijite la opción de producto que desee agregar: "))
        if 1<=opcion<=len(productos):
            cantidad = int(input("Digite la cantidad de productos a comprar: "))
            producto = productos[opcion-1]
            if cantidad > producto["cantidad"]:
                print("No existe la cantidad requerida del producto en inventario")
            else:
                productos[opcion-1]['cantidad'] -= cantidad
                carrito.append({"nombre":producto["nombre"], "precio":producto['precio'], "cantidad":cantidad})
                print(carrito)
                print(f"Felicidades añadiste: {cantidad} de {producto['nombre']} de manera exitosa")
    except Exception as e:
        print("Se ha producido un error", e)

def mostrar_carrito():
    limpiar_pantalla()
    if carrito:
        print("Carrito de compras")
        for i, item in enumerate(carrito, 1):
            print(f"{i}.producto: {item['nombre']} - precio: ${item['precio']} - cantidad: {item['cantidad']}")
    else:
        print("Carrito vacio")


def calcular_total():
    total = sum(item["precio"] * item["cantidad"] for item in carrito)
    print(f"El total a pagar es: ${total}")

def finalizar_compra():
    limpiar_pantalla()
    mostrar_carrito()
    if carrito:
        calcular_total()
        confirmar = input("¿Desea finalizar su compra? (si/no): ")
        if confirmar.lower() == "si" :
            carrito.clear()
            print("La compra fue realizada exitosamente")
        else:
            print("Compra cancelada")
    else:
        print("No hay productos en el carrito")

def main():

    while True:
        limpiar_pantalla()
        print("------------------- MENÚ -------------------------")
        print(" 1. Mostrar productos disponibles \n 2. Añadir productos al carrito \n 3. Mostrar carrito \n 4. Finalizar la compra \n 5. Salir de la compra")

        try:
            opciones={
                1:mostrar_productos,
                2:agregar_carrito,
                3:mostrar_carrito,
                4:finalizar_compra
            }
            seleccion = int(input("Digite la opción deseada: "))
            if seleccion in opciones:
                opciones[seleccion]()
                input("presione enter para continuar ")
            elif seleccion == 5:
                break
            
        except ValueError:
            print("La entrada es invalida, por favor digite un número")
            input("Presione enter para continuar... ")

        except Exception:
            print("Se ha presentado un error")
            input("Precione enter para continuar... ")

main()
