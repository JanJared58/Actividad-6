def obtener_conjunto(mensaje):
    entrada = input(mensaje)
    conjunto = {int(elemento) for elemento in entrada.split()}
    return conjunto

conjunto = obtener_conjunto("Introduce los elementos del conjunto separados por espacios (o deja vacío para un conjunto vacío): ")

if not conjunto:
    print("El conjunto está vacío")
else:
    print("El conjunto no está vacío y contiene los siguientes elementos:", conjunto)
