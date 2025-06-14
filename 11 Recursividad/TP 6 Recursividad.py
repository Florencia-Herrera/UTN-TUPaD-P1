#1 Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Pedir número al usuario
limite = int(input("Ingrese un número entero positivo: "))

print("Factoriales del 1 al", limite)
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

# 2 Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Pedir posición final
posicion = int(input("Mostrar la serie de Fibonacci hasta la posición: "))

print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")

# 3 Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un algoritmo general.
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Prueba general
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(f"{base}^{exponente} = {potencia(base, exponente)}")

# 4 Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicitar número decimal
numero = int(input("Ingrese un número entero positivo para convertir a binario: "))

# Caso especial si el número es 0
if numero == 0:
    print("0 en binario es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"{numero} en binario es: {binario}")

# 5 Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

# Ejemplo
print(es_palindromo("reconocer"))  # True
print(es_palindromo("python"))     # False

# 6 Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Ejemplos
print(suma_digitos(1234))  # 10
print(suma_digitos(9))     # 9
print(suma_digitos(305))   # 8

# 7 Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Ejemplos
print(contar_bloques(1))  # 1
print(contar_bloques(2))  # 3
print(contar_bloques(4))  # 10

# 8 Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas vecesaparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Ejemplos
print(contar_digito(12233421, 2))  # 3
print(contar_digito(5555, 5))      # 4
print(contar_digito(123456, 7))    # 0
