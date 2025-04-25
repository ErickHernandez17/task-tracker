from uuid import uuid4
from datetime import datetime
from fileManager import DBTasks

file = DBTasks()

def fastSearch(task_id:str) -> dict:
    data = file.get_data()
    hash_map = {}
    for n in range(len(data["tasks"])):
        task_data = data["tasks"][n]
        task_data["n"] = n
        hash_map[data["tasks"][n]["id"]] = task_data
    coincidences = []
    for key, value in hash_map.items():
        if task_id in key:
            coincidences.append(key)
    if len(coincidences) == 0:
        return "Task not found"
    elif len(coincidences) > 1:
        return "More than one task found"
    return coincidences[0]
    

def createTask(description:str, status:str)  -> str:
    task = {
        "id": str(uuid4()),
        "description": description,
        "status": status,
        "createdAt": str(datetime.now())
    }
    file = DBTasks()
    file.append(task)
    return task


def listTasks() -> list:
    data = file.get_data()
    return data["tasks"]


def getTask(id:str):
    data = file.get_data()
    id_str = fastSearch(id)
    if id_str == "Task not found": return id_str
    if id_str == "More than one task found": return id_str
    for task in data["tasks"]:
        if task["id"] == id_str:
            return task
    return "Task not found"


def changeStatus(id:str, new_status:str):
    #print("input",id,new_status)
    data = file.get_data()
    tasks = data["tasks"]
    id_str = fastSearch(id)
    if id_str == "Task not found": return id_str
    if id_str == "More than one task found": return id_str
    task = None
    for n in range(len(tasks)):
        if tasks[n]["id"] == id_str:
            tasks[n]["status"] = new_status
            tasks[n]["updatedAt"] = str(datetime.now())
            task = tasks[n]
            file.update(n, task)
            return "status was changed successfuly"
    return "Task not found :C"


def updateTask(id:str, description:str):
    data = file.get_data()
    tasks = data["tasks"]
    id_str = fastSearch(id)
    if id_str == "Task not found": return id_str
    if id_str == "More than one task found": return id_str
    for n in range(len(tasks)):
        if tasks[n]["id"] == id_str:
            tasks[n]["description"] = description
            tasks[n]["updatedAt"] = str(datetime.now())
            task = tasks[n]
            file.update(n, task)
            return "description was updated successfuly"
    return "Task not found :C"
    

def deleteTask(id:str):
    data = file.get_data()
    tasks = data["tasks"]
    id_str = fastSearch(id)
    if id_str == "Task not found": return id_str
    if id_str == "More than one task found": return id_str
    for n in range(len(tasks)):
        if tasks[n]["id"] == id_str:
            file.delete(n)
            return "Task removed"
    return "Task not found"


def getTaskByStatus(status:str) -> list:
    data = file.get_data()
    #print("data: ",data)
    tasks_filtered = list(filter(lambda a: a["status"] == status, data["tasks"]))
    #print("tasks_filtered",tasks_filtered)
    return tasks_filtered

