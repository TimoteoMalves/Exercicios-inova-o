'''class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


    def remove_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        if self.tasks:
            counter = 1
            for i in self.tasks:
                print(f"\nTask {counter}: {i}")
                counter += 1
        else:
            print("nothing to show")

    def clear_tasks(self):
        self.tasks = []
        return self.tasks
    
myList = ToDoList()
myList.add_task("Go home")
myList.add_task("Study")
myList.add_task("Play")
myList.show_tasks()
myList.remove_task("Play")
myList.show_tasks()
myList.clear_tasks()
myList.show_tasks()'''

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


    def remove_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        if self.tasks:
            counter = 1
            for i in self.tasks:
                print(f"\nTask {counter}: {i}")
                counter += 1
        else:
            print("nothing to show")

    def clear_tasks(self):
        self.tasks = []
        return self.tasks

def menu():
    print('1 - add\n2 - remove\3 - show\n4 - clear\n5 - Exit')
    opc = str(input("Option: "))
    return opc

def main():
    myList = ToDoList()

    while True:
        opc = menu()

        if opc == 1:
           task = str(input("Task: "))
           myList.add_task(task)

        elif opc == 2:
            task_removed = str(input("Task to be remove: "))
            myList.remove_task(task_removed)

        elif opc == 3:
            myList.show_tasks()

        elif opc == 4:
            myList.clear_tasks()

        elif opc == 5:
            break
        

main()



