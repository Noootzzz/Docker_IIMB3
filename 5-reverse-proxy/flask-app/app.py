from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def index():
    return jsonify({"service": "Flask API", "message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

