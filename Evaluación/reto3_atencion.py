from collections import deque


cola = deque()
siguiente_turno = 1


def registrar_cliente(nombre):
    global siguiente_turno

    nombre = nombre.strip()
    if not nombre:
        print("Error: el nombre del cliente no puede estar vacío.")
        return

    turno = siguiente_turno
    cola.append((turno, nombre))
    siguiente_turno += 1
    print(f"Turno {turno} registrado para {nombre}.")


def atender_cliente():
    if not cola:
        print("No hay clientes pendientes para atender.")
        return

    turno, nombre = cola.popleft()
    print(f"Atendiendo turno {turno}: {nombre}.")


def consultar_proximo():
    if not cola:
        print("No hay clientes pendientes; la cola está vacía.")
        return

    turno, nombre = cola[0]
    print(f"Próximo cliente: turno {turno}, {nombre}.")


def mostrar_clientes():
    if not cola:
        print("No hay clientes en espera; la cola está vacía.")
        return

    print("\nClientes en espera (primero en ser atendido a la izquierda):")
    print("FRENTE")
    for turno, nombre in cola:
        print(f"  [{turno}] {nombre}")
    print("FINAL")


def mostrar_pendientes():
    print(f"Cantidad de clientes pendientes: {len(cola)}")


def mostrar_menu():
    print("\n=== SISTEMA DE ATENCIÓN AL CLIENTE ===")
    print("1. Registrar turno")
    print("2. Atender al siguiente cliente")
    print("3. Consultar próximo cliente")
    print("4. Mostrar clientes en espera")
    print("5. Mostrar cantidad de pendientes")
    print("6. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_cliente(input("Nombre del cliente: "))
        elif opcion == "2":
            atender_cliente()
        elif opcion == "3":
            consultar_proximo()
        elif opcion == "4":
            mostrar_clientes()
        elif opcion == "5":
            mostrar_pendientes()
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Seleccione del 1 al 6.")


main()