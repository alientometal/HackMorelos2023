import conekta
from flask import Flask, render_template, request


#insancia api
api = conekta.Conekta(
    merchant_id="YOUR_MERCHANT_ID",
    public_key="YOUR_PUBLIC_KEY",
    private_key="YOUR_PRIVATE_KEY",
)

#código de pago
charge = api.create_charge(
    amount=1000,
    description="Compra de producto",
    payment_method="oxxopay",
)

# estado de pago
charge = api.get_charge(charge.id)


app = Flask(__name__)


@app.route("/")
def index():
    if request.method == "POST":
        # Obtiene los datos del pago
        monto = float(request.form["monto"])
        descripcion = request.form["descripcion"]

        # Genera un código de pago OxxoPay
        charge = api.create_charge(
            amount=monto,
            description=descripcion,
            payment_method="oxxopay",
        )

        # Envía el código de pago al cliente
        return render_template("index.html", charge=charge)

    return render_template("index.html")

@app.route("/status/<charge_id>")
def status(charge_id):
    # Obtener el estado del pago
    charge = api.get_charge(charge_id)

    return render_template("status.html", charge=charge)

if __name__ == "__main__":
    app.run(debug=True)