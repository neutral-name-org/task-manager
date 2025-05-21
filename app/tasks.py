class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def create_task(self, title):
        task = {
            'id': self.counter,
            'title': title,
            'done': False
        }
        self.tasks[self.counter] = task
        self.counter += 1
        return task

    def list_tasks(self):
        return list(self.tasks.values())

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def mark_done(self, task_id):
        task = self.tasks.get(task_id)
        if task:
            task['done'] = True
        return task
