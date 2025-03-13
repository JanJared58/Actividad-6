def obtener_conjunto(mensaje):
    entrada = input(mensaje)
    conjunto = {int(elemento) for elemento in entrada.split()}
    return conjunto

conjunto1 = obtener_conjunto("Introduce los elementos del primer conjunto separados por espacios: ")
conjunto2 = obtener_conjunto("Introduce los elementos del segundo conjunto separados por espacios: ")

diferencia = conjunto1 - conjunto2

print("La diferencia entre los conjuntos es:", diferencia)