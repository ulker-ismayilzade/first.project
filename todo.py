import json

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

def main():
    tasks = load_tasks()
    while True:
        print("\nTasks:", tasks)
        choice = input("1:Add 2:Remove 3:Exit > ")
        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            if task in tasks: tasks.remove(task)
        elif choice == "3":
            break
        save_tasks(tasks)

if __name__ == "__main__":
    main()
