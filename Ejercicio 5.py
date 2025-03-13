def obtener_consonantes(cadena):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    conjunto_consonantes = set()
    for letra in cadena:
        if letra in consonantes:
            conjunto_consonantes.add(letra)
    return conjunto_consonantes

cadena = input("Introduce una cadena: ")
resultado = obtener_consonantes(cadena)
print("Las consonantes presentes en la cadena son:", resultado)