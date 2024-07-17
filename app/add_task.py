def add_task_functionality(app):
    task = app.input_field.text()
    if task:
        app.task_list.add_task(task)
        app.input_field.clear()
