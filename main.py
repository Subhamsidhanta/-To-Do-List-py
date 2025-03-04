import os
import datetime as dt

print("To Do List")
print("_" * 20)
print(dt.datetime.today().strftime("%Y-%m-%d"))

da = dt.datetime.today().strftime("%d")

def date():
    with open("date.txt", "w") as f:
        f.write(da)

def rdate():
    if os.path.exists("date.txt"):
        with open("date.txt", "r") as f:
            return f.read().strip()  # Return stored date
    return ""

def changeDate():
    if str(da) != str(rdate()):
        with open("todo.txt", "w") as f:
            f.write("")  # Clears the todo file when date changes

# Task loading
def load():
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
            return [task.strip() for task in tasks]
    return []  # Return an empty list if file doesn't exist

def tasknum():
    tasks = load()
    if not tasks:
        return 1  # Start numbering from 1 if no tasks exist
    last = tasks[-1]
    num = last.split(".")[0]
    return int(num) + 1

def add():
    c = tasknum()
    task = input("Enter the task: ")
    with open("todo.txt", "a") as f:
        f.write(f"{c}. {task}\n")
    print("Task added successfully")
    print("_" * 20)

def delete():
    tasks = load()
    if not tasks:
        print("No tasks to delete!\n")
        return

    view()  # Show tasks before deletion
    try:
        n = int(input("Enter the task number to delete: "))
        new_tasks = [task for task in tasks if not task.startswith(f"{n}.")]

        with open("todo.txt", "w") as f:
            for task in new_tasks:
                f.write(task + "\n")

        print("Task deleted successfully!\n")
    except ValueError:
        print("Invalid input! Please enter a valid task number.\n")

def view():
    tasks = load()
    print("Your tasks are:")
    if tasks:
        print("\n".join(tasks))
    else:
        print("No tasks to display")
    print("_" * 20)

def main():
    date()
    changeDate()

    while True:
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        print("_" * 20)

        if choice == "1":
            add()
        elif choice == "2":
            delete()
        elif choice == "3":
            view()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
