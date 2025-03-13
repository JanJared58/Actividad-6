def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado exitosamente.")

def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        print(f"El número de teléfono de {nombre} es {agenda[nombre]}.")
    else:
        print(f"El contacto {nombre} no se encuentra en la agenda.")

def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado exitosamente.")
    else:
        print(f"El contacto {nombre} no se encuentra en la agenda.")

def gestionar_agenda():
    agenda = {}
    while True:
        print("\n1. Agregar contacto\n2. Buscar contacto\n3. Eliminar contacto\n4. Ver todos los contactos\n5. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Introduce el nombre del contacto: ")
            telefono = input("Introduce el número de teléfono del contacto: ")
            agregar_contacto(agenda, nombre, telefono)
        elif opcion == "2":
            nombre = input("Introduce el nombre del contacto a buscar: ")
            buscar_contacto(agenda, nombre)
        elif opcion == "3":
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            eliminar_contacto(agenda, nombre)
        elif opcion == "4":
            print("\nContactos en la agenda:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
        elif opcion == "5":
            print("Saliendo del programa de gestión de agenda.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

gestionar_agenda()
