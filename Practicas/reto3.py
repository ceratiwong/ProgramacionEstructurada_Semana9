# Datos globales
cola_pendientes = [
    {"id": 101, "nombre": "Ana"},
    {"id": 102, "nombre": "Luis"},
    {"id": 103, "nombre": "María"},
]
historial_pila = [{"id": 100, "nombre": "Carlos"}]

def cancelar_pendiente(id_solicitud):
    for i, registro in enumerate(cola_pendientes):
        if registro["id"] == id_solicitud:
            return cola_pendientes.pop(i)
    return None

# --- PRUEBA ---

print("Estado inicial de la cola:", cola_pendientes)

# 1. Cancelar una solicitud intermedia (ID 102)
cancelado = cancelar_pendiente(102)
print("\nElemento cancelado:", cancelado)
print("Cola tras cancelación (mantiene orden relativo):", cola_pendientes)

# 2. Intentar cancelar una solicitud ya atendida que está en el historial (ID 100)
cancelado_historial = cancelar_pendiente(100)
print("\nIntento de cancelar atendida (ID 100):", cancelado_historial)