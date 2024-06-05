from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application info', version='1.0.3')
# Endpoint que devuelve "Hola Mundo"
@app.route('/')
@metrics.counter('hello_world_requests', 'Number of requests to hello_world endpoint')
def hello_world():
    return 'Hola Mundo!'

# Endpoint que devuelve un error
@app.route('/error')
@metrics.counter('error_requests', 'Number of requests to error endpoint')
def error():
    # Simulamos un error con un código de estado 500 (Internal Server Error)
    return jsonify({'error': 'Se ha producido un error'}), 500

# Endpoint que indica que el sitio está en mantenimiento
@app.route('/mantenimiento')
@metrics.counter('maintenance_requests', 'Number of requests to maintenance endpoint')
def mantenimiento():
    # Simulamos un mensaje de mantenimiento con un código de estado 503 (Service Unavailable)
    return jsonify({'mensaje': 'El sitio está en mantenimiento, vuelva más tarde'}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
