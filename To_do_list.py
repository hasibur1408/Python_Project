def add_task(Tasks):
    Task=input("Enter your task :")
    Tasks.append(Task)
    print(f"Task '{Task}' added")
    
def show_task(Tasks):
    if not Tasks:
        print("No task assign")
        return 
    else:
        print("\n--- Your To-Do List ---")
        for n,Task in enumerate(Tasks,start=1):
            print(f'{n}.',Task)
            
def remove_task(Tasks):
    show_task(Tasks)
    if not Tasks:
        return 
    task_index=int(input("Enter task number you want to remove "))
       
    if 1<=task_index<=len(Tasks):
        remove_task=Tasks.pop(task_index)
        print(f"Task {remove_task} remove")
    else:
        print("Invalid task Number")
    
if __name__ == "__main__":   
    
    Tasks=[]
    print("welcome to Do_do_List")
    while True:
        print("-----Enter your chooice-----\n")
        print("1. Add Task to the list.")
        print("2. Show Task from the list.")
        print("3. Remove Task from the list.")
        print("4. Exit.")
        chooice=input("Enter your chooice : ")
        
        match chooice:
            case '1':
                add_task(Tasks)
            case '2':
                show_task(Tasks)
            case '3':
                remove_task(Tasks)
            case '4':
                break
            case _:
                print("Wrong chooice. Try again")
         
    