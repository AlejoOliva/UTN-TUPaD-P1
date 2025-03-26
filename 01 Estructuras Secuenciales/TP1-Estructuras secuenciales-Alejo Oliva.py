#Actividad 1
print("hola mundo!")

#Actividad 2
nombre = input("ingrese su nombre: ")
print(f"hola", nombre)

#Actividad 3
nombre2 = input("ingrese su nombre: ")
apellido = input ("ingrese su apellido: ")
edad = input ("ingrese su edad: ")
residencia = input("ingrese su lugar de residencia: ")
print(f"soy", nombre2,apellido,",tengo",edad,"y vivo en", residencia)

#Actividad 4
print("calcule el perimetro y el area de un circulo")
radio = int(input("ingrese el radio del circulo: "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print("el perimetro del circulo es igual a", perimetro , "y el area es", area)

#Actividad 5
print("calcule segundos a horas")
seg = int(input("Ingrese los segundos a calcular: "))
horas = seg / 3600
print("Es igual a", horas,"horas")

#Actividad 6
print("calcule la tabla de multiplicar de un numero")
num = int(input("ingrese un numero: " ))
tabla = num
for i in range(11):
    tabla = num * i
    print(num,"x",i ,"=",tabla)

#Actividad 7
print("Ingrese dos numeros enteros distintos de 0")
num1 = int(input("ingrese el primer numero: "))
num2= int(input("ingrese el segundo numero: "))
if (num1 and num2) != 0:
    suma7 = num1 + num2
    division7= num1 / num2
    multi7= num1 * num2
    resta7 = num1 - num2
    print("La suma de ambos numeros es igual a",suma7)
    print("La division de ambos numeros es igual a",division7)
    print("La multiplicacion de ambos numeros es igual a",multi7)
    print("La resta de ambos numeros es igual a",resta7)
else:
    print("Unos de los numeros ingresados es igual a 0")

#Activdad 8
print("Calcule su masa corporal")
altura = float(input("Ingrese su altura en m: "))
peso = int(input("Ingrese su peso en kg: "))
imc = peso // (altura ** 2)
print ("Su masa corporal es de", imc)

#Actividad 9
print("Transforme de celsius a Fahrenheit")
celsius = int(input("Ingrese la temperatura en grado celsius: "))
Fahr = celsius * 9 / 5 + 32
print("La temperatura es igual a", Fahr,"grados fahrenhit")

#Actividad 10
print("Calcule el promedio de tres numeros")
prom1 = int(input("Ingrese el primer numero: "))
prom2 = int(input("Ingrese el segundo numero: "))
prom3 = int(input("Ingrese el tercer numero: "))
prom = (prom1 + prom2 + prom3) / 3 
print("el promedio de los tres numeros es igual a", prom)




