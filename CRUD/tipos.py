datos = ("a", "b", "a", "c")

print(list(datos))      # ['a','b','a','c']
print(tuple(datos))     # ('a','b','a','c')   -> la sello, ya no cambia
print(set(datos))       # {'a','b','c'}       -> pierdo orden y repetidos
print(sorted(set(datos)))                     # ['a','b','c'] sin repetidos y ordenado

print(dict(zip(("id", "nombre"), (1, "Ana"))))   # {'id':1, 'nombre':'Ana'}
print(list({"id": 1, "nombre": "Ana"}.items()))  # [('id',1), ('nombre','Ana')]