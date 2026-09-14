n = int(input('Ingrese un número: '))
for i in range(1, 13):
    print(f"{n} × {i} = {n * i}")

'''Ejercicio 2: Contador de dígitos de un número entero
1.- Entender el problema
Entrada: Un número entero cualquiera (int), puede ser positivo, negativo o cero.
Proceso:abs(num) ➔ Convierte el número a su valor absoluto para neutralizar los 
signos negativos.Si el número es exactamente 0, se define directamente que tiene 1 dígito.
Si es mayor a cero, se ejecuta un bucle que divide el número de forma entera entre 10 (n // 10) 
repetidamente hasta que el número llegue a cero, sumando +1 a un contador en cada vuelta.
Salida: La cantidad total de dígitos que componen al número.
2.- Bosquejo a mano
num = -345 ➔ Valor absoluto n = 345
Vuelta 1: digitos = 1 ➔ 345 // 10 = 34
Vuelta 2: digitos = 2 ➔ 34 // 10 = 3
Vuelta 3: digitos = 3 ➔ 3 // 10 = 0 (Termina el ciclo)
Resultado esperado: "3 dígitos"
3.- Descubrir patrón
Tiene 1 entrada y 1 salida. Aplica el algoritmo matemático por descomposición decimal sucesiva,
utilizando un bucle condicional while cuyo criterio de parada depende de la reducción a cero 
de la variable numérica por divisiones sucesivas.
4.- Código'''
num = int(input("Número: "))
n = abs(num)                
digitos = 0
if n == 0:
    digitos = 1            
else:
    while n > 0:
        digitos += 1
        n = n // 10 
print(f"{digitos} dígitos")

n = int(input('Ingrese números: '))                                            
suma_pares = 0
suma_impares = 0
for i in range(n):
    x = int(input(f'Números {i+1}: '))
    if x % 2 == 0:
        suma_pares += x
    else : suma_impares += x
print(f'Suma de pares: {suma_pares}')
print(f'Suma de pares: {suma_impares}')

while True:
    edad = int(input("Edad (0-120): "))
    if 0 <= edad <= 120:
        break                       
    print("Error, intenta de nuevo")
print(f"Edad válida: {edad}")

import random
secreto = random.randint(1, 100)
intentos = 0
while True:
    intento = int(input("Adivina (1-100): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto en {intentos} intentos!")
        break
    elif intento < secreto:
        print("Es mayor")
    else:
        print("Es menor")

n = int(input("¿Cuántos? "))
a, b = 0, 1                      
for _ in range(n):               
    print(a, end=" ")
    a, b = b, a + b  
print()                       