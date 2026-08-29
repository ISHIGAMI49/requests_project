tasks=[]
while True :
    print("--- To-Do Menu---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")

    choice= input("Enter your choice :")

    if choice == "1" :
        task=input("Add a task :")
        tasks.append(task)
        print("task added")
    elif choice == "2" :
        for index,tsk in enumerate(tasks ,start=1) :
            print(index,":",tsk)
    elif choice == "3" :
        for index,tsk in enumerate(tasks ,start=1) :
                    print(index,":",tsk)
        taskdel=int(input("wich one :"))
        tasks.pop(taskdel  - 1)
        print("Task deleted")
        print("The rest :")
        for index,tsk in enumerate(tasks ,start=1) :
                    print(index,":",tsk)
    elif choice == "4":
        print("Goodbye")
        break
    else : 
        print("Try again")