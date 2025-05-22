import os

from flask import Flask, request, jsonify
from tasks import TaskManager

app = Flask(__name__)
mongo_uri = os.getenv('MONGO_URI', 'mongodb://mongo:27017/taskmanager')
task_manager = TaskManager(mongo_uri)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400
    task = task_manager.create_task(data['title'], data.get('description'), data.get('due_date'))
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def list_tasks():
    search_term = request.args.get('search')
    order_by = request.args.get('order_by')
    return jsonify(task_manager.list_tasks(search_term, order_by)), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_manager.get_task(task_id)
    if task:
        return jsonify(task), 200
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>/done', methods=['POST'])
def mark_done(task_id):
    task = task_manager.mark_done(task_id)
    if task:
        return jsonify(task), 200
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
