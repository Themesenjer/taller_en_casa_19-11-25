from flask import Flask, jsonify

app = Flask(__name__)

# Creamos una ruta simple para la suma para simular un servicio
@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    """
    Realiza la suma de dos números enteros.
    Endpoint de prueba para el despliegue Swarm.
    """
    resultado = num1 + num2
    return jsonify({
        "servicio": "Calculadora Pablo",
        "operacion": "Suma",
        "numero1": num1,
        "numero2": num2,
        "resultado": resultado
    })

@app.route('/')
def home():
    """Ruta principal simple."""
    return "¡Servicio de Calculadora de Pablo Reyes funcionando! Prueba /suma/5/3"

if __name__ == '__main__':
    # Flask debe escuchar en el puerto 8080
    app.run(debug=True, host='0.0.0.0', port=8080)