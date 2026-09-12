def cal_area(base,altura):
    return base * altura 
print(cal_area(10,100))
print(cal_area(5,4.5))

def maximo(a,b,c):
    return max(a , b, c)
def maxino_manual(a,b,c):
    mayor = a
    if b > mayor : mayor = b
    if c > mayor : mayor = c
    return mayor 
print(maximo(10,100,-4))
print(maximo(-1,0,1))

def es_bisiesto(anio):
    divisible_4 = anio % 4 == 0
    divisible_100 = anio % 100 == 0
    divisible_400 = anio % 400 == 0
    return (divisible_4 and not divisible_100) or divisible_400
anio = int(input("Ingrese un año: "))
print(f"El año {anio} es bisiesto: {es_bisiesto(anio)}")

def es_bisiesto_corta(anio):
    return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)
print(es_bisiesto_corta(2024))
for y in [2024, 2025, 2014, 2004]:
    print(f"{y}: {es_bisiesto_corta(y)}")

def factorial (n):
    fact = 1
    for i in range (2, n +1):
        fact *= i
    return fact
def combinatorio(n,k):
    return factorial(n) // (factorial(k) * factorial( n - k))
print(factorial(5))
print(combinatorio(5,10))

def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        return None           
    return a / b
while True:
    print("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
    op = input("Opción: ")
    if op == "5":
        break
    a = float(input("a: "))
    b = float(input("b: "))
    if op == "1": r = sumar(a, b)
    elif op == "2": r = restar(a, b)
    elif op == "3": r = multiplicar(a, b)
    elif op == "4":
        r = dividir(a, b)
        if r is None:
            print("No se puede dividir entre 0")
            continue
    else:
        print("Opción inválida"); continue
    print(f"Resultado: {r}")