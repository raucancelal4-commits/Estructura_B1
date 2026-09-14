'''Ejercicio 1: Cálculo del área de un rectángulo
1.- Entender el problema
Entrada: Base (float/int) y altura (float/int) pasadas como argumentos a la función.
Proceso:cal_area(base, altura) ➔ Multiplica el valor de la base por la 
altura para calcular la superficie.
Salida: El valor del área calculada del rectángulo.
2.- Bosquejo a mano
base = 10, altura = 100
Paso 1: 10 * 100 = 1000
Resultado esperado: 1000
3.- Descubrir patrón
Tiene 2 entradas numéricas y 1 salida. El patrón aplica una fórmula geométrica
directa encapsulada en una función reutilizable, capaz de recibir tanto números 
enteros como decimales dinámicamente.
4.- Código'''
def cal_area(base,altura):
    return base * altura 
print(cal_area(10,100))
print(cal_area(5,4.5))

'''Ejercicio 2: Encontrar el número máximo de tres valores
1.- Entender el problema
Entrada: Tres números (a, b, c) recibidos por parámetro.
Proceso:
Enfoque 1 (maximo): Usa la función nativa de Python max().
Enfoque 2 (maxino_manual): Supone que a es el mayor. Luego, compara secuencialmente 
si b es mayor o si c es mayor, actualizando la variable en caso afirmativo.
Salida: El número más grande de los tres.
2.- Bosquejo a mano
a = 10, b = 100, c = -4
Paso 1: Asignar mayor = 10
Paso 2: ¿100 > 10? Sí ➔ mayor = 100
Paso 3: ¿-4 > 100? No ➔ mayor se queda en 100
Resultado esperado: 100
3.- Descubrir patrón
Tiene 3 entradas y 1 salida. El patrón demuestra el uso de un algoritmo de ordenamiento
o selección lineal secuencial, donde se descartan elementos paso a paso mediante 
condicionales if simples e independientes.
4.- Código'''
def maximo(a,b,c):
    return max(a , b, c)
def maxino_manual(a,b,c):
    mayor = a
    if b > mayor : mayor = b
    if c > mayor : mayor = c
    return mayor 
print(maximo(10,100,-4))
print(maximo(-1,0,1))

'''Ejercicio 3: Verificación de año bisiesto
1.- Entender el problema
Entrada: Un número entero correspondiente a un año (int).
Proceso:Un año es bisiesto si es divisible para 4,
pero no para 100, a menos que también sea divisible para 400.
Se evalúan los residuos aritméticos (%) con respecto a 4, 100 y 400.
Salida: Un valor booleano (True o False) que confirma si el año es bisiesto.
2.- Bosquejo a mano
anio = 2024
Paso 1: 2024 % 4 == 0 ➔ True
Paso 2: 2024 % 100 == 0 ➔ False
Paso 3: Evaluar expresión ➔ (True and not False) or False ➔ True
Resultado esperado: El año 2024 es bisiesto: True
3.- Descubrir patrón
Tiene 1 entrada entera y una salida booleana. El patrón radica en el uso
de la lógica matemática proposicional (operadores and, or, not) para 
empaquetar reglas de negocio del calendario gregoriano en una sola línea de código evaluable.
4.- Código'''
def es_bisiesto(anio):
    divisible_4 = anio % 4 == 0
    divisible_100 = anio % 100 == 0
    divisible_400 = anio % 400 == 0
    return (divisible_4 and not divisible_100) or divisible_400
anio = int(input("Ingrese un año: "))
print(f"El año {anio} es bisiesto: {es_bisiesto(anio)}")
def es_bisiesto_corta(anio):
    return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)
print(es_bisiesto_corta(2024))
for y in [2024, 2025, 2014, 2004]:
    print(f"{y}: {es_bisiesto_corta(y)}")

'''Ejercicio 4: Factorial y coeficiente combinatorio
1.- Entender el problema
Entrada: Valores enteros para el total de elementos n y el tamaño del grupo k.
Proceso:factorial(n) ➔ Multiplica consecutivamente un acumulador desde 2 hasta
n mediante un ciclo for.combinatorio(n, k) ➔ Aplica la fórmula estadística de 
combinaciones sin repetición: \(n! / (k! \times (n-k)!)\) usando división entera //.
Salida: El número de combinaciones posibles.
2.- Bosquejo a manon = 5 para factorial
Paso 1: 1 * 2 * 3 * 4 * 5 = 120
Resultado esperado: 120
3.- Descubrir patrón
Tiene 2 entradas y 1 salida de tipo entero largo. Utiliza el patrón de 
acumulación por producto multiplicativo dentro de un ciclo de rango 
determinado, acoplado a otra función matemática de orden superior.
4.- Código'''
def factorial (n):
    fact = 1
    for i in range (2, n +1):
        fact *= i
    return fact
def combinatorio(n,k):
    return factorial(n) // (factorial(k) * factorial( n - k))
print(factorial(5))
print(combinatorio(5,10))

'''Ejercicio 5: Calculadora interactiva con control de división para cero
1.- Entender el problema
Entrada: Una opción de menú (str) y dos números flotantes a y b.
Proceso:Se declaran minifunciones en una sola línea para las operaciones básicas.
En la función dividir, se valida si el denominador es cero. Si lo es, retorna un 
objeto especial None.Se controla el flujo interactivo en un bucle infinito mediante while True.
Salida: El resultado decimal de la operación escogida o advertencias de error.
2.- Bosquejo a mano
op = "4" (Dividir), a = 15, b = 0
Paso 1: Se llama a dividir(15, 0) ➔ Detecta que b == 0 y devuelve None.
Paso 2: El menú evalúa si el resultado es None e interrumpe el ciclo con continue mostrando alerta.
Resultado esperado: "No se puede dividir entre 0"
3.- Descubrir patrón
Tiene múltiples entradas dinámicas. Utiliza el patrón de funciones lambda
encubiertas o compactas, un bucle infinito controlado y una validación de 
seguridad contra errores en tiempo de ejecución (excepciones lógicas) al 
controlar que no se rompa el sistema por una división entre cero.
4.- Código'''
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        return None           
    return a / b
while True:
    print("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
    op = input("Opción: ")
    if op == "5":
        break
    a = float(input("a: "))
    b = float(input("b: "))
    if op == "1": r = sumar(a, b)
    elif op == "2": r = restar(a, b)
    elif op == "3": r = multiplicar(a, b)
    elif op == "4":
        r = dividir(a, b)
        if r is None:
            print("No se puede dividir entre 0")
            continue
    else:
        print("Opción inválida"); continue
    print(f"Resultado: {r}")