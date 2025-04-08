import random

#Actividad 1
for i in range(101):
    print(i)

#Actividad 2
num2 = (input("Ingrese un numero entero: "))
dig = len(num2)

print("El numero contiene ", dig , " digitos")

#Actividad 3
num3 = int(input("Ingrese el primer valor: "))
num33 = int(input("Ingrese el segundo valor: "))
suma3 = 0

for i in range(num3 + 1 , num33):
    suma3 += i

print("La suma de todos los valores comprendidos es igual a ", suma3)

#Actividad 4
num4 = int(input("Ingrese un numero entero: "))
suma4 = 0

while num4 != 0:
    suma4 += num4
    num4 = int(input("Ingrese otro numero entero o Ingrese 0 para terminar la suma: "))

print("la suma total de todos los numeros ingresados es igual a ", suma4)

#Actividad 5
numrandom = random.randint(0,9)
print("Adivine el numero del 0 al 9")
adiv = int(input("Ingrese su numero: "))
intentos = 0

while numrandom != adiv:
    intentos += 1
    adiv = int(input("Ingrese otro numero: "))

print("Fueron necesarios", intentos, "intentos para acertar")

#Actividad 6
for i in range(100,-1, -2):
    print(i)

#Actividad 7
num7 = int(input(" Ingrese hasta que numero quiere sumar: "))
suma7 = 0

for i in range(num7):
    suma7 += i

print("La suma total de todos los numeros comprendidos es igual a ", suma7)

#Actividad 8
par8 = 0
impar8 = 0
pos8 = 0
neg8 = 0

print("Ingrese 100 numeros enteros")
for i in range(100):
    num8 = int(input("Ingrese un numero: "))
    if num8 % 2 == 0:
        par8 += 1
    else:
        impar8 += 1
    if num8 > 0:
        pos8 += 1
    else:
        neg8 += 1

print(par8, " numeros son pares")
print(impar8, " numeros son impares")
print(pos8, " numeros son positivos")
print(neg8, " numeros son negativos")

#Actividad 9
suma9 = 0

print("Ingrese 100 numeros enteros")
for i in range(100):
    num9 = int(input("Ingrese un numero: "))
    suma9 += num9
media = suma9 // 100

print("La media de todos los numeros ingresados es de ", media)

#Actividad 10
num10 = int(input("Ingrese el numero a invertir: "))
inver = 0

while num10 > 0:
    dig = num10 % 10
    inver = inver * 10 + dig
    num10 = num10 // 10

print("el numero invertido es ", inver)
