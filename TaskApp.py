import pickle
import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = '✓' if self.completed else '✗'
        return f'{status} {self.description}'


class TaskManager:
    def __init__(self, filename='tasks.pkl'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, description):
        self.tasks.append(Task(description))
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f'{i + 1}. {task}')

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()

    def save_tasks(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        return []

    def __str__(self):
        return f'TaskManager with {len(self.tasks)} tasks'

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add task 📝")
        print("2. Remove task 🗑️")
        print("3. List tasks 📄")
        print("4. Complete task ✅")
        print("5. Quit 🛑")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            task_manager.add_task(description)
            print("Task added!")
        elif choice == '2':
            task_manager.list_tasks()
            index = int(input("Enter task number to remove: ")) - 1
            task_manager.remove_task(index)
            print("Task removed!")
        elif choice == '3':
            task_manager.list_tasks()
        elif choice == '4':
            task_manager.list_tasks()
            index = int(input("Enter task number to complete: ")) - 1
            task_manager.complete_task(index)
            print("Task marked as completed!")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
