from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from kafka import KafkaConsumer, KafkaProducer
from application.models import db, migrate
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

TOPIC_NAME = "test"
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers = KAFKA_SERVER,
    api_version = (0, 11, 15)
)

POSTGRES = {
    'user': os.getenv("POSTGRES_USER"),
    'pw': 'postgres',
    'db': os.getenv("POSTGRES_DB"),
    'host': os.getenv("POSTGRES_HOSTNAME"),
    'port': os.getenv("POSTGRES_PORT"),
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
migrate.init_app(app, db)

@app.route('/', methods=['GET'])
def home():
    return 'hola'

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