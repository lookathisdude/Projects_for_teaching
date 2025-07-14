#Lists
# A list is defined with []
todo_list=[]

def display_todos():
    #If there is nothing in todo_list
    if not todo_list:
        print("You have nothing to do!")
    else:
        print("\nTodo list: ")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    print()

def add_task():
    task = input("Enter a new task to do: ")
    todo_list.append(task) #Append is to add the input to the list
    print("Task added.\n")

def delete_task():
    display_todos()
    try:
        task_num=int(input("What task do you want to delete? "))
        if 1 <= task_num <= len(todo_list):
            removed_item=todo_list.pop(task_num - 1) #remove the task from the list and
            # minus one from it
            print(f"Removed: {removed_item}\n")  #Display the removed item
            #{} acts as an object
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("Options: [1] View [2] Add [3] Delete [4] Quit")
        choice=input("Choose an option you want to do: ")
        print()

        if choice == "1":
            display_todos()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Have a nice day :) ")
            break
        else:
            print("Invalid choice.\n")
if __name__ == "__main__":
    main()