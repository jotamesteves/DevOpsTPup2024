from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint que devuelve "Hola Mundo"
@app.route('/')
def hello_world():
    return 'Hola Mundo!'

# Endpoint que devuelve un error
@app.route('/error')
def error():
    # Simulamos un error con un código de estado 500 (Internal Server Error)
    return jsonify({'error': 'Se ha producido un error'}), 500

# Endpoint que indica que el sitio está en mantenimiento
@app.route('/mantenimiento')
def mantenimiento():
    # Simulamos un mensaje de mantenimiento con un código de estado 503 (Service Unavailable)
    return jsonify({'mensaje': 'El sitio está en mantenimiento, vuelva más tarde'}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
