def consultar_siguiente(cola):
    if not cola:
        return None
    return cola[0]


# --- PRUEBA ---
cola = [101, 102, 103]

print("Primera llamada:", consultar_siguiente(cola))
print("Segunda llamada:", consultar_siguiente(cola))
print("Longitud de la cola:", len(cola))