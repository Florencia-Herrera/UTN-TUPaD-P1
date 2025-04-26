#Actividades
#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):  # Desde 0 hasta 100 (inclusive)
    print(i)

#2 ) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene
# Solicitar al usuario un número entero
numero = int(input("Introduce un número entero: "))

# Calcular la cantidad de dígitos
cantidad_digitos = len(str(abs(numero)))  # Usamos abs para manejar números negativos

# Mostrar el resultado
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
 
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
# Solicitar al usuario dos números enteros
inicio = int(input("Introduce el primer número entero: "))
fin = int(input("Introduce el segundo número entero: "))

# Asegurarnos de que el primer número sea menor que el segundo
if inicio >= fin:
    print("El primer número debe ser menor que el segundo.")
else:
    # Sumar los números entre el rango excluyendo los dos valores
    suma = sum(range(inicio + 1, fin))
    print(f"La suma de los números entre {inicio} y {fin} (excluyendo ambos) es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0
# Inicializar la variable para la suma acumulada
suma_acumulada = 0

# Bucle que sigue pidiendo números hasta que el usuario ingrese un 0
while True:
    numero = int(input("Introduce un número entero (0 para detenerse): "))
    
    # Si el número es 0, detener el programa
    if numero == 0:
        break
    
    # Sumar el número al total acumulado
    suma_acumulada += numero

# Mostrar el resultado final
print(f"La suma total acumulada es: {suma_acumulada}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

# Generar un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)

# Inicializar el contador de intentos
intentos = 0

# Bucle para que el usuario siga adivinando
while True:
    # Solicitar al usuario un número
    adivinanza = int(input("Adivina un número entre 0 y 9: "))
    
    # Contabilizar el intento
    intentos += 1
    
    # Comprobar si el número adivinado es correcto
    if adivinanza == numero_aleatorio:
        print(f"¡Felicidades! Has acertado el número {numero_aleatorio} en {intentos} intentos.")
        break
    elif adivinanza < numero_aleatorio:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
# Imprimir los números pares entre 0 y 100 en orden decreciente
for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
# Solicitar al usuario un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Verificar que el número sea positivo
if numero < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    # Calcular la suma de los números desde 0 hasta el número indicado
    suma = sum(range(numero + 1))  # range incluye 0 hasta el número especificado
    
    # Mostrar el resultado
    print(f"La suma de los números entre 0 y {numero} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
# Inicializar los contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Establecer la cantidad de números a ingresar (puedes cambiar este valor)
cantidad_numeros = 100

# Pedir al usuario que ingrese 'cantidad_numeros' números
for i in range(cantidad_numeros):
    numero = int(input(f"Introduce el número {i + 1}: "))
    
    # Contar números pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Contar números positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Mostrar los resultados
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor)
# Inicializar las variables
suma = 0

# Establecer la cantidad de números a ingresar (puedes cambiar este valor)
cantidad_numeros = 100

# Pedir al usuario que ingrese 'cantidad_numeros' números
for i in range(cantidad_numeros):
    numero = int(input(f"Introduce el número {i + 1}: "))
    suma += numero

# Calcular la media
media = suma / cantidad_numeros

# Mostrar el resultado
print(f"La media de los {cantidad_numeros} números ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
# Solicitar al usuario que ingrese un número
numero = input("Introduce un número entero: ")

# Invertir el número usando slicing
numero_invertido = numero[::-1]

# Mostrar el resultado
print(f"El número invertido es: {numero_invertido}")
