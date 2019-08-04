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
    return "<h1>Welcome to my New Flask App</h1>"

@app.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not Found'}), 404)