def registrar_puntajes():
    puntajes = {}
    while True:
        nombre = input("Introduce el nombre del jugador (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        puntaje = int(input(f"Introduce el puntaje de {nombre}: "))
        puntajes[nombre] = puntaje
    return puntajes

def imprimir_puntajes(puntajes):
    print("\nPuntajes de los jugadores:")
    for nombre, puntaje in puntajes.items():
        print(f"{nombre}: {puntaje}")

puntajes = registrar_puntajes()

imprimir_puntajes(puntajes)