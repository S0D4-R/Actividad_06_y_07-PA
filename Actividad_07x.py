"""
Ingresar una lista de n números reales y mostrar:
    Suma total
    Promedio
    Cantidad de positivos, negativos y ceros
    Cuántos son múltiplos de 3
Calcular el área y perímetro de un rectángulo (usar funciones separadas para cada cálculo)
Verificar si un número ingresado es primo o no
Calcular el promedio de n calificaciones, e indicar:
    Cuántas son mayores o iguales a 85
    Cuántas están en zona de riesgo (menor a 60)
Ingresar una lista de n números enteros y mostrar:
    El número mayor
    El número menor
Cuántos se repiten (frecuencia)
Simular una calculadora de operaciones básicas (suma, resta, multiplicación y división) entre dos números
Salir del programa
"""
from Demos.service.pipeTestServiceClient import testLargeMessage


def multifunction_n(maximum):
    try:
        nombaa_1 = 0
        three_y = 0
        zeroes = 0
        nombaa_neg = 0
        nombaa_pos = 0
        for number in range(maximum + 1):
            nombaa_x = int(input("Coloque un número: "))
            if nombaa_x < 0:
                nombaa_neg += 1
            elif nombaa_x == 0:
                zeroes += 1
            elif nombaa_x % 3:
                three_y += 1
            else:
                nombaa_pos += 1
            nombaa_1 += nombaa_x
        print(f"La suma de todos es: {nombaa_1}\n"
              f"El promedio es: {nombaa_1 / maximum}\n"
              f"La cantidad de números negativos es: {nombaa_neg}\n"
              f"La cantidad de ceros es: {zeroes}\n"
              f"La cantidad de múltiplo de tres es: {three_y}\n"
              f"La cantidad de números positivos es: {nombaa_pos}\n\n")
    except ValueError:
        print("Número no válido")


def rectarea():
    try:
        base = int(input("Coloque la base del triángulo: "))
        height = int(input("Coloque la altura del tirángulo: "))
        return print(f"El área del triángulo es: {(base * height)}\n\n")
    except ValueError:
        return print("Número no válido")

def even_odd(number_x):
    discriminante = number_x % 2
    if discriminante == 0:
        return print("Número es par")
    else:
        return print("Número no es par")
key = True


def max_min_calculataa():
    temp_list = []
    while True:
        temp_numba = int(input("Coloque el número que agregará: "))
        temp_list.append(temp_numba)
        conf = input("Quiere agregar uno más? Y/N")
        if conf.lower() == "n":
            break
    print(f"El número mínimo: {min(temp_list)}\nEl número máximo es: {max(temp_list)}")


def score_calc():
    loop = 0
    true_numba = 0
    while True:
        loop += 1
        temp_numba = int(input("Coloque la nota que agregará: "))
        true_numba +=temp_numba
        conf = input("Quiere agregar uno más? Y/N")
        if conf.lower() == "n":
            break
    print("El promedio general es: {}".format(true_numba/loop))


while key:
    menu_inpt = input("----------Bienvenido----------\n"
                      "\n1. Ingresar n números y mostrar"
                      "\n2. Calcular el área de un triángulo"
                      "\n3. Verificar si un número es par o impar"
                      "\n4. Calcular el promedio de n calificaciones"
                      "\n5. Ingresar n números y mostrar el mayor y el menor"
                      "\n6. Salir del programa\n\nSeleccione una opción: ")
    match menu_inpt:
        case "1":
            try:
                max = int(input("Coloque la cantidad de números que quiere colocar: "))
                multifunction_n(max)
            except ValueError:
                print("Ese no es un número")
        case "2":
            rectarea()
        case "3":
            try:
                eve_xxx = int(input("Coloque el número: "))
                even_odd(eve_xxx)
            except ValueError:
                print("Ese no es un número")
        case "4":
            score_calc()
        case "5":
            max_min_calculataa()
        case "6":
            print("Gracias por usar el programa")
            key = False
