'''Escribe un programa que pida una calificacion numerica (0-100) y determine si el estudiante aprueba o no 
(60 o más es aprobado)'''

import math

calificacion = float(input("Ingrese su calificacion: "))

calificacion = round(calificacion) #"Redodea ya sea hacia abajo o hacia arriba"
#calificacion = math.floor(calificacion) "Redondea hacia abajo"
#calificacion = math.ceil(calificacion) "redondea hacia arriba"

if calificacion >= 60 and calificacion <= 100:
    print("El estudiante aprobo.")
elif calificacion >= 0 and calificacion <= 60:
    print("El estudiante reprobo.")
else:
    print("La Calificacion no es valida.")

