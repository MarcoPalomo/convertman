"""flask pour exposer en web app"""
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    #return "Super, on est en mode web app!"
    celsius = request.args.get("celsius", "")

    if celsius:
        fahrenheit = fahrenh_from(celsius)
    else:
        fahrenheit = ""

    return (
        """<form action="" method="get">
                Temperature en Celsius: <input type="text" name="celsius">
                <input type="submit" value="Convertir">
            </form>"""
        + "Cela fait en Fahrenheit: "
        + fahrenheit
    )

@app.route("/<int:celsius>")
#conversion C vers F pour la temperature"""
def fahrenh_from(celsius):
    """Convertir la temperature C vers F (degrees)."""
    try:
        fahrenh = float(celsius) * 9 / 5 + 32
        fahrenh = round(fahrenh, 4)  # arrondir a quatre decimales
        return str(fahrenh)
    except ValueError:
        return "erreur ! Entre un nombre"

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080, debug=True)
#    celsius = input("combien de Celsius: ")
#    print("il fait ", fahrenh_from(celsius) + " Farenheit")
