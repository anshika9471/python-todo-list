#  to do list in python
import json

#  Task class
class Task:
    def __init__(self, title, due_date="", priority="Medium"):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.completed = False
        

#  Task list
task_list = []

#  Add task
def add_task():
    title = input("Enter task title: ")
    due_date = input("Enter due date (optional): ")
    priority = input("Enter priority (Low/Medium/High): ")
    task = Task(title, due_date, priority)
    task_list.append(task)
 print" Task added successfully!")

#  View tasks
def view_tasks():
    if not task_list:
        print(" No tasks found.")
        return
    print("\n To-Do List:")
    for i, task in enumerate(task_list):
        status = " Done" if task.completed else " Pending"
        print(f"{i+1}. {task.title} | Due: {task.due_date} | Priority: {task.priority} | Status: {status}")

#  Mark task as completed
def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(task_list):
            task_list[index].completed = True
            print(" Task marked as completed.")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

#  Delete task
def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(task_list):
            task_list.pop(index)
            print(" Task deleted.")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

#  Save tasks to JSON file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump([task.__dict__ for task in task_list], file)
    print(" Tasks saved successfully!")

#  Load tasks from file
def load_tasks():
    global task_list
    try:
        with open("tasks.json", "r") as file: 
            data = json.load(file)
            task_list = [Task(**item) for item in data]
        print(" Tasks loaded successfully!")
    except FileNotFoundError:
        print(" No saved tasks found.")

#  Menu
def menu():
    while True:
        print("\n --- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5": 
            save_tasks()
        elif choice == "6":
            load_tasks()
        elif choice == "7":
            print(" Goodbye! Stay productive.")
            break
        else:
            print(" Invalid choice. Try again.")

#  Start the app
if __name__ == "__main__":
    load_tasks()  # Optional: auto-load tasks at start
    menu()