from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton
from .task_list import TaskList
from .add_task import add_task_functionality
from .delete_task import delete_task_functionality

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 300)
        
        self.layout = QVBoxLayout()
        
        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.delete_button = QPushButton("Delete Task")
        self.task_list = TaskList()
        
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.task_list)
        
        self.add_button.clicked.connect(lambda: add_task_functionality(self))
        self.delete_button.clicked.connect(lambda: delete_task_functionality(self))
        
        self.setLayout(self.layout)
