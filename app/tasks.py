from pymongo import MongoClient

class TaskManager:
    def __init__(self, mongo_uri='mongodb://mongo:27017/taskmanager'):
        self.client = MongoClient(mongo_uri)
        self.db = self.client.taskmanager
        self.tasks = self.db.tasks

    def create_task(self, title, description=None, due_date=None):
        task = {
            'title': title,
            'description': description,
            'due_date': due_date,
            'done': False
        }
        result = self.tasks.insert_one(task)
        task['id'] = str(result.inserted_id)
        return task

    def list_tasks(self, search_term=None, order_by=None):
        query = {}
        if search_term:
            query = {
                '$or': [
                    {'title': {'$regex': search_term, '$options': 'i'}},
                    {'description': {'$regex': search_term, '$options': 'i'}}
                ]
            }
        tasks = list(self.tasks.find(query))
        for task in tasks:
            task['id'] = str(task.pop('_id'))
        if order_by:
            tasks = sorted(tasks, key=lambda x: x.get(order_by, ''))
        return tasks

    def get_task(self, task_id):
        task = self.tasks.find_one({'_id': task_id})
        if task:
            task['id'] = str(task.pop('_id'))
        return task

    def mark_done(self, task_id):
        result = self.tasks.update_one({'_id': task_id}, {'$set': {'done': True}})
        if result.modified_count > 0:
            return self.get_task(task_id)
        return None
