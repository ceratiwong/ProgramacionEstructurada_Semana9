cola = []

def encolar(queue, element):
    queue.append(element)

def desencolar(queue):
    if len(queue) == 0:
        return None
    return queue.pop(0)

def esta_vacia(queue):
    if len(queue) == 0:
        print("La cola está vacía")
        return True
    print("La cola no está vacía")
    return False

def mostrar_cola(queue):
    return str(queue)

def menu():
    while True:
        try:
            print("\n--- Menú de la Cola ---")
            print("1. Encolar")
            print("2. Desencolar")
            print("3. Mostrar Cola")
            print("4. Verificar si está vacía")
            print("5. Salir del programa")
            opc = int(input("Seleccione una opción: "))
            if opc == 1:
                elemento = input("Ingrese el elemento a encolar: ")
                if elemento == "":
                    print("Error. No ingresó ningún elemento.")
                else:
                    encolar(cola, elemento)
                    print(f"Elemento '{elemento}' encolado.")
            elif opc == 2:
                elemento_desencolado = desencolar(cola)
                if elemento_desencolado is None:
                    print("La cola está vacía. No se puede desencolar.")
                else:
                    print(f"Elemento '{elemento_desencolado}' desencolado.")
            elif opc == 3:
                print("Elementos en cola:", mostrar_cola(cola))
            elif opc == 4:
                esta_vacia(cola)
            elif opc == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Opción fuera de rango. Seleccione un número entre 1 y 5.")
        except ValueError:
            print("Valor no válido. Ingrese un valor entero.")

def main():
    menu()

main()