from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
import subprocess

app = Flask(__name__)

# Swagger
SWAGGER_URL = '/api/docs'
API_URL = '/api/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/api/swagger.json')
def swagger():
    return jsonify({
        "openapi": "3.0.0",
        "info": {"title": "Arsenal Apik API", "version": "3.0"},
        "paths": {
            "/api/run": {
                "post": {
                    "summary": "Run a module",
                    "parameters": [{"in": "body", "name": "body", "schema": {"type": "object"}}],
                    "responses": {"200": {"description": "OK"}}
                }
            }
        }
    })

# ... (endpoint lain sama kayak sebelumnya)
