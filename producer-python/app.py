from flask import Flask, Response, request, jsonify
import json
from kafka import KafkaProducer
from application.models import db, migrate, User
from dotenv import load_dotenv
from sqlalchemy import exc
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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
migrate.init_app(app, db)

@app.route('/', methods=['GET'])
def home():
    return 'hello world'

@app.route('/user', methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
        email = request.form['email']
        if email:
            try:
                User.add_user(email)
                return Response("User added", 201, mimetype='application/json')
            except exc.IntegrityError:
                return Response('User with email %s already exists'%(email), status=200, mimetype='application/json')
    else:
        return jsonify({'User': User.get_all_users()})

@app.route('/user/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_put_delete_user(id): 
    if request.method == 'DELETE':
        User.delete_user(id)
        return Response("User deleted", 201, mimetype='application/json')
    elif request.method == 'GET': 
        return jsonify(User.get_user(id))

    elif request.method == 'PUT':
        email = request.form['email']
        user = User.update_user(id, email)

        return Response(jsonify(user), 200, mimetype='application/json')


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