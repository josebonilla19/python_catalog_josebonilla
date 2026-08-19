Catalogo_jugadores = {
    "Lamine": {"club": "FC Barcelona", "posicion": "Delantero", "dorsal": 10},
    "Rodri": {"club": "FC Barcelona", "posicion": "Centrocampista", "dorsal": 16},
    "Anthony Gordon": {"club": "FC Barcelona", "posicion": "Delantero", "dorsal": 25},
}


def agregar_elemento():
    nombre = input("Nombre del jugador: ")
    club = input("Club: ")
    posicion = input("Posicion: ")
    dorsal = int(input("Dorsal: "))
    Catalogo_jugadores[nombre] = {"club": club, "posicion": posicion, "dorsal": dorsal}
    print("Jugador agregado con exito.")


while True:
    print("\nCatalogo de jugadores")
    print("1. Ver todos los elementos")
    print("2. Agregar un elemento")
    print("3. Modificar un elemento")
    print("4. Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        print("Opcion todavia no disponible")
    elif opcion == "2":
        agregar_elemento()
    elif opcion == "3":
        print("Opcion todavia no disponible")
    elif opcion == "4":
        print("Hasta luego")
        break
    else:
        print("Opcion invalida")

Catalogo_jugadores = {
    "Lamine": {"club": "FC Barcelona", "posicion": "Delantero", "dorsal": 10},
    "Rodri": {"club": "FC Barcelona", "posicion": "Centrocampista", "dorsal": 16},
    "Anthony Gordon": {"club": "FC Barcelona", "posicion": "Delantero", "dorsal": 25},
}


def agregar_elemento():
    nombre = input("Nombre del jugador: ")
    club = input("Club: ")
    posicion = input("Posicion: ")
    dorsal = int(input("Dorsal: "))
    Catalogo_jugadores[nombre] = {"club": club, "posicion": posicion, "dorsal": dorsal}
    print("Jugador agregado con exito.")


def ver_todos():
    for nombre, datos in Catalogo_jugadores.items():
        print("\nJugador:", nombre)
        for atributo, valor in datos.items():
            print(" -", atributo, ":", valor)


while True:
    print("\n--- Catalogo de jugadores ---")
    print("1. Ver todos los elementos")
    print("2. Agregar un elemento")
    print("3. Modificar un elemento")
    print("4. Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        ver_todos()
    elif opcion == "2":
        agregar_elemento()
    elif opcion == "3":
        print("Opcion todavia no disponible")
    elif opcion == "4":
        print("Hasta luego")
        break
    else:
        print("Opcion invalida")

Catalogo_jugadores = {
    "Lamine": {"club": "FC Barcelona", "posicion": "Delantero", "dorsal": 10},
    "Rodri": {"club": "FC Barcelona", "posicion": "Centrocampista", "dorsal": 16},
    "Anthony Gordon": {"club": "FC Barcelona", "posicion": "Delantero", "dorsal": 25},
}


def agregar_elemento():
    nombre = input("Nombre del jugador: ")
    club = input("Club: ")
    posicion = input("Posicion: ")
    dorsal = int(input("Dorsal: "))
    Catalogo_jugadores[nombre] = {"club": club, "posicion": posicion, "dorsal": dorsal}
    print("Jugador agregado con exito.")


def ver_todos():
    for nombre, datos in Catalogo_jugadores.items():
        print("\nJugador:", nombre)
        for atributo, valor in datos.items():
            print(" -", atributo, ":", valor)


def modificar_elemento():
    nombre = input("Nombre del jugador a modificar: ")
    if nombre in Catalogo_jugadores:
        print("Atributos actuales:", Catalogo_jugadores[nombre])
        atributo = input("Que atributo desea modificar (club/posicion/dorsal): ")
        if atributo in Catalogo_jugadores[nombre]:
            nuevo_valor = input("Nuevo valor: ")
            if atributo == "dorsal":
                nuevo_valor = int(nuevo_valor)
            Catalogo_jugadores[nombre][atributo] = nuevo_valor
            print("Elemento modificado con exito.")
        else:
            print("Ese atributo no existe.")
    else:
        print("Ese jugador no esta en el catalogo.")


while True:
    print("\n--- Catalogo de jugadores ---")
    print("1. Ver todos los elementos")
    print("2. Agregar un elemento")
    print("3. Modificar un elemento")
    print("4. Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        ver_todos()
    elif opcion == "2":
        agregar_elemento()
    elif opcion == "3":
        modificar_elemento()
    elif opcion == "4":
        print("Hasta luego")
        break
    else:
        print("Opcion invalida")