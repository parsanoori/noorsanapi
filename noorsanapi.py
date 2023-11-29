from flask import Flask, jsonify, request
import random
import string
import time

app = Flask(__name__)

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def random_unix_time():
    return int(time.time()) - random.randint(1, 365) * 24 * 60 * 60

def random_positive_integer(digits):
    return random.randint(10 ** (digits - 1), 10 ** digits - 1)

@app.route('/credittotoken', methods=['POST'])
def credittotoken():
    token_id = request.json.get('tokenid', '')

    response_data = {
        "company": random_string(5),
        "technology": random_string(5),
        "device": random_string(5),
        "carbon_value": random_string(5),
        "carbon_type": random_string(5),
        "project_name": random_string(5),
        "registry_address": random_string(5),
        "credit_id": random_string(5),
        "retired_date": random_unix_time(),
        "energy": random_positive_integer(3),
        "standard": "noorsan" if token_id.startswith("1402") else random_string(5)
    }

    return jsonify(response_data)

@app.route('/approveco2', methods=['POST'])
def approveco2():
    token_id = request.json.get('tokenid', '')
    standard = request.json.get('standard', '')

    if standard == "noorsan" and token_id.startswith("1402"):
        return jsonify(result=True)
    else:
        return jsonify(result=False)

if __name__ == '__main__':
    app.run()

