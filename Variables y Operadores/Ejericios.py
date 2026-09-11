numero = int(input('Ingrese 3 digitos: '))
centena = numero // 100
decena = (numero // 10) % 10
unidad = numero % 10
suma = centena + decena + unidad
print(f"La suma es: {suma}")

total = int(input('Ingrese minutos: '))
horas = total // 60
minutos = total % 60
print(f'{horas} horas {minutos} minutos')

peso = int (input('Peso (Kg): '))
estatura = float(input('Estatura (m): '))
imc = peso / (estatura ** 2)
print(f'IMC es: {imc:.2f}')

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