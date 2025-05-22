class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def create_task(self, title, description=None, due_date=None):
        task = {
            'id': self.counter,
            'title': title,
            'description': description,
            'due_date': due_date,
            'done': False
        }
        self.tasks[self.counter] = task
        self.counter += 1
        return task

    def list_tasks(self, search_term=None, order_by=None):
        tasks = self.tasks.values()
        if search_term:
            tasks = [task for task in tasks if search_term.lower() in task['title'].lower() or (task['description'] and search_term.lower() in task['description'].lower())]
        if order_by:
            tasks = sorted(tasks, key=lambda x: x.get(order_by, ''))
        return list(tasks)

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def mark_done(self, task_id):
        task = self.tasks.get(task_id)
        if task:
            task['done'] = True
        return task
