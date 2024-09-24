edad = 15
tiene_licencia = True

if edad >= 18:
    print("Eres mayor de edad.")
    if tiene_licencia:
        print("Tienes licencia de conduccion, puedes manejar")
    else:
        print("No tienes licencia de conduccion, no puedes manejar.")
else:
    print("Eres menor de edad, no puedes manejar.")