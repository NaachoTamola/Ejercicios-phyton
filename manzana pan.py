from flask import Flask, render_template, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambia esto por una clave segura

# Diccionario de productos
productos = {
    "manzana": {"precio": 1.5, "imagen": "manzana.png"},
    "pan": {"precio": 2.0, "imagen": "pan.png"}
}

# Función auxiliar para obtener el carrito (usando la sesión)
def obtener_carrito():
    if "cart" not in session:
        session["cart"] = {}
    return session["cart"]

def calcular_total(carrito):
    total = 0
    for producto, cantidad in carrito.items():
        total += productos[producto]["precio"] * cantidad
    return total

@app.route("/")
def index():
    carrito = obtener_carrito()
    total = calcular_total(carrito)
    return render_template("index.html", productos=productos, cart=carrito, total=total)

@app.route("/agregar/<producto>")
def agregar_producto(producto):
    carrito = obtener_carrito()
    if producto in carrito:
        carrito[producto] += 1
    else:
        carrito[producto] = 1
    session["cart"] = carrito  # Actualizamos la sesión
    return redirect(url_for("index"))

@app.route("/vaciar")
def vaciar_carrito():
    session["cart"] = {}
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
