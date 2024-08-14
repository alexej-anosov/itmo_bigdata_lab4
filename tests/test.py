import requests
import glob
import time
import pytest
import json


def wait_until_active(max_attempts=10, url='http://0.0.0.0:8000/health'):
    for attempt in range(max_attempts):
        try:
            print(f"Attempt {attempt + 1}: Trying to connect...")
            if requests.get(url).ok:
                return True
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    return False


@pytest.fixture(autouse=True)
def setup_and_teardown():
    assert wait_until_active(), "Failed to connect to the server after multiple attempts"
    print("Connected successfully")
    yield


def test_json_file(url='http://0.0.0.0:8000/request/'):
    headers = {'Content-Type': 'application/json'}
    for json_file_path in glob.glob("../tests/*.json"):          
        with open(json_file_path, 'r') as json_file:
            X, y = json.load(json_file)
        response = requests.post(url, json=X, headers=headers)
        assert response.ok, f"Request failed for file {json_file_path}"
        assert response.json() == y, f"Prediction is not correct for file {json_file_path}: {response.json()} != {y} "

