### TRABAJO PRACTICO 6 ###

# 1
def factorial_recur(num):
    if num == 0:
        return 1
    return num * factorial_recur(num - 1)

# 2
def fibonacci_recur(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
       return (fibonacci_recur(num - 1) + fibonacci_recur(num - 2))
    
def serie_fibonacci(num):
    return list(fibonacci_recur(i) for i in range (num + 1))
       

# 3
def potencia_recur(num,potencia):
    if potencia == 0:
        return 1
    elif potencia == 1:
        return num
    else:
        return num * potencia_recur(num, potencia - 1)
    

# 4
def binario_recur(num):
    if num < 0:
        return "Ingrese un numero entero positivo"
    elif num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return binario_recur(num // 2) + str(num % 2)


# 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return "es palindromo"
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return "no es palindromo"


# 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)


# 7
def contar_bloques(bloques):
    if bloques == 1:
        return 1
    else:
        return contar_bloques(bloques - 1) + bloques


# 8
def contar_digito(numero,digitos):
    ult_digito = numero % 10
    if numero == digitos:
        return 1
    elif ult_digito == digitos:
        return 1 + contar_digito(numero//10, digitos) 
    else:
        return contar_digito(numero//10, digitos) 

# Codigo Principal

# Punto 1
print("-----------------Punto 1-----------------")

num1 = int(input("Ingrese el numero a calcular su factorial --> "))
print(f"el factorial de {num1} es igual a {factorial_recur(num1)} ")

# Punto 2
print("-----------------Punto 2-----------------")

pos = int(input("Ingrese la posicion a calcular en la serie fibonacci --> "))
print(f"el valor de la serie fibonacci en la posicion indicada es de {fibonacci_recur(pos)}")
print(f"----Serie completa hasta la posicion es----")
print(serie_fibonacci(pos))

# Punto 3
print("-----------------Punto 3-----------------")

num3 = int(input("Ingrese el numero a calcular --> "))
potencia = int(input("Ingrese la potencia a elevar el numero --> "))
print(f"el resultado de {num3} elevado sobre {potencia} es igual a {potencia_recur(num3,potencia)}")

# Punto 4
print("-----------------Punto 4-----------------")

num4 = int(input("Ingrese un numero entero natural a convertir en binario --> "))
print(f"El numero {num4} es igual a {binario_recur(num4)} en numero binarios")

# Punto 5
print("-----------------Punto 5-----------------")

palabra5 = input("Ingrese una palabra sin espacios ni tildes para ver si es palindromo --> ")
print(f"La palabra ingresada {es_palindromo(palabra5)}")

# Punto 6
print("-----------------Punto 6-----------------")

num6 = int(input("Ingrese el numero para sumar cada uno de sus digitos --> "))
print(f"la suma total de cada uno de sus digitos es igual a {suma_digitos(num6)}")

# Punto 7
print("-----------------Punto 7-----------------")

bloques = int(input("Ingrese la cantidad de bloques utilizados en la base --> "))
print(f"La cantidad de bloques total que se va a necesitar es de {contar_bloques(bloques)}")

# Punto 8
print("-----------------Punto 8-----------------")

num8 = int(input("Ingrese el numero para contar cuantas veces aparece un digito --> "))
digito = int(input("Ingrese el digito a revisar --> "))
print(f"La cantidad de veces que aparece el digito {digito} en {num8} es de {contar_digito(num8,digito)} veces")










