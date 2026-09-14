'''Ejercicio 1: Tabla de multiplicar de un número
1.- Entender el problema
Entrada: Un número entero n (int).Proceso:Utilizar un ciclo for que itera 
consecutivamente desde el 1 hasta el 12.En cada repetición, multiplicar n 
por el número de la iteración actual (i).
Salida: La tabla de multiplicar formateada línea por línea.
2.- Bosquejo a mano
n = 5
Vuelta 1 (i = 1): 5 × 1 = 5
Vuelta 2 (i = 2): 5 × 2 = 10(...así sucesivamente hasta llegar al 12...)
Vuelta 12 (i = 12): 5 × 12 = 60
Resultado esperado: 12 líneas impresas en pantalla mostrando la tabla del 5.
3.- Descubrir patrón
Tiene 1 entrada y 12 salidas impresas. El patrón consiste en un bucle de 
rango fijo determinado (for i in range(1, 13)) que actúa como un contador 
indexado para automatizar operaciones de producto aritmético escalonado.
4.- Código'''
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

'''Ejercicio 3: Separación y suma de números pares e impares
1.- Entender el problema
Entrada: Un número entero n que indica cuántos valores se van a evaluar, 
seguido por los n números individuales.
Proceso:Se crean dos variables acumuladoras en cero: suma_pares y suma_impares.
Se abre un ciclo for que se repite n veces para capturar cada número (x).
Para cada número se evalúa el residuo entre 2 (x % 2 == 0). 
Si es verdadero se suma a los pares, si no, a los impares.
Salida: La suma acumulada final de los números pares y los impares por separado.
2.- Bosquejo a mano
n = 3 (Se van a ingresar 3 números)
Número 1: x = 4 ➔ Par ➔ suma_pares = 4
Número 2: x = 7 ➔ Impar ➔ suma_impares = 7
Número 3: x = 2 ➔ Par ➔ suma_pares = 4 + 2 = 6
Resultado esperado: "Suma de pares: 6", "Suma de impares: 7"
3.- Descubrir patrón
Tiene múltiples entradas dinámicas y 2 salidas. El patrón combina un bucle iterativo 
con lectura incremental de datos dinámicos (input interno) controlado por 
condiciones lógicas internas de clasificación estadística simultánea (acumuladores condicionales).
4.- Código'''
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

'''Ejercicio 4: Validación de rango de edad
1.- Entender el problema
Entrada: Valores enteros para la edad (int).
Proceso:Se inicia un bucle infinito que solicita la edad de manera persistente.
Se utiliza un condicional compuesto encadenado (0 <= edad <= 120) para evaluar 
si el número ingresado se encuentra dentro del rango biológico admisible.
Si está en rango, se ejecuta un break para romper el bucle. De lo contrario, 
se despliega una alerta.
Salida: Confirmación de la edad una vez validada con éxito.
2.- Bosquejo a mano
Intento 1: edad = 150 ➔ No cumple rango ➔ Muestra "Error, intenta de nuevo"
Intento 2: edad = -5 ➔ No cumple rango ➔ Muestra "Error, intenta de nuevo"
Intento 3: edad = 21 ➔ Cumple rango ➔ Ejecuta break y sale.
Resultado esperado: "Edad válida: 21"
3.- Descubrir patrón
Tiene entradas indefinidas y una salida controlada. El patrón implementa el 
mecanismo estándar de asertividad o sanitización de datos de usuario (Data Validation) 
mediante bucles de captura indefinidos, garantizando la integridad de los datos antes 
de que pasen al flujo principal del sistema.
4.- Código'''
while True:
    edad = int(input("Edad (0-120): "))
    if 0 <= edad <= 120:
        break                       
    print("Error, intenta de nuevo")
print(f"Edad válida: {edad}")

'''Ejercicio 5: Juego de adivinanza numérica (Mayor o menor)
1.- Entender el problema
Entrada: Números enteros provistos como intentos de adivinanza por el usuario (int).
Proceso:La computadora genera un número aleatorio oculto (random.randint).Un ciclo 
indefinido lee las propuestas del usuario y mantiene un contador de intentos incremental.
Se evalúan tres caminos condicionales: si es idéntico (gana y finaliza), si el secreto 
es mayor o si el secreto es menor, guiando al usuario con pistas lógicas.
Salida: Mensajes de guía o pistas conductuales y la cantidad final de intentos al acertar.
2.- Bosquejo a mano
secreto = 42 (Generado por la PC de forma aleatoria)
Intento 1: intento = 50 ➔ ¿50 == 42? No. ¿50 < 42? No. ➔ Imprime "Es menor"
Intento 2: intento = 30 ➔ ¿30 == 42? No. ¿30 < 42? Sí. ➔ Imprime "Es mayor"
Intento 3: intento = 42 ➔ ¿42 == 42? Sí. ➔ Imprime "¡Correcto en 3 intentos!"
Resultado esperado: Dinámica interactiva de aproximación numérica por pistas.
3.- Descubrir patrónEmplea la librería externa pseudoaleatoria (random) vinculada a un patrón 
de búsqueda interactiva binaria empírica. El sistema refina la toma de decisiones utilizando 
condicionales relacionales compuestos por exclusión mutua (if-elif-else).0
4.- Código'''
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

'''Ejercicio 6: Serie matemática de Fibonacci
1.- Entender el problema
Entrada: Cantidad de elementos n que se desean calcular y proyectar de la serie (int).
Proceso:Se inicializan los dos primeros valores bases de la serie: a = 0 y b = 1.
Se corre un ciclo for que iterará exactamente n veces.
En cada repetición se imprime el valor actual de a de manera horizontal (end=" ") y se actualizan
los valores de forma simultánea: a toma el valor de b, mientras b toma la suma algebraica de los 
dos anteriores (a + b).
Salida: La secuencia numérica lineal de los términos de Fibonacci solicitados.
2.- Bosquejo a mano
n = 4
Vuelta 1: Imprime a (0) ➔ Nuevos valores: a = 1, b = (0 + 1) = 1
Vuelta 2: Imprime a (1) ➔ Nuevos valores: a = 1, b = (1 + 1) = 2
Vuelta 3: Imprime a (1) ➔ Nuevos valores: a = 2, b = (1 + 2) = 3
Vuelta 4: Imprime a (2) ➔ Nuevos valores: a = 3, b = (2 + 3) = 5
Resultado esperado: 0 1 1 2 
3.- Descubrir patrón
Tiene 1 entrada y una secuencia de salida continua. El patrón radica en el uso de la asignación 
múltiple simultánea o empaquetamiento de tuplas en Python (a, b = b, a + b), lo cual permite 
modificar estados de variables concurrentes en memoria sin requerir de variables temporales auxiliares.
4.- Código'''
n = int(input("¿Cuántos? "))
a, b = 0, 1                      
for _ in range(n):               
    print(a, end=" ")
    a, b = b, a + b  
print()                       