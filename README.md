# To-Do List App

## Overview
The To-Do List App is a simple desktop application built using PyQt5. It allows users to add and delete tasks from a list, helping them keep track of their to-dos. This project demonstrates the basics of creating a graphical user interface (GUI) with PyQt5.

## Features
- Add new tasks to the list.
- Delete selected tasks from the list.
- Display the list of tasks in a scrollable view.
- Clear the input field after adding a task.

## Prerequisites
- Python 3.6
- PyQt5

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todo-app.git
    cd todo-app
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the project directory.
2. Run the application:
    ```bash
    python main.py
    ```

## Project Structure
todo_app/
├── README.md
├── LICENSE
├── main.py
├── requirements.txt
├── app/
│ ├── init.py
│ ├── main_window.py
│ ├── add_task.py
│ ├── delete_task.py
│ ├── task_list.py
└── tests/
├── init.py
├── test_add_task.py
├── test_delete_task.py
├── test_task_list.py


### File Descriptions

- **README.md**: Project overview and instructions.
- **LICENSE**: License for the project.
- **main.py**: The main entry point for the application.
- **requirements.txt**: List of dependencies required for the project.
- **app/__init__.py**: Initialization file for the app module, importing main components.
- **app/main_window.py**: Contains the main window class and application initialization.
- **app/add_task.py**: Contains the functionality for adding tasks.
- **app/delete_task.py**: Contains the functionality for deleting tasks.
- **app/task_list.py**: Contains the task list widget and related functions.
- **tests/__init__.py**: Initialization file for the tests module.
- **tests/test_add_task.py**: Unit tests for the add_task functionality.
- **tests/test_delete_task.py**: Unit tests for the delete_task functionality.
- **tests/test_task_list.py**: Unit tests for the task_list functionality.

## Code Explanation

### main.py

```python
import sys
from PyQt5.QtWidgets import QApplication
from app import ToDoApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
```
### init.py
```python
from .main_window import ToDoApp
from .add_task import add_task_functionality
from .delete_task import delete_task_functionality
from .task_list import TaskList
```
### main_window.py
```python
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
```
### add_task.py
```python
def add_task_functionality(app):
    task = app.input_field.text()
    if task:
        app.task_list.add_task(task)
        app.input_field.clear()
```
### delete_task.py
```python
from PyQt5.QtWidgets import QMessageBox

def delete_task_functionality(app):
    selected_items = app.task_list.selectedItems()
    if not selected_items:
        QMessageBox.warning(app, "Warning", "Please select a task to delete")
        return
    for item in selected_items:
        app.task_list.delete_task(item)
```
### task_list.py
```python
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
```
### Tests
To be implemented in the tests folder to ensure each functionality works correctly.

## Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.

## Licencse 
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
PyQt5 documentation: https://www.riverbankcomputing.com/static/Docs/PyQt5/
