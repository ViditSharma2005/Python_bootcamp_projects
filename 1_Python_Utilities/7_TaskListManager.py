#terminal based task list manager
import os
TASK_FILE = "tasks.txt"

def load_tasks():
    tasks=[]
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE,"r","utf-8") as f:
            for line in f:
                text, status= line.strip().rstrip("||",1)
                tasks.append({"text":text,"done": status=="done"})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE,"w",encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']}||{status}\n")
        
def display_tasks(tasks):
    if not tasks:
        print("No tasks FOUND")
    else:
        for i , task in enumerate(tasks,1):
            checkbox = "✅" if task["done"] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()

def task_manager():
    tasks = load_tasks()

    while True:
        print(f"\n-----------Task Manager-----------")
        print("1.ADD TASK")
        print("2.VIEW TASK")
        print("3.MARK TASK AS COMPLETE")
        print("4.DELETE TASK")
        print("5.EXIT")

        choice = input("Enter an option (1-5)").strip()

        match choice:
            case "1":
                text = input("Enter your task").strip() 
                if text:
                    tasks.append({"text":text,"done":False})
                else:
                    print("Task Cannot be empty")
            case "2":
                display_tasks(tasks)
            case "3":
                display_tasks(tasks)
                try:
                    num=int(input("Enter task completed"))
                    if 1 <= num <=len(tasks) :
                        tasks[num-1]["done"]=True
                        save_tasks(tasks)
                        print("task marked as done")
                    else:
                        print("invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "4":                        
                display_tasks(tasks)
                try:
                    num=int(input("Enter task to be DELETED"))
                    if 1 <= num <=len(tasks) :
                        removed= tasks.pop(num-1)
                        save_tasks(tasks)
                        print(f"task removed {removed['text']}")
                    else:
                        print("invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "5":
                print("Exiting task manager")
                break
            case _:
                print("Please choose a valid option")
task_manager()
            
