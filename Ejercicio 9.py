sinonimos = {
    "rápido": ["veloz", "ligero", "expedito"],
    "feliz": ["contento", "alegre", "jovial"],
    "triste": ["melancólico", "apesadumbrado", "afligido"],
    "inteligente": ["listo", "brillante", "perspicaz"],
    "fuerte": ["robusto", "resistente", "vigoroso"]
}

def buscar_sinonimos(palabra):
    if palabra in sinonimos:
        return sinonimos[palabra]
    else:
        return "No se encontraron sinónimos para la palabra dada."

palabra = input("Introduce una palabra para buscar sus sinónimos: ")

resultado = buscar_sinonimos(palabra)
print(f"Sinónimos de '{palabra}': {resultado}")


print("\nClaves del diccionario de sinónimos:")
for clave in sinonimos.keys():
    print(clave)