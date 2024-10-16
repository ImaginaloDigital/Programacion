def operaciones(a,b):
    def suma():
        return(a + b)
    
    def resta():
        return(a - b)
    
    resultado_suma = suma() #se puede quitar si se usa como en el diccionario
    resultado_resta = resta()

    return resultado_suma,resultado_resta

suma_resultado, resta_resultado = operaciones(10,5)
print(f"La suma es: {suma_resultado} y la resta es: {resta_resultado}")

'''
____________________________________________________________________________________________________________
usando una lista
    lista_operaciones = [resultado_suma, resultado_resta]
    return lista_operaciones

operaciones_lista  = operaciones(10,5)
print(f"La suma es: {operaciones_lista[0]} y la resta es: {operaciones_lista[1]}")'''

'''
_____________________________________________________________________________________________________________
Usando un diccionario
dic_opciones = {
"suma" : suma()
"resta" : resta()
}

return dic_opciones

operaciones_dic = operaciones(10,5)

print(f"La suma es: {operaciones_dic["suma"]} y la resta es: {operaciones_dic["resta"]}")
'''