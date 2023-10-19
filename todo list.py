todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the TODO list.")

def update_task(index, new_task):
    if index >= 0 and index < len(todo_list):
        todo_list[index] = new_task
        print(f"Task {index + 1} updated to '{new_task}'.")
    else:
        print("Invalid task index.")

def display_list():
    print("\nTODO List:")
    for index, task in enumerate(todo_list):
        print(f"{index + 1}. {task}")
    print()

while True:
    print("Options:")
    print("1. Add a task")
    print("2. Update a task")
    print("3. Display the TODO list")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        display_list()
        index = int(input("Enter the task number to update: ")) - 1
        new_task = input("Enter the updated task: ")
        update_task(index, new_task)
    elif choice == '3':
        display_list()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
