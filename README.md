# Task Tracker

Task Tracker is a simple and efficient command-line tool to manage your tasks. It allows you to create, update, delete, and filter tasks based on their status.

## Features

- Add new tasks with descriptions and statuses.
- Update task descriptions or statuses.
- Delete tasks by their unique ID.
- Filter tasks by their status (e.g., "todo", "in-progress", "done").
- View all tasks in the system.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ErickHernandez17/task-tracker.git
   ```
2. Add the path of the repository to your PATH system.
3. Now execute `taskTracker.py --help` in the console to view all options.

## Usage
Open a terminal and navigate to the directory where the repository is located. Use the following command to see all available options:
``` bash
python [taskTracker.py](http://_vscodecontentref_/0) --help
```

Example Commands
- Create a new task:
``` bash 
python taskTracker.py create --description "Finish project report" --status "todo" 
```
- List all tasks:
``` bash 
python taskTracker.py list
```

- Update a task's description:
``` bash
python taskTracker.py update --id <task_id> --description "Updated description"
```

- Change a task's status:
``` bash
python taskTracker.py change-status --id <task_id> --status "done"
```

- Delete a task:
``` bash 
python taskTracker.py delete --id <task_id>
```

- Filter tasks by status:
``` bash 
python taskTracker.py filter --status "in-progress"
```

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
