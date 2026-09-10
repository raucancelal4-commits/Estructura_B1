
celsius = float(input('Ingrese temperatura: '))
F = celsius * 9/5 + 32
print(f"La temperatura es: {F:.1f} °F")

total= int (input('Ingrese el total de segundos: '))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f"La hora es: {horas}:{minutos:02d}:{segundos:02d}")

a = int(input('a: '))
b = int(input('b: '))
a, b = b , a
print(f"a: {a} y b: {b}")

precio = float(input('Precio sin Iva: '))
IVA = 0.15
iva = precio * IVA
total = precio + iva 
print(f"Iva: {iva:.2f}")
print(f"EL total es: {total:.2f}")