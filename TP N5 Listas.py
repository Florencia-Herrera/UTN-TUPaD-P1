#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
mis_favoritos = ["papas fritas", "música", "viajes", "series", "gatos"]
penultimo_elemento = mis_favoritos[-2]
print(penultimo_elemento)

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.
lista_vacia = []  

lista_vacia.append("sol")
lista_vacia.append("mar")
lista_vacia.append("arena")

print(lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"   # Segundo valor (índice 1)
animales[-1] = "oso"   # Último valor (índice -1)

print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros= [8,15,3,22,7] #Se crea una lista con sus respectivos valores.
numeros.remove(max(numeros)) #La funcion max se encarga de buscar el numero mas grande de la lista y la funcion remove de eliminarlo.
print(numeros) #Se imprime la lista modificada

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
numeros = list(range(10, 31, 5))
print(numeros[:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos = ["sedan", "polo", "suran", "gol"]

autos[1:3] = ["civic", "corolla"]

print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla
dobles = []  # Lista vacía

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

# Lista inicial de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][compras[1].index("fideos")] = "tallarines"

#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

#d) Imprimir la lista resultante por pantalla
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

# Crear la lista anidada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# Imprimir la lista resultante
print(lista_anidada)


