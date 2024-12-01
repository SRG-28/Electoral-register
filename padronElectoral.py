# Padrón Electoral
nombres = []
cedulas = []
provincias = []
opcion = ""

while opcion != "5":
    print("\nBienvenido al padrón electoral")
    print("1. Agregar")
    print("2. Borrar")
    print("3. Mostrar")
    print("4. Modificar")
    print("5. Salir")
    opcion = input("Digite su opción: ")

    match opcion:
        case "1":  # Agregar
            nombre = input("Digite el nombre de la persona: ").upper()
            if nombre != "SALIR":
                cedula = int(input("Digite la cédula de la persona: "))
                provincia = input("Digite la provincia donde vive la persona: ").capitalize() #método de cadenas en Python que convierte la primera letra de la cadena a mayúscula y el resto a minúsculas
                nombres.append(nombre)
                cedulas.append(cedula)
                provincias.append(provincia)
                print(f"{nombre} agregado correctamente.")
        
        case "2":  # Eliminar
            nombre = input("Digite el nombre de la persona a eliminar: ").upper()
            if nombre in nombres:
                indice = nombres.index(nombre)
                nombres.pop(indice)
                cedulas.pop(indice)
                provincias.pop(indice)
                print(f"{nombre} eliminado correctamente.")
            else:
                print("No se encontró el nombre en el padrón, por favor verifique.")

        case "3":  # Mostrar
            if nombres:
                print("\nListado de personas en el padrón:")
                for i in range(len(nombres)):
                    print(f"Nombre: {nombres[i]}, Cédula: {cedulas[i]}, Provincia: {provincias[i]}")
            else:
                print("El padrón está vacío.")

        case "4":  # Modificar
            nombre = input("Digite el nombre de la persona a modificar: ").upper()
            if nombre in nombres:
                indice = nombres.index(nombre)
                cedulas[indice] = int(input("Digite la nueva cédula de la persona: "))
                provincias[indice] = input("Digite la nueva provincia donde vive la persona: ").capitalize()
                print(f"Datos de {nombre} actualizados correctamente.")
            else:
                print("No se encontró el nombre en el padrón, por favor verifique.")

        case "5":
            print("Hasta luego...")

        case _:
            print("Opción inválida. Intente nuevamente.")
