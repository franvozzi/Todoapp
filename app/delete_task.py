from PyQt5.QtWidgets import QMessageBox

def delete_task_functionality(app):
    selected_items = app.task_list.selectedItems()
    if not selected_items:
        QMessageBox.warning(app, "Warning", "Please select a task to delete")
        return
    for item in selected_items:
        app.task_list.delete_task(item)
