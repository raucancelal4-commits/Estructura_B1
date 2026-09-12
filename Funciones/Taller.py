'''def calcular_iva(precio):
    return precio * 0.15
def calcular_total(precio):
    iva = calcular_iva(precio)
    return precio + iva
precio = float(input("Precio: $"))
total = calcular_total(precio)
print(f"Total con IVA: ${total:.2f}")

def contar_primos(a, b):
    cantidad = 0
    for num in range(a, b + 1):
        es_primo = True
        if num < 2:
            es_primo = False
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            cantidad += 1
    return cantidad
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
resultado = contar_primos(a, b)
print(f"Hay {resultado} números primos entre {a} y {b}")

def es_narcisista(n):
    digitos = str(n)
    cantidad = len(digitos)
    suma = 0
    for digito in digitos:
        suma += int(digito) ** cantidad
    return suma == n
n = int(input("Ingrese un número: "))
if es_narcisista(n):
    print("Es un número narcisista")
else:
    print("No es un número narcisista")
'''
b = int(input('Numero: '))
d =int(input('Otro numero: '))
def suma():
    return b + d
def dividir():
    return b / d
def resta():
    return b - d
def multiplicacion():
    return b * d
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Dividir")
    print("3. Resta")
    print("4. Multiplicación")
    print("5. Salir")
while True:
        mostrar_menu()
        opcion = input("Opción: ")
        if opcion == "1":
            print("Resultado es: ",suma())
        elif opcion == "2":
            print("Resultado es: ",dividir())
        elif opcion == "3":
            print("Resultado es: ", resta())
        elif opcion == "4":
            print("El resultado es: ", multiplicacion())
        elif opcion == "5":
            print("Adios, Chao")
            break
        else:
            print("Opción inválida")