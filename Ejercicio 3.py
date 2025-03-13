def obtener_lista(mensaje):
    entrada = input(mensaje)
    lista = entrada.split()
    return lista

lista = obtener_lista("Introduce los elementos de la lista separados por espacios: ")

conjunto = set(lista)

print("El conjunto resultante es:", conjunto) 