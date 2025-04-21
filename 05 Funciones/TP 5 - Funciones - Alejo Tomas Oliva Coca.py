######## FUNCIONES ########

# Actividad 1
def imprimir_hola_mundo():
    print("hola mundo")

# Actividad 2
def saludar_usuario(nombre):
    print("Hola", nombre, "!")
    
# Actividad 3
def informacion_personal(nombre,apellido,edad,residencia):
    print("soy", nombre, apellido, ", tengo", edad,"años y vivo en",residencia )

# Actividad 4
def calcular_area_circulo(radio):
    area = 3.14 * (radio**2)
    print("El area del circulo es de",area,"cm")
def calcular_perimetro_circulo(radio):
    per = 2 * 3.14 * radio
    print("El perimetro del circulo es de",per,"cm")

# Actividad 5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print("Equivale a", (round(horas,2)), "horas")

# Actividad 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        tabla = numero * i
        print(tabla)

# Actividad 7

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a // b
    print(suma,resta,multiplicacion,division)

# Actividad 8
def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    print("El indice de masa corporal es de", (round(imc,2)))

# Actividad 9
def celsius_a_fahrenheit(celsius):
    fahr = celsius * (9/5) + 32
    print("Equivale a ",fahr, "grados fahrenheit")

# Actividad 10
def calcular_promedio(a,b,c):
    prom  = (a + b + c) // 3
    print("El promedio es igual a", prom)


######## Programa Principal ########

# Actividad 1
(imprimir_hola_mundo())

# Actividad 2
nombre = input("Ingrese su nombre de usuario: ")
(saludar_usuario(nombre))

# Actividad 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residenecia: ")

informacion_personal(nombre,apellido,edad,residencia)

# Actividad 4
radio = int(input("Ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# Actividad 5
segundos = int(input("Ingrese cuantos segundos quiere pasar a horas: "))
segundos_a_horas(segundos)

# Actividad 6
numero = int(input("Ingrese el numero a calcular la tabla: "))
tabla_multiplicar(numero)

# Actividad 7
a = int(input("Ingrese el primer numero:"))
b = int(input("Ingrese el segundo numero: "))
operaciones_basicas(a,b)

# Actividad 8
peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
calcular_imc(peso,altura)

# Actividad 9
celsius = int(input("Ingrese los grados celsius a transformar: "))
celsius_a_fahrenheit(celsius)

# Actividad 10
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
calcular_promedio(a,b,c)

