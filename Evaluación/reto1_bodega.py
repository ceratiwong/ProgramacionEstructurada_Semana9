pila = []


def apilar(codigo):
    codigo = codigo.strip()

    if not codigo:
        print("Error: el código de la caja no puede estar vacío.")
        return

    if any(caja.casefold() == codigo.casefold() for caja in pila):
        print("Error: ya existe una caja con ese código.")
        return

    pila.append(codigo)
    print(f"Caja {codigo} apilada correctamente.")


def desapilar():
    if not pila:
        print("No se puede retirar: la pila está vacía.")
        return

    codigo = pila.pop()
    print(f"Caja retirada: {codigo}")


def consultar_tope():
    if not pila:
        print("La pila está vacía; no hay caja en el tope.")
        return

    print(f"Caja en el tope: {pila[-1]}")


def mostrar_pila():
    if not pila:
        print("\nLa pila está vacía.")
        print("Cantidad de cajas: 0\n")
        return

    ancho = max(len(codigo) for codigo in pila)
    ancho = max(ancho, len("TOPE"))
    borde = "+" + "-" * (ancho + 2) + "+"

    print("\n       TOPE")
    for codigo in reversed(pila):
        print(f"       {borde}")
        print(f"       | {codigo:^{ancho}} |")
        print(f"       {borde}")
    print("       BASE")
    print(f"Cantidad de cajas: {len(pila)}\n")


def mostrar_menu():
    print("=== SISTEMA DE CAJAS - BODEGA ===")
    print("1. Apilar caja")
    print("2. Desapilar caja")
    print("3. Consultar tope")
    print("4. Mostrar pila")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            apilar(input("Ingrese el código de la caja: "))
        elif opcion == "2":
            desapilar()
        elif opcion == "3":
            consultar_tope()
        elif opcion == "4":
            mostrar_pila()
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Seleccione del 1 al 5.")

main()
