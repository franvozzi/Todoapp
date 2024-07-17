import sys
from PyQt5.QtWidgets import QApplication
from app.main_window import ToDoApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
