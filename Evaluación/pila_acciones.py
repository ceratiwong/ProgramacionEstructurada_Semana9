
acciones = []
 
def registrar_accion(descripcion):
    acciones.append(descripcion)
    print("Acción registrada:", descripcion)
 
def deshacer():
    if not acciones:
        print("No existen acciones para deshacer")
        return
    ultima = acciones.pop()
    print("Se deshizo:", ultima)
 
def historial():
    print("Acciones pendientes:", acciones)
 
registrar_accion("Escribir título")
registrar_accion("Agregar párrafo")
registrar_accion("Cambiar formato")
historial()
deshacer()
historial()
