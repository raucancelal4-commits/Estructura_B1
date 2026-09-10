nombre = input('Ingrese su nombre: ')
edad = int (input('Ingrese su edad: '))
print(f"Hola mi nombre es {nombre} y tengo {edad} años, Bienvenido al curso.")

n1 = float(input('Nota 1: '))
n2= float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
promedio = ( n1 + n2 + n3 ) / 3
print(f"Promedio: {promedio:.1f}")
if promedio >= 7 : print("AProbado")
else : print("reprobado")

import math
radio = int(input('Ingrese el radio: '))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio 
print(f"El area es: {area:.2f} y el perimetro es: {perimetro:.2f}")