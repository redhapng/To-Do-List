

tasks = []

while True : 
    print("n\--Welcom to thet to do list programe--")
    print("1. Add task : ")
    print("2. Show tasks : ")
    print("3. Mark task as done : ")
    print("4. Exit")

    choice = input("What is your choice? : ")

    if choice == "1":
        print()
        n_tasks = int(input("How much tasks you want to add: "))

        for i in range(n_tasks):
            task = input("Enter the task: ")
            tasks.append({"task": task, "done": False})
            print("Task added! ")
    elif choice == "2":
        print("\nTasks:")
        for index, task in  enumerate(tasks):
            status = "Done" if task["done"] else "Not done"
            print(f"{index + 1}. {task['task']} - {status}")
    elif choice == "3":
        task_index = int(print("Enter the number of the task you want to mark as done"))
        if 0 <= task_index < len(tasks):
            tasks[task_index]["done"] = True
            print("Task marked as done succesfully ")
        else:
            print("Invalid task number try again with a corecet number! ")
    elif choice == "4":
        print("Exiting the To-Do-List")
    else:
        print("Invalid choice. Please try again")


    

