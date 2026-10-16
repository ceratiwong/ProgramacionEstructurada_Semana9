import os

from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

# Clave para desarrollo local.
app.config["SECRET_KEY"] = os.environ.get(
    "FLASK_SECRET_KEY",
    "clave-temporal-solo-para-desarrollo"
)

# Constantes de configuración
MAX_CAPACITY = 100
MAX_ITEM_LENGTH = 120

# Estado en memoria (cada elemento es un diccionario con 'text' e 'image')
stack = []
capacity = None


# ---------- Operaciones de la pila ----------

def is_empty(items):
    """Indica si la pila está vacía."""
    return len(items) == 0


def push(item_text, image_data):
    """Agrega un elemento con su imagen si hay capacidad."""
    if capacity is None:
        return False, "Primero debes configurar la capacidad de la pila."

    if not image_data:
        return False, "Es obligatorio tomar una foto antes de apilar el elemento."

    if len(item_text) > MAX_ITEM_LENGTH:
        return False, f"El elemento no puede superar {MAX_ITEM_LENGTH} caracteres."

    if len(stack) >= capacity:
        return False, "La pila está llena. No se agregó el elemento."

    stack.append({
        "text": item_text,
        "image": image_data
    })
    return True, f"Se agregó «{item_text}» con su fotografía a la pila."


def pop_item():
    """Retira y devuelve el elemento superior."""
    if is_empty(stack):
        return False, "La pila está vacía."

    item = stack.pop()
    return True, f"Se retiró «{item['text']}» de la pila."


def peek():
    """Consulta el elemento superior sin eliminarlo."""
    if is_empty(stack):
        return False, "La pila está vacía."

    return True, f"Elemento superior: «{stack[-1]['text']}»"


def len_stack():
    """Devuelve la cantidad de elementos de la pila."""
    return len(stack)


# ---------- Ruta principal ----------

@app.route("/", methods=["GET", "POST"])
def index():
    global capacity

    if request.method == "POST":
        action = request.form.get("action", "").strip()

        if action == "configure":
            raw_capacity = request.form.get("capacity", "").strip()

            try:
                new_capacity = int(raw_capacity)
                if not 1 <= new_capacity <= MAX_CAPACITY:
                    raise ValueError
            except ValueError:
                flash(
                    f"Ingresa un número entero entre 1 y {MAX_CAPACITY}.",
                    "danger"
                )
            else:
                capacity = new_capacity
                stack.clear()
                flash(f"Pila configurada para {capacity} elementos.", "success")

        elif action == "push":
            item_text = request.form.get("item", "").strip()
            image_data = request.form.get("image_data", "").strip()

            if capacity is None:
                flash("Primero debes configurar la capacidad de la pila.", "warning")
            elif not item_text:
                flash("Escribe un elemento antes de apilarlo.", "warning")
            elif not image_data:
                flash("Debes tomar una foto antes de apilar el elemento.", "danger")
            else:
                success, message = push(item_text, image_data)
                flash(message, "success" if success else "danger")

        elif action == "pop":
            success, message = pop_item()
            flash(message, "success" if success else "warning")

        elif action == "peek":
            success, message = peek()
            flash(message, "info" if success else "warning")

        elif action == "clear":
            stack.clear()
            flash("La pila se vació correctamente.", "info")

        else:
            flash("La operación solicitada no es válida.", "danger")

        return redirect(url_for("index"))

    return render_template(
        "index.html",
        stack=list(stack),
        capacity=capacity,
        count=len_stack(),
        top=stack[-1] if stack else None
    )


if __name__ == "__main__":
    app.run(debug=True)