clientes = ["Ana", "Luis", "Sol"]

# --- AGREGAR ---
clientes.append("Marco")          # al final       -> ['Ana','Luis','Sol','Marco']
clientes.insert(1, "Beto")        # en la posición 1
clientes.extend(["Iván", "Ruth"]) # varios de una vez

# --- QUITAR ---
clientes.remove("Beto")   # por valor (error si no existe)
ultimo = clientes.pop()   # saca y devuelve el último  <- esto es una PILA
primero = clientes.pop(0) # saca el primero            <- esto es una COLA

# --- CONSULTAR ---
print(len(clientes))            # cuántos hay
print(clientes[0], clientes[-1])# primero y último
print("Ana" in clientes)        # True/False
print(clientes.index("Sol"))    # en qué posición está
print(clientes.count("Ana"))    # cuántas veces aparece

# --- RECORRER ---
for nombre in clientes:
    print(nombre)

for posicion, nombre in enumerate(clientes):   # cuando necesito el índice
    print(posicion, nombre)

# --- ORDENAR ---
clientes.sort()                       # modifica la lista original
copia_ordenada = sorted(clientes)     # deja la original intacta
clientes.sort(reverse=True)           # de Z a A

# --- TRANSFORMAR (list comprehension) ---
mayusculas = [n.upper() for n in clientes]
con_a      = [n for n in clientes if n.startswith("A")]   # filtrar
longitudes = [len(n) for n in clientes]

# --- ACUMULAR ---
notas = [18, 15, 20, 12]
print(sum(notas), max(notas), min(notas), sum(notas) / len(notas))