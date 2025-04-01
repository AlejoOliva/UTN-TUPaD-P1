#imports
from statistics import mode, median, mean
import random

#Actividad 1
edad = int(input("ingrese su edad: "))

if edad <= 17:
    print("el usuario es menor de edad")
else:
    print("el usuario es mayor de edad")

#Actividad 2
nota = int(input("ingrese su nota: "))

if 6 <= nota:
    print("Aprobado")
else:
    print("desaprobado")

#Actividad 3
num = int(input("Ingrese un numero par: "))

if num % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor,ingrese un numero par")

#Actividad 4
EDAD = int(input("ingrese su edad: "))

if EDAD < 12:
    print("El usuario pertenece a la categoria niño/niña")
elif 12 <= EDAD and EDAD < 18:
    print("El usuario pertenece a la categoria adolescente")
elif 18 <= EDAD and EDAD < 30:
    print("El usuario pertence a la categoria adulto/a joven")
else:
    print("El usuario pertence a la categoria adulto/a")

#Actividad 5
contraseña = input("Introduzca una contraseña de entre 8 y 14 caracteres: ")

if len(contraseña) <= 14 and 8 <= len(contraseña):
    print("Ha ingresado una contraseña correcta")
else:
    print("Ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6
numeros_aleatorios = (random.randint(1, 100) for i in range(50))
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if mediana < media and moda < mediana:
    print("Hay sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo o a la izquierda")
elif media == moda == mediana:
    ("sin sesgo")

#Actividad 7
frase = input("Ingrese una palabra o frase: ")

if frase.endswith("a" or "e" or "i" or "o" or "u"):
    print(frase, "!")
else:
    print(frase)

#Actividad 8
nombre = input("ingrese su nombre: ")
print("Si quiere su nombre en mayusculas ingrese 1")
print("Si quiere su nombre en minusculas ingrese 2")
print("Si quiere su nombre con la primera letra mayuscula ingrese 3")
opcion = int(input("Ingrese su opcion: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("opcion invalida")

#Actividad 9
magnitud = int(input("ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print("Magnitud muy leve, imperceptible")
elif 3 <= magnitud and magnitud < 4:
    print("Magnitud leve, ligeramentet perceptible")
elif 4 <= magnitud and magnitud < 5:
    print("Magnitud moderada, sentido por personas, generalment sin daños")
elif 5 <= magnitud and magnitud < 6:
    print("Magnitud fuerte, puede causar daños a estructuras debiles")
elif 6 <= magnitud and magnitud < 7:
    print("Magnitud muy fuerte, puede causar daños significativos")
elif 7 <= magnitud:
    print("Magnitud extrema, puede causar graves daños a gran escala")

#Actividad 10
hemisferio = (input("ingrese en que hemisferio se encuentra N/S: "))
dia = int(input("ingrese que numero de dia hoy: "))
mes = int(input("ingrese el numero de mes"))

if hemisferio == "N":
    if mes == (1 or 2):
        print("Usted se encuentra en invierno")
    elif mes == (4 or 5):
        print("usted se encuentra en primavera")
    elif mes == (7 or 8):
        print("usted se encuentra en verano")
    elif mes == (10 or 11):
        print("Usted se encuentra en otoño")
    elif mes == 3:
        if dia < 21:
            print("usted se encuentra en invierno")
        else:
            print("Usted se encuentra en primavera")
    elif mes == 6:
        if dia < 21:
            print("usted se encuentra en primavera")
        else:
            print("Usted se encuentra en verano")
    elif mes == 9:
        if dia < 21:
            print("usted se encuentra en verano")
        else:
            print("Usted se encuentra en otoño")
    elif mes == 12:
        if dia < 21:
            print("usted se encuentra en Otoño")
        else:
            print("Usted se encuentra en invierno")
elif hemisferio == "S":
    if mes == (1 or 2):
        print("Usted se encuentra en verano")
    elif mes == (4 or 5):
        print("usted se encuentra en otoño")
    elif mes == (7 or 8):
        print("usted se encuentra en invierno")
    elif mes == (10 or 11):
        print("Usted se encuentra en primavera")
    elif mes == 3:
        if dia < 21:
            print("usted se encuentra en verano")
        else:
            print("Usted se encuentra en otoño")
    elif mes == 6:
        if dia < 21:
            print("usted se encuentra en otoño")
        else:
            print("Usted se encuentra en invierno")
    elif mes == 9:
        if dia < 21:
            print("usted se encuentra en invierno")
        else:
            print("Usted se encuentra en primavera")
    elif mes == 12:
        if dia < 21:
            print("usted se encuentra en primavera")
        else:
            print("Usted se encuentra en verano")
else:
    print("seleccione un hemisferio valido")