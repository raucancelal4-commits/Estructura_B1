'''Ejercicio 1: Cálculo de IVA con funciones
1.- Entender el problema
Entrada: Precio del producto (float).
Proceso:calcular_iva(precio) ➔ Multiplica el precio por 0.15 para 
obtener el impuesto.calcular_total(precio) ➔ Llama a la función anterior y le suma el impuesto al precio base.
Salida: El precio total con el IVA incluido.
2.- Bosquejo a manoprecio = 200
Paso 1 (calcular_iva): 200 * 0.15 = 30
Paso 2 (calcular_total): 200 + 30 = 230
Resultado esperado: "Total con IVA: $230.00"
3.- Descubrir patrón
Hay 1 entrada decimal y 1 salida. El patrón consiste en la modularización mediante funciones, 
donde una función principal (calcular_total) depende del valor de retorno de una función 
secundaria (calcular_iva) para completar su cálculo.
4.- Código'''
def calcular_iva(precio):
    return precio * 0.15
def calcular_total(precio):
    iva = calcular_iva(precio)
    return precio + iva
precio = float(input("Precio: $"))
total = calcular_total(precio)
print(f"Total con IVA: ${total:.2f}")

'''Ejercicio 2: Contador de números primos en un rango
1.- Entender el problema
Entrada: Dos números enteros que definen el inicio a y el fin b del rango (int).
Proceso:Iterar con un ciclo desde a hasta b.Para cada número, validar si es menor a 2 (no es primo).
Utilizar otro ciclo interno desde 2 hasta el número anterior para verificar si tiene divisores 
exactos (num % i == 0).Si no tiene divisores, se incrementa un contador de números primos.
Salida: La cantidad total de números primos encontrados en el rango.
2.- Bosquejo a mano
a = 3, b = 10 (Rango: 3, 4, 5, 6, 7, 8, 9, 10)
¿3 es primo? Sí (contador = 1)
¿4 es primo? No (divisible para 2)
¿5 es primo? Sí (contador = 2)
¿6, 8, 9, 10? No son primos.
¿7 es primo? Sí (contador = 3)
Resultado esperado: "Hay 3 números primos entre 3 y 10"
3.- Descubrir patrónTiene 2 entradas y 1 salida entera. Utiliza el patrón de anidación de 
bucles (for dentro de for) combinado con una bandera booleana (es_primo) y una estructura
de ruptura (break) para optimizar la búsqueda de divisores exactos.
4.- Código'''
def contar_primos(a, b):
    cantidad = 0
    for num in range(a, b + 1):
        es_primo = True
        if num < 2:
            es_primo = False
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            cantidad += 1
    return cantidad
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
resultado = contar_primos(a, b)
print(f"Hay {resultado} números primos entre {a} y {b}")

'''Ejercicio 3: Verificación de número narcisista
1.- Entender el problema
Entrada: Un número entero n (int).
Proceso:Convertir el número a texto (str) para contar cuántos dígitos tiene (len).
Iterar sobre cada dígito, elevarlo a la potencia de la cantidad de dígitos y sumarlos.
Comparar si la suma final es igual al número original (True o False).
Salida: Un mensaje indicando si el número cumple o no con la condición.
2.- Bosquejo a mano
n = 153 (Tiene 3 dígitos)
Paso 1: 1**3 + 5**3 + 3**3
Paso 2: 1 + 125 + 27 = 153
Paso 3: ¿153 es igual a 153? Sí.
Resultado esperado: "Es un número narcisista"
3.- Descubrir patrónTiene 1 entrada y una salida condicional. Aplica un patrón de casteo o
conversión de tipos de datos (int a str para medir y separar, y luego de str a int para 
operar matemáticamente) junto con una acumulación en un ciclo for.
4.- Código'''
def es_narcisista(n):
    digitos = str(n)
    cantidad = len(digitos)
    suma = 0
    for digito in digitos:
        suma += int(digito) ** cantidad
    return suma == n
n = int(input("Ingrese un número: "))
if es_narcisista(n):
    print("Es un número narcisista")
else:
    print("No es un número narcisista")

'''Ejercicio 4: Calculadora con menú interactivo
1.- Entender el problema
Entrada: Dos números enteros iniciales (b y d) y la opción elegida del menú (str).
Proceso:Crear funciones individuales para cada operación aritmética básica.
Mostrar un menú visual repetitivamente utilizando un ciclo infinito.
Evaluar la opción del usuario para ejecutar la función matemática correspondiente o cerrar el programa.
Salida: Resultados numéricos según la operación seleccionada hasta que se elija salir.
2.- Bosquejo a mano
b = 10, d = 5
Menú en pantalla ➔ Usuario digita "4" (Multiplicación).
Paso 1: Se ejecuta multiplicacion() ➔ 10 * 5 = 50.
Menú en pantalla ➔ Usuario digita "5" (Salir).
Paso 2: Se rompe el bucle.
Resultado esperado: "El resultado es: 50", "Adios, Chao"
3.- Descubrir patrón
Tiene 3 entradas principales y salidas repetitivas. Emplea el patrón de bucle de control 
infinito (while True) para mantener el programa vivo, usando condicionales múltiples (if-elif-else)
para direccionar el flujo y la instrucción break como cláusula de escape.
4.- Código'''
b = int(input('Numero: '))
d =int(input('Otro numero: '))
def suma():
    return b + d
def dividir():
    return b / d
def resta():
    return b - d
def multiplicacion():
    return b * d
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Dividir")
    print("3. Resta")
    print("4. Multiplicación")
    print("5. Salir")
while True:
        mostrar_menu()
        opcion = input("Opción: ")
        if opcion == "1":
            print("Resultado es: ",suma())
        elif opcion == "2":
            print("Resultado es: ",dividir())
        elif opcion == "3":
            print("Resultado es: ", resta())
        elif opcion == "4":
            print("El resultado es: ", multiplicacion())
        elif opcion == "5":
            print("Adios, Chao")
            break
        else:
            print("Opción inválida")