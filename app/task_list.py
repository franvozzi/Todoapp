from PyQt5.QtWidgets import QListWidget

class TaskList(QListWidget):
    def __init__(self):
        super().__init__()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.addItem(task)
    
    def delete_task(self, item):
        self.tasks.remove(item.text())
        self.takeItem(self.row(item))
