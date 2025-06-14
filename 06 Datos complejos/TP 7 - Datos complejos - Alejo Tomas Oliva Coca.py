### Trabajo practico 8 ###

# Actividad 1
print("-----------------Actividad 1-----------------")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


# Actividad 2
print("-----------------Actividad 2-----------------")

precios_frutas["Banana"] = 1300
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# Actividad 3
print("-----------------Actividad 3-----------------")

print(precios_frutas.keys())

# Actividad 4
print("-----------------Actividad 4-----------------")
print("....Programa que almacena maximo 5 contactos y sus numeros telefonicos....")

contactos ={}
for a in range(5):
    contactos[input("Ingrese el nombre un contacto --> ")] = input("ingrese el numero telefonico de su contacto --> ")

    seguir = input("Si quiere agregar mas contactos escriba S y si no N --> ")
    if seguir == "S":
        continue
    else:
        break

# Consulta de contacto
consulta = input("Si quiere consulter el numero asociado a algun contacto ingrese 1 y sino 0 --> ")
if consulta == "1":
    nombre = input("Ingrese el nombre del contacto --> ")
    if nombre in contactos:
        print(f"El número de {nombre} es {contactos[nombre]}")
    else:
        print("Ese contacto no está en la agenda.")
else:
    pass

# Actividad 5
print("-----------------Actividad 5-----------------")

frase = input("ingrese la frase que quiera --> ")
palabras = frase.split
palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print(f"Las palabras unicas que aparecen en la frase son {palabras_unicas}")
print(f"La cantidad de veces que aparece cada palabra es de {recuento}")


# Actividad 6
print("-----------------Actividad 6-----------------")

alumnos = {
    input("ingrese el primer alumno --> "): (int(input("primer nota: ")),int(input("segunda nota: ")),int(input("tercer nota: "))),
    input("ingrese el segundo alumno --> "): (int(input("primer nota: ")),int(input("segunda nota: ")),int(input("tercer nota: "))),
    input("ingrese el tercer alumno --> "):  (int(input("primer nota: ")),int(input("segunda nota: ")),int(input("tercer nota: ")))
}

prom1 = 0
prom2 = 0
prom3 = 0

for a in list(alumnos.values())[0]:
    prom1 += a

for a in list(alumnos.values())[1]:
    prom2 += a

for a in list(alumnos.values())[2]:
    prom3 += a

prom1 = prom1 // 3
prom2 = prom2 // 3
prom3 = prom3 // 3




print(f"El promedio de {list(alumnos.keys())[0]} es igual a {prom1}")
print(f"El promedio de {list(alumnos.keys())[1]} es igual a {prom2}")
print(f"El promedio de {list(alumnos.keys())[2]} es igual a {prom3}")




# Actividad 7
print("-----------------Actividad 7-----------------")

parcial1 = {102, 105, 108, 110, 113, 115, 119}
parcial2 = {101, 105, 107, 110, 112, 115, 117, 120}

print(f"Los estudiantes que aprobaron ambos parciales fueron {parcial1 & parcial2}")
print(f"Los estudiantes que aprobaron solo un parcial fueron {parcial1 ^ parcial2}")
print(f"Los estudiantes que aprobaron el parcial 2 fueron {parcial1 | parcial2}")


# Actividad 8
print("-----------------Actividad 8-----------------")

productos = {}

while True:
    print("Ingrese 1 para agregar un nuevo producto ")
    print("Ingrese 2 para consultar el stock de un producto ")
    print("Ingrese 3 para cambiar el stock de un producto ")
    print("Ingrese 4 para salir ")

    print("..............................")

    opcion = int(input("ingrese su opcion deseada --->"))

    print("..............................")

    if opcion == 1:
        productos[input("ingrese el nombre del producto --> ")] = input(" Cantidad de stock del producto --> ")
    elif opcion == 2:
        print(f"La cantidad de stock es de: {productos[input("ingrese el nombre del producto a consultar stock -->")]}")
    elif opcion == 3:
        productos[input("ingrese el nombre del producto al que se le cambiara el stock --> ")] = input(" Cantidad nueva de stock del producto --> ")
    elif opcion == 4:
        break
    else:
        print("opcion ingresada no valida")

    print("..............................")


# Actividad 9
print("-----------------Actividad 9-----------------")

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input("Ingrese el día: ")
hora = input("Ingrese la hora (por ejemplo, 10:00): ")

if (dia, hora) in agenda:
    print(f"En {dia} a las {hora} hay: {agenda[(dia, hora)]}")
else:
    print("No hay ninguna actividad agendada en ese día y hora.")


# Actividad 10
print("-----------------Actividad 10-----------------")

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}


invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print("original =", original)
print("invertido =", invertido)





