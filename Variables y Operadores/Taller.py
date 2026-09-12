
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


tiempo = input("Ingrese hh:mm:ss: ")
partes = tiempo.split(":")
horas = int(partes[0] )
minutos = int(partes[1])
segundos = int(partes[2])
total = (horas * 3600) + (minutos * 60) + (segundos * 1)
print(total)


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