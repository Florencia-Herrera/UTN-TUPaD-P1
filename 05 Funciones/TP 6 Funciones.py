# Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamada a la función
imprimir_hola_mundo()


# Función que recibe un nombre y retorna un saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Solicita nombre al usuario e imprime el saludo
nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))


# Función que muestra información personal usando 4 parámetros
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Solicita datos al usuario y llama a la función
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


# Importa el módulo math para operaciones matemáticas
import math

# Calcula el área de un círculo (π * r²)
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Calcula el perímetro de un círculo (2 * π * r)
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Solicita radio, calcula e imprime resultados con 2 decimales
radio = float(input("Ingrese el radio: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")


# Convierte segundos a horas (segundos / 3600)
def segundos_a_horas(segundos):
    return segundos / 3600

# Solicita segundos e imprime equivalencia en horas
segundos = int(input("Ingrese los segundos: "))
print(f"Equivale a {segundos_a_horas(segundos):.2f} horas")


# Imprime la tabla de multiplicar del 1 al 10 para un número dado
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicita un número y genera su tabla de multiplicar
numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)


# Realiza las 4 operaciones básicas y retorna una tupla con resultados
def operaciones_basicas(a, b):
    # Evita división por cero usando operador ternario
    return (a + b, a - b, a * b, a / b if b != 0 else "División por cero")

# Solicita dos números, realiza operaciones e imprime resultados
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
suma, resta, multi, div = operaciones_basicas(a, b)
print(f"Suma: {suma}\nResta: {resta}\nMultiplicación: {multi}\nDivisión: {div}")


# Calcula el Índice de Masa Corporal (IMC = peso / altura²)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicita peso y altura, luego muestra IMC con 2 decimales
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
print(f"Tu IMC es {calcular_imc(peso, altura):.2f}")


# Convierte grados Celsius a Fahrenheit (F = C * 9/5 + 32)
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Solicita temperatura en Celsius e imprime equivalencia en Fahrenheit
c = float(input("Temperatura en °C: "))
print(f"Equivale a {celsius_a_fahrenheit(c):.2f} °F")


# Calcula el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Solicita tres números e imprime su promedio
a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))
print(f"Promedio: {calcular_promedio(a, b, c):.2f}")