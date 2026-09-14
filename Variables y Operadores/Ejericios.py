'''Ejercicio 6: Suma de dígitos de un número de 3 cifras
1.- Entender el problema
Entrada: Un número entero de 3 dígitos (input).
Proceso:
centena = numero // 100 -> Extrae el primer dígito usando división entera.
decena = (numero // 10) % 10 -> Quita el último dígito y saca el residuo para obtener el del medio.
unidad = numero % 10 -> Extrae el último dígito usando el operador residuo (módulo).
suma = centena + decena + unidad -> Suma los tres dígitos extraídos.
Salida: La suma de los tres dígitos.
2.- Bosquejo a mano
numero = 584
Paso 1 (Centena): 584 // 100 = 5
Paso 2 (Decena): 584 // 10 = 58 -> 58 % 10 = 8
Paso 3 (Unidad): 584 % 10 = 4
Paso 4 (Suma): 5 + 8 + 4 = 17
Resultado esperado: "La suma es: 17"
3.- Descubrir patrónHay 1 entrada entera (int) y 1 salida. No se usan decisiones ni bucles. 
El patrón principal es el uso de operadores aritméticos de división entera (//) y 
módulo (%) para descomponer un número posicionalmente.
4.- Código

'''
numero = int(input('Ingrese 3 digitos: '))
centena = numero // 100
decena = (numero // 10) % 10
unidad = numero % 10
suma = centena + decena + unidad
print(f"La suma es: {suma}")

'''Ejercicio 7: Conversión de minutos a horas y minutos
1.- Entender el problema
Entrada: Cantidad total de minutos en valor entero (input).
Proceso:horas = total // 60 -> Divide el total entre 60 para saber cuántas horas completas hay.
minutos = total % 60 -> Obtiene el residuo de la división para saber cuántos minutos sobran.
Salida: Las horas completas y los minutos restantes.
2.- Bosquejo a mano
total = 135
Paso 1 (Horas): 135 // 60 = 2
Paso 2 (Minutos): 135 % 60 = 15
Resultado esperado: "2 horas 15 minutos"
3.- Descubrir patrón
Hay 1 entrada y 2 datos de salida formateados en una sola línea. No hay bucles ni condicionales. 
Es una conversión de tiempo basada en un sistema sexagesimal (base 60) usando división exacta y residuos
4.- Código'''
total = int(input('Ingrese minutos: '))
horas = total // 60
minutos = total % 60
print(f'{horas} horas {minutos} minutos')

'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
1.- Entender el problema
Entrada: Peso en kilogramos (int) y estatura en metros (float).
Proceso:imc = peso / (estatura ** 2) -> Divide el peso entre la estatura elevada al cuadrado.
Salida: El valor del IMC formateado con dos decimales.
2.- Bosquejo a manopeso = 70, estatura = 1.75
Paso 1 (Estatura al cuadrado): 1.75 ** 2 = 3.0625
Paso 2 (Dividir peso): 70 / 3.0625 = 22.8571...
Resultado esperado: "IMC es: 22.86"
3.- Descubrir patrónHay 2 entradas de tipos mixtos (int y float) y 1 salida decimal. 
Aplica una fórmula matemática directa. Se utiliza el formato de cadena :.2f 
para redondear visualmente la salida a 2 decimales sin alterar el valor matemático de la variable.
4.- Código'''
peso = int (input('Peso (Kg): '))
estatura = float(input('Estatura (m): '))
imc = peso / (estatura ** 2)
print(f'IMC es: {imc:.2f}')

'''Ejercicio 9: Redondeo personalizado de decimales
1.- Entender el problema
Entrada: Un número decimal (float) y la cantidad de decimales deseada (int).
Proceso:
resultado = round(num, dec) -> Utiliza la función nativa de Python para 
redondear el número flotante a los dígitos indicados.
Salida: 
El número ya redondeado.
2.- Bosquejo a manonum = 5.6789, dec = 2
Paso 1 (Redondear): round(5.6789, 2) = 5.68
Resultado esperado: 5.68
3.- Descubrir patrón
Tiene 2 entradas (float e int) y una salida de precisión variable. El patrón consiste en usar 
la función incorporada round(), la cual altera directamente el valor de la variable flotante
según el parámetro de precisión entregado por el usuario.
4.- Código'''
num = float(input("Número: "))
dec = int(input("Decimales: "))
resultado = round(num, dec)
print(resultado)


PRECIO = 12
cant = int(input("Cantidad: "))
if cant >= 10:
    descuento = 0.15
elif cant >= 5:
    descuento = 0.05
else:
    descuento = 0
subtotal = PRECIO * cant
total = subtotal * (1 - descuento)
print(f"Precio unitario: ${PRECIO}")
print(f"Descuento: {int(descuento*100)}%")
print(f"Total: ${total:.2f}")