from flask import Flask, request, jsonify

app = Flask(__name__)

storage = {}

@app.route('/')
def home():
    return '✅ Cloud Data Store for Second Life is running.'

@app.route('/save', methods=['POST'])
def save():
    key = request.form.get('key')
    value = request.form.get('value')
    if not key or not value:
        return jsonify({"error": "Missing key or value"}), 400
    storage[key] = value
    return jsonify({"status": "ok", "saved": {key: value}})

@app.route('/fetch', methods=['GET'])
def fetch():
    key = request.args.get('key')
    if not key:
        return jsonify({"error": "Missing key"}), 400
    value = storage.get(key)
    if value is None:
        return jsonify({"error": "Key not found"}), 404
    return jsonify({"key": key, "value": value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
