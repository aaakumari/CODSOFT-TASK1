# Define a list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")

# Function to remove a task from the list
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed from your to-do list.")
    else:
        print("Invalid task index!")

# Main function to operate the to-do list
def todo_list():
    while True:
        print("\nSelect an option:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            task = input("Enter task to add: ")
            add_task(task)
        elif choice == '3':
            if tasks:
                index = int(input("Enter index of task to remove: "))
                remove_task(index)
            else:
                print("Your to-do list is empty!")
        elif choice == '4':
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Calling the todo_list function to start the program
if __name__ == "__main__":
    todo_list()
