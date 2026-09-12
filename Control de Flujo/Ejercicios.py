n = int(input('Ingrese un número: '))
for i in range(1, 13):
    print(f"{n} × {i} = {n * i}")

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