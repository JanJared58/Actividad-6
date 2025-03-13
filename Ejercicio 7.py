texto = input("Introduce el texto o párrafo: ")

puntuaciones = ['.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '-', '_', '"', "'"]

for puntuacion in puntuaciones:
    texto = texto.replace(puntuacion, "")

palabras = texto.lower().split()

frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print("Frecuencia de las palabras en el texto:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")