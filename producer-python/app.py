from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from kafka import KafkaConsumer, KafkaProducer
app = Flask(__name__)
TOPIC_NAME = "test"
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers = KAFKA_SERVER,
    api_version = (0, 11, 15)
)

@app.route('/', methods=['GET'])
def home():
    return 'hola modificado'

@app.route('/python', methods=['GET'])
def index():
    response = {'language': 'python', 'is': 'awesome'}

    json_payload = json.dumps(response)
    json_payload = str.encode(json_payload)

    print(json_payload)

    # push data into INFERENCE TOPIC
    producer.send(TOPIC_NAME, json_payload)
    producer.flush()
    print("Sent to consumer")
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port = 5000)