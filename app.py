#!flask/bin/python
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy food',
        'description': u'Milk, Orange Juice, Pizza',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Flask',
        'description': u'Read the flask docs',
        'done': False
    }
]

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)