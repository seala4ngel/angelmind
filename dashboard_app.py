from flask import Flask, send_file, render_template_string, jsonify, request
import subprocess
import json
import os

app = Flask(__name__)

# ========== ROUTE UTAMA ==========
@app.route('/')
def index():
    # LANGSUNG NAMPILIN dashboard_pro_v2.html
    return send_file('dashboard_pro_v2.html')

# ========== API ==========
@app.route('/api/modules')
def list_modules():
    modules = [
        'subhunter', 'portprobe', 'fingerprint',
        'sqli', 'xss', 'ssrf', 'ssti', 'graphql',
        'deser', 'authbypass', 'chain', 'vulntrigger',
        'misconfig', 'leakscan', 'bucketscan',
        'webfuzz', 'apifuzz',
        'implant', 'beacon',
        'privesc', 'lateral', 'cleanup', 'persist',
        'phishing', 'exploit_payload',
        'weaponize', 'diff', 'crash',
        'mailcraft', 'pretext'
    ]
    return jsonify({'modules': modules})

@app.route('/api/run', methods=['POST'])
def run_module():
    data = request.json
    module = data.get('module')
    target = data.get('target')
    if not module or not target:
        return jsonify({'error': 'module and target required'}), 400
    try:
        result = subprocess.run(
            ['python3', 'run.py', '--module', module, '--target', target],
            capture_output=True, text=True, timeout=180
        )
        output = result.stdout or result.stderr
        try:
            return jsonify(json.loads(output))
        except:
            return jsonify({'output': output[:500]})
    except subprocess.TimeoutExpired:
        return jsonify({'error': f'Module "{module}" timed out after 180 seconds'}), 408
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/beacons')
def get_beacons():
    try:
        with open('beacons.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except:
        return jsonify({})

@app.route('/api/c2/start', methods=['POST'])
def start_c2():
    subprocess.Popen(['python3', '-c', 'from modules.c2.listener import app; app.run(host="0.0.0.0", port=8080)'], shell=True)
    return jsonify({'message': 'C2 started on port 8080'})

@app.route('/api/c2/stop', methods=['POST'])
def stop_c2():
    subprocess.run(['pkill', '-f', 'modules.c2.listener'], capture_output=True)
    return jsonify({'message': 'C2 stopped'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
