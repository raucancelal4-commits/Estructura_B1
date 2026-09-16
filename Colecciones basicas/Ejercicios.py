'''Ejercicio 1: Conteo de vocales en una frase
1. Entender el problema
Entrada: Una frase o texto ingresado por teclado (cadena de texto).
Proceso: Convertir el texto a minúsculas, recorrer carácter por carácter y 
verificar si pertenece al conjunto de vocales ("aeiouAEIOU"). Incrementar un 
contador por cada coincidencia.
Salida: La cantidad total de vocales encontradas.
2. Bosquejo a mano (Frase: "Hola")
Convertir a minúsculas: "hola"
Carácter 'h': ¿Está en "aeiouAEIOU"? No -> ttal = 0
Carácter 'o': ¿Está en "aeiouAEIOU"? Sí -> ttal = 1
Carácter 'l': ¿Está en "aeiouAEIOU"? No -> ttal = 1
Carácter 'a': ¿Está en "aeiouAEIOU"? Sí -> ttal = 2
Resultado esperado: 2 Vocales.
3. Descubrir patrón
Pertenencia e incremento: Uso del operador in para evaluar si el carácter 
pertenece al conjunto de vocales y actualización del acumulador ttal += 1.
4. Código'''
Mensaje = input('Frase: ').lower()
vocal = "aeiouAEIOU"
ttal = 0
for sh in Mensaje:
    if sh in vocal:
        ttal += 1
print(f"{ttal} Vocales.")

'''Ejercicio 2: Estadísticas de notas (Promedio, Máximo y Mínimo)
1. Entender el problema
Entrada: Una lista predefinida de notas numéricas.
Proceso: Calcular el promedio dividiendo la suma total (sum) para la cantidad de elementos (len). 
Obtener el valor máximo con max() y el mínimo con min().
Salida: Valores máximo y mínimo impresos con formato de 2 decimales.
2. Bosquejo a mano (notas = [7, 8.5, 6, 9, 10, 5.5])
Suma total: 7 + 8.5 + 6 + 9 + 10 + 5.5 = 46.0
Cantidad: 6 
Promedio: 46.0 / 6 = 7.67
Máximo: 10.00 ; Mínimo: 5.50
Resultado esperado:Maximo es: 10.00 Minimo es: 5.50
3. Descubrir patrón
Uso de funciones nativas de agregación: Operaciones directas sobre colecciones (sum, len, max, min) 
combinadas con formato de cadenas f-string (:.2f).
4. Código'''
notas= [7, 8.5, 6, 9, 10, 5.5]
promedio= sum(notas) /len(notas)
Maximo = print(f"Maximo es: {max(notas):.2f}")
Minimo = print(f"Minimo es: {min(notas):.2f}")

'''Ejercicio 3: Eliminar duplicados y ordenar una lista
1. Entender el problema
Entrada: Una lista de caracteres/cadenas con elementos repetidos.
Proceso: Convertir la lista a un conjunto (set) para eliminar duplicados y luego aplicar 
sorted() para ordenar los elementos restantes alfabéticamente.
Salida: Una nueva lista ordenada con valores únicos.
2. Bosquejo a mano (ordena = ["a", "b", "a", "c", "b", "d"])
Paso 1 (set): Elimina duplicados -> {'a', 'b', 'c', 'd'}
Paso 2 (sorted): Ordena alfabéticamente -> ['a', 'b', 'c', 'd']
Resultado esperado: ['a', 'b', 'c', 'd']
3. Descubrir patrón
Conversión de colecciones: Explotar la propiedad de los conjuntos (set) donde no existen 
elementos duplicados, devolviendo una estructura limpia mediante sorted().
4. Código'''
ordena = ["a", "b", "a", "c", "b", "d"]
sin_repetir = sorted(set(ordena))
print(sin_repetir)

texto = input("Frase: ")
conteo = {}
for palabra in texto.split() :
    conteo[palabra]= conteo.get(palabra, 0)+1
print(conteo) 
mas = max(conteo, key = conteo.get)
print(f"Mas repetida: '{mas}' ({conteo[mas]} veces)")