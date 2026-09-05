from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/api/run', methods=['POST'])
def run_module():
    data = request.json
    module = data.get('module')
    target = data.get('target')
    if not module or not target:
        return jsonify({'error': 'module and target required'}), 400
    result = subprocess.run(
        ["python3", "run.py", "--module", module, "--target", target],
        capture_output=True, text=True
    )
    return jsonify({'output': result.stdout, 'error': result.stderr})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
