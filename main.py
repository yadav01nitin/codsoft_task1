class ToDolist:
    def __init__(self):
        self.tasks={}

    def add_task(self,task_name,task_description):
        self.tasks[task_name]=task_description
        print("Task added")

    def update_task(self,task_name,new_description):
        if task_name in self.tasks:
            self.tasks[task_name]=new_description
            print("Task Updated")
        else:
            print(f"Task'{task_name}' not found")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task_name,task_description in self.tasks.items():
                print(f"Task: {task_name}\nDescription:{task_description}\n")

def main():
    todo_list=ToDolist()

    while True:
        print("1. Add Task")
        print("2. Update Task")
        print("3. Show  Task")
        print("4. Exit")
        select=input("Select your task: ")

        if select=="1":
            task_name=input("Enter your taskname: ")
            task_description=input("Enter your task description: ")
            todo_list.add_task(task_name, task_description)

        elif select=="2":
            task_name=input("Enter your taskname to update: ")
            newtask_description=input("Enter your new task description: ")
            todo_list.update_task(task_name, newtask_description)

        elif select=="3":
            todo_list.show_tasks()

        elif select=="4":
            break

        else:
            print("Select the valid task")

if __name__=="__main__":
    main()






