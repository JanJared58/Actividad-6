def obtener_conjunto(mensaje):
    entrada = input(mensaje)
    conjunto = {int(elemento) for elemento in entrada.split()}
    return conjunto

def eliminar_elemento(conjunto, elemento):
    if elemento in conjunto:
        conjunto.remove(elemento)
        print(f"El elemento {elemento} ha sido eliminado del conjunto.")
    else:
        print(f"El elemento {elemento} no está presente en el conjunto.")
    return conjunto


conjunto = obtener_conjunto("Introduce los elementos del conjunto separados por espacios: ")
elemento = int(input("Introduce el elemento que deseas eliminar: "))

conjunto_actualizado = eliminar_elemento(conjunto, elemento)

print("El conjunto actualizado es:", conjunto_actualizado)
