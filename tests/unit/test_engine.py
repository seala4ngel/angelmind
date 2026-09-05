import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from core.engine import ArsenalEngine

def test_engine_normalize():
    engine = ArsenalEngine()
    assert engine.normalize("example.com") == "https://example.com"
    assert engine.normalize("https://example.com") == "https://example.com"

def test_engine_request():
    engine = ArsenalEngine()
    resp = engine.request("https://httpbin.org/get")
    assert resp.status_code == 200
