salario = float(input("Ingrese su salario anual: "))

if salario > 50000:
    if salario> 100000:
        print("El impuesto es del 30%: ", (salario*0.3))
    else:
        print("El impuesto es del 20%: ", (salario*0.2))
else:
    print("No paga impuesto")