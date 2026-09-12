n = int(input('N: '))
for i in range(n, 0, -1):
    print(i)

suma = 0                   
for a in range(2, 101, 2):
    suma = suma + a        
print(f"Suma: {suma}")

s = int(input("N: "))
fact = 1                  
for i in range(1, s + 1):
    fact = fact * i
print(f"{s}! = {fact}")

est = int(input("¿Cuántos estudiantes? "))
aprobados = 0  
reprobados = 0 
for i in range(est):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:                 
        aprobados += 1 
    else:
        reprobados += 1
porcentaje = round((aprobados / est) * 100, 2)
print(f'Aprobados: {porcentaje}%')

n = int(input("¿Cuántas notas? "))
menor = float("inf")             
for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota < menor:               
        menor= nota              
print(f"Menor: {menor}")

primos = []  
for num in range(2, 101):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False 
            break  
    if es_primo:
        primos.append(num)
print("Números primos entre 2 y 100:")
print(primos)