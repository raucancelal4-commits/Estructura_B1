'''Ejercicio 4:  Convertir grados Celsius a Fahrenheit
1.- Entender el problema
Entrada:
Celsius (input)
Proceso
F= Celsius * 9 / 5 + 32 -> Una formula
Salida
Fahrenheit
2.- Bosquejo a mano 
Celsius = 25.5
Paso 1= F: 25.5 * 9 / 5 + 32 :77.9°F
3.- descubrir patrón
Hay 1 entrada y 1 salida, no hay bucles ni decisiones, como puede venir decimales 
como Celsius de 25.5 es válida por que utilizamos el float
4.- Código'''
celsius = float(input('Ingrese temperatura: '))
F = celsius * 9/5 + 32
print(f"La temperatura es: {F:.1f} °F")

'''Ejercicio 5: Segundos a horas, minutos y segundos. 
1.- Entender el problema
Entrada:
Total = (input)
Proceso
Horas = total // 3600
Resto = total % 3600
Minutos= resto //60
Segundos = resto % 60
Salida
hh:mm:ss
2.- Bosquejo a mano 
Total = 3725
Paso 1= horas = 3725 // 3600 = 1
Paso 2= resto = 3725 % 3600 = 125
Paso 3= minutos = 125 // 60 = 2
Paso 4= segundo = 125 % 60 = 5 
3.- descubrir patrón
Tiene 1 entrada y 1 salida; no utiliza bucles ni decisiones. Usa int porque los segundos se ingresan como números enteros.
4.- Código'''
total= int (input('Ingrese el total de segundos: '))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f"La hora es: {horas}:{minutos:02d}:{segundos:02d}")

'''Ejercicio 6: Intercambio de variable
1.- Entender el problema
Entrada:
a= (input), b = (input)
Proceso
a , b = b , a
Salida
a = a
b= b
2.- Bosquejo a mano 
a = 10 ; b = 5
a = 5 ; b = 10
3.- descubrir patrón
Tiene 2 entradas y 1 salida, no utiliza bucles ni decisiones, y realiza un intercambio de valores entre las variables a y b.
4.- Código'''
a = int(input('a: '))
b = int(input('b: '))
a, b = b , a
print(f"a: {a} y b: {b}")

'''Ejercicio 7: Calcular el Iva (15% Ecuador) 
1.- Entender el problema
Entrada:
Precio (input)
Proceso
iva= precio * 0.15
Total = precio + iva
Salida
Total del precio con iva
2.- Bosquejo a mano 
precio= 150
iva = 150 * 0.15 = 22.50
total = 150 + 22.50 = 172.50
3.- descubrir patrón
Tiene 1 entrada y 2 salidas: muestra el valor del IVA y el precio total con IVA. Utilizamos float porque el precio puede contener decimales y no hay condiciones ni bucles.
4.- Código'''
precio = float(input('Precio sin Iva: '))
IVA = 0.15
iva = precio * IVA
total = precio + iva 
print(f"Iva: {iva:.2f}")
print(f"EL total es: {total:.2f}")