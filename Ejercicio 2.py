def es_subconjunto(conjunto1, conjunto2):
    for elemento in conjunto1:
        if elemento not in conjunto2:
            return False
    return True

def obtener_conjunto(mensaje):
    entrada = input(mensaje)
    conjunto = {int(elemento) for elemento in entrada.split()}
    return conjunto

conjunto1 = obtener_conjunto("Introduce los elementos del primer conjunto separados por espacios: ")
conjunto2 = obtener_conjunto("Introduce los elementos del segundo conjunto separados por espacios: ")

if es_subconjunto(conjunto1, conjunto2):
    print("El primer conjunto es subconjunto del segundo conjunto")
else:
    print("El primer conjunto no es subconjunto del segundo conjunto")
