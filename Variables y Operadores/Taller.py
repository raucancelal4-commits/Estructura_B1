'''Ejercicio 1: Descuento e IVA
1.- Entender el problema
Entrada:
Precio sin IVA (input)
Proceso
descuento = precio * 0.10 -> Calculamos el descuento
subtotal = precio - descuento -> Restamos el descuento al precio
iva = subtotal * 0.15 -> Calculamos el IVA
total = subtotal + iva -> Sumamos el IVA al subtotal
Salida
Descuento
IVA
Total a pagar
2.- Bosquejo a mano
precio = 100
Paso 1 = descuento: 100 * 0.10 = 10
Paso 2 = subtotal: 100 - 10 = 90
Paso 3 = iva: 90 * 0.15 = 13.50
Paso 4 = total: 90 + 13.50 = 103.50
3.- descubrir patrón
Hay 1 entrada y 3 salidas, no hay bucles ni decisiones, 
como puede venir decimales como precio de 100.50 es válida por que utilizamos el float
4.- Código'''
IVA = 0.15
DESCUENTO = 0.10
precio = float(input('Precio sin Iva: '))
descuento = precio * DESCUENTO
subtotal = precio - descuento
iva = subtotal * IVA
total = subtotal + iva
print(f"Descuento: ${descuento:.2f}")
print(f"IVA: ${iva:.2f}")
print(f"Total a pagar: ${total:.2f}")

'''Ejercicio 2: Número par, impar y múltiplos de 3 y 5
1.- Entender el problema
Entrada:
Número (input)
Proceso
resultado = "par" if num % 2 == 0 else "impar" -> Verificamos si el número es par o impar
Si num % 3 == 0 y num % 5 == 0 -> Es múltiplo de ambos
Si num % 3 == 0 -> Es múltiplo de 3
Si num % 5 == 0 -> Es múltiplo de 5
Si no cumple ninguna condición -> No es múltiplo de 3 ni de 5
Salida
Par o impar
Múltiplo de 3, 5 o de ambos
2.- Bosquejo a mano
num = 30
Paso 1 = 30 % 2 = 0 -> Es par
Paso 2 = 30 % 3 = 0 -> Es múltiplo de 3
Paso 3 = 30 % 5 = 0 -> Es múltiplo de 5
Resultado = 30 es par
Es múltiplo de ambos (3 y 5)
3.- descubrir patrón
Hay 1 entrada y 2 salidas, no hay bucles, como trabajamos con números enteros utilizamos el int, 
utilizamos decisiones if, elif y else para verificar si es par, impar o múltiplo de 3 y 5
4.- Código'''
num = int(input("Ingresa un número: "))
resultado = "par" if num % 2 == 0 else "impar"
print(f"{num} es {resultado}")
if num % 3 == 0 and num % 5 == 0:
    print('Es múltiplo de ambos (3 y 5)')
elif num % 3 == 0:
    print('Es múltiplo de 3')
elif num % 5 == 0:
    print('Es múltiplo de 5')
else:
    print('No es múltiplo ni de 3 ni de 5')

'''Ejercicio 3: Convertir hh:mm a segundos
1.- Entender el problema
Entrada:
Tiempo en hh:mm (input)
Proceso
partes = tiempo.split(":") -> Separamos las horas, minutos y segundos
horas = int(partes[0]) -> Convertimos las horas a entero
minutos = int(partes[1]) -> Convertimos los minutos a entero
segundos = int(partes[2]) -> Convertimos los segundos a entero
total = (horas * 3600) + (minutos * 60) + (segundos * 1) -> Convertimos todo a segundos
Salida
Total de segundos
2.- Bosquejo a mano
tiempo = 02:30:15
Paso 1 = horas: 2 * 3600 = 7200
Paso 2 = minutos: 30 * 60 = 1800
Paso 3 = segundos: 15 * 1 = 15
Paso 4 = total: 7200 + 1800 + 15 = 9015 segundos
3.- descubrir patrón
Hay 1 entrada y 1 salida, no hay bucles ni decisiones, como el tiempo viene en formato hh:mm utilizamos
el input y split para separar las horas,minutos y segundos, 
luego utilizamos el int para convertirlos en números enteros
4.- Código'''
tiempo = input("Ingrese hh:mm:ss: ")
partes = tiempo.split(":")
horas = int(partes[0] )
minutos = int(partes[1])
segundos = int(partes[2])
total = (horas * 3600) + (minutos * 60) + (segundos * 1)
print(total)

'''Ejercicio 4: Convertir un monto en billetes
1.- Entender el problema
Entrada:
Monto (input)
Proceso
resto = monto -> Guardamos el monto inicial
b50 = resto // 50 -> Calculamos los billetes de $50
b20 = resto // 20 -> Calculamos los billetes de $20
b10 = resto // 10 -> Calculamos los billetes de $10
b5 = resto // 5 -> Calculamos los billetes de $5
b1 = resto // 1 -> Calculamos los billetes de $1
Salida
Cantidad de billetes de $50
Cantidad de billetes de $20
Cantidad de billetes de $10
Cantidad de billetes de $5
Cantidad de billetes de $1
2.- Bosquejo a mano
monto = 187
Paso 1 = 187 // 50 = 3 billetes de $50
Resto = 187 % 50 = 37
Paso 2 = 37 // 20 = 1 billete de $20
Resto = 37 % 20 = 17
Paso 3 = 17 // 10 = 1 billete de $10
Resto = 17 % 10 = 7
Paso 4 = 7 // 5 = 1 billete de $5
Resto = 7 % 5 = 2
Paso 5 = 2 // 1 = 2 billetes de $1
3.- descubrir patrón
Hay 1 entrada y 5 salidas, no hay bucles ni decisiones, como trabajamos con un monto entero utilizamos el int, 
utilizamos // para saber cuántos billetes necesitamos y % para obtener el resto del monto
4.- Código'''
monto = int(input("Monto: $"))
resto = monto
b50 = resto // 50; resto = resto % 50
b20 = resto // 20; resto = resto % 20
b10 = resto // 10; resto = resto % 10
b5  = resto // 5;  resto = resto % 5
b1  = resto // 1;  resto = resto % 1
print(f"$50 × {b50}")
print(f"$20 × {b20}")
print(f"$10 × {b10}")
print(f"$5  × {b5}")
print(f"$1  × {b1}")

'''Ejercicio 5: Convertir un monto en monedas
1.- Entender el problema
Entrada:
Monto (input)
Proceso
resto = monto -> Guardamos el monto inicial
b025 = resto // 0.25 -> Calculamos las monedas de $0.25
b010 = resto // 0.10 -> Calculamos las monedas de $0.10
b005 = resto // 0.05 -> Calculamos las monedas de $0.05
b001 = resto // 0.01 -> Calculamos las monedas de $0.01
Salida
Cantidad de monedas de $0.25
Cantidad de monedas de $0.10
Cantidad de monedas de $0.05
Cantidad de monedas de $0.01
2.- Bosquejo a mano
monto = 0.87
Paso 1 = 0.87 // 0.25 = 3 monedas de $0.25
Resto = 0.87 % 0.25 = 0.12
Paso 2 = 0.12 // 0.10 = 1 moneda de $0.10
Resto = 0.12 % 0.10 = 0.02
Paso 3 = 0.02 // 0.05 = 0 monedas de $0.05
Paso 4 = 0.02 // 0.01 = 2 monedas de $0.01
3.- descubrir patrón
Hay 1 entrada y 4 salidas, no hay bucles ni decisiones, como el monto puede venir con decimales como 0.87 
es válido por que utilizamos el float,utilizamos // para saber cuántas monedas necesitamos 
y % para obtener el resto del monto
4.- Código'''
monto = float(input("Monto: $"))
resto = monto
b025  = resto // 0.25;  resto = resto % 0.25
b010  = resto // 0.10;  resto = resto % 0.10
b005  = resto // 0.05;  resto = resto % 0.05
b001  = resto // 0.01;  resto = resto % 0.01
print(f"$0.25  × {b025}")
print(f"$0.10  × {b010}")
print(f"$0.05  × {b005}")
print(f"$0.01  × {b001}")