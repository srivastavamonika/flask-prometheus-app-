from flask import Flask, Response
from prometheus_client import generate_latest, Counter

app = Flask(__name__)

# Define a Prometheus counter metric
REQUEST_COUNT = Counter('my_requests_total', 'Total HTTP Requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()  # increment on each request
    return "Hello from Flask App with Prometheus!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001)
