from tasks import createTask, listTasks, changeStatus, getTask, deleteTask, getTaskByStatus, updateTask
from fileManager import DBTasks



def test_any_task():
    tasks = listTasks()
    assert tasks == []

def test_create_task():
    task = createTask(description="appending a task",status="todo")
    print(task)
    assert task["description"] == "appending a task"
    data = listTasks()
    assert data[-1] == task

def test_chance_status():
    # validate creation
    task = createTask(description="status changed",status="todo")
    assert task["description"] == "status changed"
    exists = getTask(task["id"])
    assert exists == task
    # validate update
    response = changeStatus(exists["id"], "in-progress")
    updated_task = getTask(exists["id"])
    assert response == "status was changed successfuly"
    assert updated_task["status"] == "in-progress"

def test_delete_task():
    # validate creation
    task = createTask(description="delete a task",status="done")
    assert task["description"] == "delete a task"
    isCreated = getTask(task["id"])
    assert isCreated == task
    # validate update
    response = deleteTask(isCreated["id"])
    assert response == "Task removed"
    tasks = listTasks()
    for _ in tasks:
        assert _["id"] != task["id"]

def test_get_filter():
    task = createTask(description="Create a container", status="todo")
    tasks_todo = getTaskByStatus("todo")
    print(tasks_todo)
    assert len(tasks_todo) == 2
    tasks_in_progress = getTaskByStatus("in-progress")
    assert len(tasks_in_progress) == 1

def test_update_task_description():
    # validate creation
    task = createTask(description="initial description", status="todo")
    assert task["description"] == "initial description"
    exists = getTask(task["id"])
    assert exists == task
    # validate update
    response = updateTask(task["id"], "updated description")
    updated_task = getTask(task["id"])
    assert response == "description was updated successfuly"
    assert updated_task["description"] == "updated description"

def test_update_task_not_found():
    response = updateTask("non-existent-id", "new description")
    assert response == "Task not found :C"

def test_change_status_not_found():
    response = changeStatus("non-existent-id", "done")
    assert response == "Task not found :C"

def test_delete_task_not_found():
    response = deleteTask("non-existent-id")
    assert response == "Task not found"

def test_get_task_not_found():
    task = getTask("non-existent-id")
    assert task == "Task not found"

def test_get_task_by_status_empty():
    tasks_done = getTaskByStatus("done")
    assert len(tasks_done) == 0

def test_create_multiple_tasks():
    task1 = createTask(description="Task 1", status="todo")
    task2 = createTask(description="Task 2", status="in-progress")
    task3 = createTask(description="Task 3", status="done")
    tasks = listTasks()
    assert task1 in tasks
    assert task2 in tasks
    assert task3 in tasks

def test_get_task_by_status_multiple():
    createTask(description="Task A", status="todo")
    createTask(description="Task B", status="todo")
    createTask(description="Task C", status="in-progress")
    tasks_todo = getTaskByStatus("todo")
    tasks_in_progress = getTaskByStatus("in-progress")
    for task in tasks_todo:
        assert task["status"] == "todo"
    for task in tasks_in_progress:
        assert task["status"] == "in-progress"

def test_create_and_delete_task():
    task = createTask(description="Temporary task", status="todo")
    assert task["description"] == "Temporary task"
    response = deleteTask(task["id"])
    assert response == "Task removed"
    tasks = listTasks()
    assert task not in tasks


