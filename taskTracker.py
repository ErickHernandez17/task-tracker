import argparse

from tasks import createTask, listTasks, changeStatus, getTask, deleteTask, getTaskByStatus, updateTask

def main():
    parser = argparse.ArgumentParser(description='A simple CLI tool for task tracking.')
    parser.add_argument("-c", "--create", nargs=2, type=str, help="Crea una nueva tarea: [descripcion] [status]")
    parser.add_argument("-l","--list", action="store_true", help="List all tasks.")
    parser.add_argument("-g", "--get", type=str, help="Get a task by ID.")
    parser.add_argument("-d", "--delete", type=str, help="Delete a task by ID.")
    parser.add_argument("-s", "--status", nargs=2,type=str, help="Change the status of a task by ID. [id] [status]")
    parser.add_argument("-u", "--update", nargs=2, type=str, help="Update a task by ID: [id] [description]")
    parser.add_argument("-f", "--filter", type=str, help="Get tasks by status.")
    parser.add_argument("-md","--markdone", type=str, help="Mark task as done. [id]")
    parser.add_argument("-mt","--marktodo", type=str, help="Mark task as todo. [id]")
    parser.add_argument("-mi", "--markinprogress", type=str, help="Mark task as in progress. [id]")

    args = parser.parse_args()

    if args.create:
        # Call the function to create a task
        task = createTask(args.create[0], args.create[1])
        print(f"Task create with ID: {task['id']}")
        # You can add your task creation logic here
    if args.list:
        # Call the function to list tasks
        tasks = listTasks()
        print("Tasks:")
        for task in tasks:
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
        # You can add your task listing logic here
    if args.get:
        # Call the function to get a task by ID
        task = getTask(args.get)
        if task != "Task not found":
            print(task)
        else:
            print("Task not found")
    if args.delete:
        # Call the function to delete a task by ID
        result = deleteTask(args.delete)
        if result != "Task not found":
            print(result)
        else:
            print("Task not found")
    if args.status:
        # Call the function to change the status of a task by ID
        result = changeStatus(args.status[0], args.status[1])
        if result != "Task not found":
            print(result)
        else:
            print("Task not found")
    if args.update:
        # Call the function to update a task by ID
        result = updateTask(args.update[0], args.update[1])
        if result != "Task not found":
            print(result)
        else:
            print("Task not found")
    if args.filter:
        # Call the function to get tasks by status
        tasks = getTaskByStatus(args.filter)
        if tasks:
            print("Filtered Tasks:")
            for task in tasks:
                print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
        else:
            print("No tasks found with the specified status.")
    if args.markdone:
        # Call the function to mark a task as done
        result = changeStatus(args.markdone, "done")
        if result != "Task not found":
            print(result)
        else:
            print("Task not found")
    if args.marktodo:
        # Call the function to mark a task as todo
        result = changeStatus(args.marktodo, "todo")
        if result != "Task not found":
            print(result)
        else:
            print("Task not found")
    if args.markinprogress:
        # Call the function to mark a task as in progress
        result = changeStatus(args.markinprogress, "in progress")
        if result != "Task not found":
            print(result)
        else:
            print("Task not found")

if __name__ == "__main__":
    main()