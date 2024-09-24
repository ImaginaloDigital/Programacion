'''
    Aries: del 21 de marzo al 19 de abril
    Tauro: del 20 de abril al 20 de mayo
    Géminis: del 21 de mayo al 20 de junio
    Cáncer: del 21 de junio al 22 de julio
    Leo: del 23 de julio al 22 de agosto
    Virgo: del 23 de agosto al 22 de septiembre
    Libra: del 23 de septiembre al 22 de octubre
    Escorpio: del 23 de octubre al 21 de noviembre
    Sagitario: del 22 de noviembre al 21 de diciembre
    Capricornio: del 22 de diciembre al 19 de enero
    Acuario: del 20 de enero al 18 de febrero
    Piscis: del 19 de febrero al 20 de marzo

    '''

dia = int(input("Ingrese dia de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))

if not(1 <= mes <= 12 and 1 <= dia <= 31) :
    print("Fecha no valida.")
elif (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
    print("Aries")
elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
    print("Tauro")
elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
    print("Géminis")
elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
    print("Cáncer")
elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
    print("Leo")
elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
    print("Virgo")
elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
    print("Libra")
elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
    print("Escorpio")
elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
    print("Sagitario")
elif (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
    print("Capricornio")
elif (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
    print("Acuario")
elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
    print("Piscis")