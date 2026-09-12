Mensaje = input('Frase: ').lower()
vocal = "aeiouAEIOU"
ttal = 0
for sh in Mensaje:
    if sh in vocal:
        ttal += 1
print(f"{ttal} Vocales.")

notas= [7, 8.5, 6, 9, 10, 5.5]
promedio= sum(notas) /len(notas)
Maximo = print(f"Maximo es: {max(notas):.2f}")
Minimo = print(f"Minimo es: {min(notas):.2f}")

ordena = ["a", "b", "a", "c", "b", "d"]
sin_repetir = sorted(set(ordena))
print(sin_repetir)

texto = input("Frase: ")
conteo = {}
for palabra in texto.split() :
    conteo[palabra]= conteo.get(palabra, 0)+1
print(conteo) 
mas = max(conteo, key = conteo.get)
print(f"Mas repetida: '{mas}' ({conteo[mas]} veces)")