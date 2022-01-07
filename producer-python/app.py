from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def index():
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
  app.run()