'''Ejercicio 1: Saludo personalizado
1.- Entender el problema
Entrada:
Nombre = (input), Edad = (input)
Proceso
Concatenar el hola, con el nombre y la edad
Salida
El saludo completo
2.- Bosquejo a mano 
Nombre = “Ronny”, Edad = 18
Salida: Hola mi nombre es Ronny y tengo 18 años. Bienvenido al curso
3.- descubrir patrón
Hay solo un dato de entrada y no hay más que hacer cuentas solo formar un mensaje. 
Este es el patrón más simple leer -> mostrar
4.- Código'''
nombre = input('Ingrese su nombre: ')
edad = int (input('Ingrese su edad: '))
print(f"Hola mi nombre es {nombre} y tengo {edad} años, Bienvenido al curso.")

'''Ejercicio 2: Promedio de 3 notas
1.- Entender el problema
Entrada:
n1,n2,n3 (input)
Proceso
Sumar las 3 y dividir para 3
Salida
EL promedio
2.- Bosquejo a mano 
n1 = 8, n2=6, n3 = 10
Paso 1= sumo 8+6+10=24
Paso 2= divido 24/3= 8.0
Paso 3 = muestro “Promedio: 8.0”
3.- descubrir patrón
Tiene 2 pasos primero suma y después divide, el paréntesis obligatorio 
sin ellos solo se divide n3 para 3, El 3 no se lee es un valor fijo del problema 
(siempre son 3 notas),solo lee lo que el usuario decide. 
En Python / siempre da float (8.0, no 8). Perfecto el promedio casi siempre da decimales.
4.- Código'''
n1 = float(input('Nota 1: '))
n2= float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
promedio = ( n1 + n2 + n3 ) / 3
print(f"Promedio: {promedio:.1f}")
if promedio >= 7 : print("AProbado")
else : print("reprobado")

'''Ejercicio 3: Area y perimetro de un rectangulo.
1.- Entender el problema
Entrada:
Base,altura (input)
Proceso
Aplica 2 formulas
Salida
El área y el perimetro
2.- Bosquejo a mano 
Base = 5, altura= 3
Área = 5 * 3 = 15
Perímetro = 2 * (5 + 3) = 16
3.- descubrir patrón
2 entradas y 2 salidas, independientes cada formula usa base
Y altura por separado, no hay bucles ni decisiones.
Como pueden venir decimales (una base de .5 cm es valida),
Usamos el float
'''
import math
radio = int(input('Ingrese el radio: '))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio 
print(f"El area es: {area:.2f} y el perimetro es: {perimetro:.2f}")