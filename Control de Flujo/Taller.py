'''Ejercicio 1: Conteo regresivo
1. Entender el problema
Entrada: Número entero n desde el cual iniciar la cuenta regresiva.
Proceso: Iterar desde el número N hasta 1 usando un paso negativo (-1).
Salida: Cada número impreso en orden descendente.
2. Bosquejo a mano 
n = 3 
Vuelta 1: Imprime 3 Siguiente i = 2 
Vuelta 2: Imprime 2 Siguiente i = 1
Vuelta 3: Imprime 1 Término del ciclo
Resultado: 3, 2, 1
3. Descubrir patrón
Uso de range(inicio, fin, paso). El límite final debe ser 0 
no incluyente para que llegue hasta 1, con paso -1.
4. Código'''
n = int(input('N: '))
for i in range(n, 0, -1):
    print(i)

'''Ejercicio 2: Suma de pares entre 2 y 100
1. Entender el problema
Entrada: Ninguna (rango fijo definido en el sistema).
Proceso: Recorrer los números pares del 2 al 100 e ir acumulando su suma.
Salida: La suma total calculada.
2. Bosquejo a mano
Vuelta 1 (a = 2): suma = 0 + 2 = 2
Vuelta 2 (a = 4): suma = 2 + 4 = 6
Vuelta 3 (a = 6): suma = 6 + 6 = 12 
... hasta 100.
Resultado esperado: Suma total 2550.
3. Descubrir patrón
Acumulador: La variable suma incrementa progresivamente con el 
valor actual de $a$. El range(2, 101, 2) avanza con paso de $2$ para saltar de un par a otro.
4. Código'''
suma = 0                   
for a in range(2, 101, 2):
    suma = suma + a        
print(f"Suma: {suma}")

'''Ejercicio 3: Factorial de un número
1. Entender el problema
Entrada: Un número entero s.
Proceso: Multiplicar consecutivamente todos los números desde 1 hasta s.
Salida: El valor del factorial (s!).
2. Bosquejo a mano (s = 4)
Vuelta 1 (i = 1): fact = 1 * 1 = 1
Vuelta 2 (i = 2): fact = 1 * 2 = 2
Vuelta 3 (i = 3): fact = 2 * 3 = 6
Vuelta 4 (i = 4): fact = 6 * 4 = 24
Resultado esperado: 4! = 24.
3. Descubrir patrón
Productorio: La variable fact inicia en 1 (neutro multiplicativo) y en 
cada paso se actualiza como fact * i.
4. Código'''
s = int(input("N: "))
fact = 1                  
for i in range(1, s + 1):
    fact = fact * i
print(f"{s}! = {fact}")

'''Ejercicio 4: Porcentaje de estudiantes aprobados
1. Entender el problema
Entrada: Cantidad total de estudiantes y la nota de cada uno.
Proceso: Evaluar cada nota; si es mayor o igual a 7, suma al contador de aprobados,
de lo contrario al de reprobados. Al final se calcula el porcentaje de aprobados.
Salida: Porcentaje de aprobados redondeado a 2 decimales.
2. Bosquejo a mano(est = 2, notas: 8 y 5)
Estudiante 1 (nota = 8): 8 >= 7 aprobados = 1
Estudiante 2 (nota = 5): 5 < 7 reprobados = 1
Cálculo: (1 / 2) * 100 = 50.0 %
Resultado esperado: Aprobados: 50.0%
3. Descubrir patrón
Contadores condicionales: Incremento con += 1 según el resultado del if.
4. Código'''
est = int(input("¿Cuántos estudiantes? "))
aprobados = 0  
reprobados = 0 
for i in range(est):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:                 
        aprobados += 1 
    else:
        reprobados += 1
porcentaje = round((aprobados / est) * 100, 2)
print(f'Aprobados: {porcentaje}%')

'''Ejercicio 5: Menor nota ingresada
1. Entender el problema
Entrada: Cantidad de notas y el valor de cada nota.
Proceso: Comparar cada nota ingresada contra una variable bandera menor 
inicializada en infinito positivo (float("inf")).
Salida: La menor nota de la serie.
2. Bosquejo a mano (n = 2, notas: 8.5 y 6.0)
Inicio: menor = ∞
Nota 1 (8.5): 8.5 < ∞ -> menor = 8.5
Nota 2 (6.0): 6.0 < 8.5 -> menor = 6.0
Resultado esperado: Menor: 6.0
3. Descubrir patrón
Patrón del Mínimo: Cualquier valor real ingresado será siempre menor que ∞, 
garantizando que la primera nota sea asignada correctamente sin importar su valor.
4. Código'''
n = int(input("¿Cuántas notas? "))
menor = float("inf")             
for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota < menor:               
        menor= nota              
print(f"Menor: {menor}")

'''Ejercicio 6: Números primos entre 2 y 100
1. Entender el problema
Entrada: Rango implícito entre 2 y 100.
Proceso: Comprobar para cada número si tiene algún divisor
en el rango desde 2 hasta num - 1. Si no tiene divisores, es primo.
Salida: Lista con todos los números primos encontrados.
2. Bosquejo a mano (num = 4)
Probando divisores para 
4: i = 2 -> 4 \% 2 == 0 -> es_primo = False -> break
Resultado para 4: No se añade a la lista.
3. Descubrir patrón
Bucle anidado con interrupción temprana: El bucle interno busca si existe residuo
cero (% == 0). Al encontrar el primer divisor se cancela con break para ahorrar cómputo.
4. Código'''
primos = []  
for num in range(2, 101):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False 
            break  
    if es_primo:
        primos.append(num)
print("Números primos entre 2 y 100:")
print(primos)