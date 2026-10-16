pila = []
 
def apilar(libro):
    pila.append(libro)
    print(f"Libro agregado: {libro}")
 
def desapilar():
    if len(pila) == 0:
        print("La pila está vacía")
    else:
        libro = pila.pop()
        print(f"Libro retirado: {libro}")
 
def mostrar_pila():
        if not pila:
            print("No hay libros")
        else:
            print("Pila actual:", pila)
            print("Libro en el tope:", pila[-1])
 
apilar("Matemáticas")
apilar("Programación")
apilar("Base de Datos")
mostrar_pila()
desapilar()
mostrar_pila()

"""¿Qué libro se retira primero? ¿Por qué?
El primer libro que se retira es Base de Datos, porque las pilas utilizan el principio LIFO 
que significa que el último elemento en entrar es el primero en salir, ya que  Base de Datos fue el último libro agregado
está en el tope de la pila y se tiene que retira primero.
¿Qué sucede cuando se intenta retirar de una pila vacía?
Cuando se intenta retirar un libro de una pila vacía, el programa verifica si su longitud es igual a cero mediante if len(pila) == 0:
Si se cumple la condición, muestra el mensaje "La pila está vacía" y no ejecuta pop(), evitando un error al intentar retirar un elemento inexistente."""