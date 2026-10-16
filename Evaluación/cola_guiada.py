
from collections import deque
 
cola = deque()
 
def registrar_paciente(nombre):
    cola.append(nombre)
    print(f"Registrado: {nombre}")
 
def atender_paciente():
    if not cola:
        print("No hay pacientes en espera")
    else:
        paciente = cola.popleft()
        print(f"Atendiendo a: {paciente}")
 
def mostrar_cola():
    if not cola:
        print("La cola está vacía")
    else:
        print("Pacientes en espera:")
        for posicion, paciente in enumerate(cola, 1):
            print(f"{posicion}. {paciente}")
 
registrar_paciente("Ana")
registrar_paciente("Luis")
registrar_paciente("María")
mostrar_cola()
atender_paciente()
mostrar_cola()
