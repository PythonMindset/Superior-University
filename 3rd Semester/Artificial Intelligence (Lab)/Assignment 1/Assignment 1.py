class listing():
    def __init__(self):
        self.list1=[]
    
    def add(self):
        print("--- Adding to the list ---")
        task=input("Please enter the task: ").lower()
        self.list1.append(task)
        print(f"Task \"{task}\" has been added to the list.")
    
    def display(self):
        print("--- Displaying the list ---")
        if not self.list1:
            print("The list is empty.")
        else:
            print("The list contains the following tasks:")
            i=0
            for task in self.list1:
                i+=1
                print(f"{i}) {task}")

    def remove(self):
        print("--- Removing from the list ---")
        task=input("Please enter the task: ").lower()
        if task not in self.list1:
            print(f"Task {task} is not in the list.")
        else:
            self.list1.remove(task)
            print(f"Task \"{task}\" has been removed from the list.")

    def update(self):
        print("--- Updating the list ---")
        task=input("Please enter the task: ").lower()
        if task not in self.list1:
            print(f"Task \"{task}\" is not in the list.")
        else:
            new_task=input("Please enter the new task: ").lower()
            self.list1.remove(task)
            self.list1.append(new_task)
            print(f"Task \"{task}\" has been updated to \"{new_task}\".")

def to_do_list():
    obj1=listing()
    while True:
        print("--- This is a dynamic To-Do-List ---")
        print("-:Menu:-")
        print("1) Add task.")
        print("2) Display task.")
        print("3) Remove task.")
        print("4) Update task.")
        print("5) End program.")
        input1=int(input(f"Please select an option: "))
        if input1==1:
            print("Add task.")
            obj1.add()
        elif input1==2:
            print("Display task.")
            obj1.display()
        elif input1==3:
            print("Remove task.")
            obj1.remove()
        elif input1==4:
            print("Update task.")
            obj1.update()
        elif input1==5:
            print("End program.")
            break
        else:
            print("Invalid input, please try again.")

to_do_list()