'''
Diccionarios
Es una coleccion desordenada de pares clave-valor, donde cada clave es unica y estar asociada a un valor
Se utiliza para representar relaciones de datos, como una tabla.

Caracteristicas:

* Los elementos sse almacenan como pares clave-valor.
* Permite adicionar listas dentro del valor de una clave.
* Son mutables
* Las claves son unicas
* Los valores se pueden repetir
* Las claves deben ser inmutables
'''

#Definicion de un diccionario
mi_diccionario = {
    "nombre" :  "Ian Andres",
    "Edad" :    27,
    "Ciudad" :  "Palmira",
    "idiomas" : ["ingles", "español", "frances"], #Lista en una clave
    "grupoSanguineo" : None
}

#imprimir solo un valor de la lista idiomas
print(mi_diccionario["idiomas"][2]) #imprime el idioma frances

#Aceder a un valor mediante su clave
print(mi_diccionario["nombre"]) #Salida: Ian Andres

#acceder a todos los valores
print(mi_diccionario)

#modificar un valor
mi_diccionario["edad"] = 28
print(mi_diccionario)

#Agregar un nuevo par de clave-valor
mi_diccionario["Profesion"] = "Administrador"
print(mi_diccionario)

#Eliminar un par de clave-valor
del mi_diccionario["Ciudad"]
print(mi_diccionario)
'''
Operadores
* del : elimina un par de clave-valor

'''