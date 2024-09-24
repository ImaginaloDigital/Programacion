temperatura = float(input("Ingrese la temperatura actual: "))
llueve = input("¿Esta lloviendo? (Si/No): ").lower()

if temperatura < 15:
    if llueve == 'SI':
        print("Lleva abrigo y paraguas")
    else:
        print("Usa abrigo")
elif 15 <= temperatura <= 25:
    if llueve == 'SI':
        print("Lleva un paraguas")
    else:
        print("Usa ropa ligera")
else:
    print("Usa ropa fresca")