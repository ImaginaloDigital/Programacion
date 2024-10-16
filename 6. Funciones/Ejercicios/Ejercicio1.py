'''Crear calculadora con un diccionario'''

def suma(x,y):
    return x + y

def resta(x,y):
    return x - y

def multiplicar(x,y):
    return x * y

def dividir(x,y):
    if y != 0:
        return x/y
    else:
        return "Error: Division por cero"

def sumar(x,y):
    return x + y

def exponente(x,y):
    return x**y     #X elevado a la potencia de Y

def menu():
    print(" 1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. División \n 5. Exponente \n 6. Salir")

#Diccionario de operaciones
operaciones = {
    1: suma,
    2: resta,
    3: multiplicar,
    4: dividir,
    5: exponente,
}

#Programa principal
while True:
    print( " ______________________ \n Calculadora:")
    menu() #muestra el menu
    opcion = int(input("Seleccione una operación: "))

    if opcion in operaciones:
        numero1 = float(input("Ingrese el primero número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        resultado = operaciones[opcion](numero1,numero2)
        print("El resultado es: ", resultado)
        #print( "\n")
    elif opcion == 6:
        print("Saliendo...")
        break
    else:
        print("Error: Opción no valida....")
