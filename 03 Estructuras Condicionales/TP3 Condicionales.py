#ACTIVIDADES
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

# Pedimos al usuario que ingrese su edad
edad=int(input("Por favor, ingrese su edad: "))

if edad>= 18:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 
#Pedimos al usuario que ingrese su nota
nota=int(input("Por favor, ingrese su nota"))

if nota>=6 :
    print("Aprobado")
else:
    print("Desaprobado")

#3scribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar. 
#Pedimos al usuario que ingrese un numero
numero=int(input("Por favor, ingrese un numero"))

if numero%2 == 0:   #Un número es par si al dividirlo por 2, el resto es 0
   print("Ha ingresado un numero par")
else:
    print("Por favor,ingrese un numero par")

#4  Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# Niño/a: menor de 12 años. 
# Adolescente: mayor o igual que 12 años y menor que 18 años. 
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#Adulto/a: mayor o igual que 30 años.

#Pedimos al usuario que ingrese su edad
edad=int(input("Por favor, ingrese su edad"))

if edad<12:
    print("Niño/a")
elif edad>=12 and edad<18:
    print("Adolescente")
elif edad>=18 and edad<30:
    print("Adulto/a joven")

else:
    print("Adulto/a")

# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
  # Pedimos al usuario que ingrese una contraseña
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

# Verificamos la longitud usando len()
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) 

import random
import statistics

# Generamos la lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos moda, mediana y media
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

# Mostramos los valores
print("Números aleatorios:", numeros_aleatorios)
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media:.2f}")

# Evaluamos el sesgo
if moda < mediana < media:
    print("Sesgo positivo (asimetría a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (asimetría a la izquierda)")
else:
    print("No hay sesgo significativo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla
# Solicitamos una frase o palabra al usuario
texto = input("Ingrese una frase o palabra: ")

# Verificamos si termina con una vocal (mayúscula o minúscula)
if texto[-1].lower() in "aeiou":
    texto += "!"
    
# Mostramos el resultado
print("Resultado:", texto)


#8)Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
#. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#elprograma debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

# Pedimos al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Pedimos al usuario que elija una opción
print("Elija una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra mayúscula")

opcion = input("Ingrese 1, 2 o 3 según su elección: ")

# Transformamos el nombre según la opción
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción inválida. Por favor, ingrese 1, 2 o 3.")

#9) 
# Pedimos la magnitud del terremoto al usuario
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasificamos según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10)

# Pedimos los datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Ingrese el mes (en número, por ejemplo, 1 para enero): "))
dia = int(input("Ingrese el día: "))

# Función auxiliar para facilitar las comparaciones de fechas
def es_fecha_despues(mes_actual, dia_actual, mes_ref, dia_ref):
    return (mes_actual > mes_ref) or (mes_actual == mes_ref and dia_actual >= dia_ref)

def es_fecha_antes(mes_actual, dia_actual, mes_ref, dia_ref):
    return (mes_actual < mes_ref) or (mes_actual == mes_ref and dia_actual <= dia_ref)

# Determinar estación
if es_fecha_despues(mes, dia, 12, 21) or es_fecha_antes(mes, dia, 3, 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif es_fecha_despues(mes, dia, 3, 21) and es_fecha_antes(mes, dia, 6, 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif es_fecha_despues(mes, dia, 6, 21) and es_fecha_antes(mes, dia, 9, 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
elif es_fecha_despues(mes, dia, 9, 21) and es_fecha_antes(mes, dia, 12, 20):
    estacion = "Otoño" if hemisferio == "N" else "Primavera"
else:
    estacion = "Fecha inválida o fuera de rango"

# Mostramos el resultado
print("La estación en tu ubicación es:", estacion)
