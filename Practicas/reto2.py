# Datos globales
cola_pendientes = [{"id": 101, "nombre": "Ana"}, {"id": 102, "nombre": "Luis"}]
historial_pila = [{"id": 100, "nombre": "Carlos"}]


def buscar_solicitud(id_solicitud):
    # Busca en pendientes (sin modificar la cola)
    for registro in cola_pendientes:
        if registro["id"] == id_solicitud:
            return registro, "Pendientes"

    # Busca en historial (sin modificar la pila)
    for registro in historial_pila:
        if registro["id"] == id_solicitud:
            return registro, "Historial"

    return None


# --- PRUEBA CON ENTRADA DE USUARIO ---
id_ingresado = int(input("Ingresa el ID a buscar: "))
resultado = buscar_solicitud(id_ingresado)

print("Resultado:", resultado)