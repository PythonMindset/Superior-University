class task1:
    def __init__(self):
        self.stack=[]

    def process(self, statement):
        for i in statement:
            if i.isdigit():
                self.stack.append(int(i))
            else:
                a1=self.stack.pop()
                a2=self.stack.pop()
                if i=="+":
                    self.stack.append(a1+a2)
                elif i=="-":
                    self.stack.append(a1-a2)
                elif i=="*":
                    self.stack.append(a1*a2)
                elif i=="/":
                    self.stack.append(a1/a2)
                else:
                    print("Invalid operator. Ending....")
                    break
        return self.stack.pop()
# statement = input("Enter a statement: ")
# obj1 = task1()
# ans = obj1.process(statement)
# print(f"The result of the postfix expression \'{statement}\' is: {ans}")

class task2:
    def __init__(self):
        self.back_stack=[]
        self.forward_stack=[]
        self.current_url=None
    
    def current(self):
        self.current_url=input("Enter the current url: ")
        self.back_stack.append(self.current_url)
        self.forward_stack.clear()

    def previous(self):
        if self.back_stack:
            self.forward_stack.append(self.current_url)
            self.current_url=self.back_stack.pop()
        else:
            print("Back Stack is empty....")
    
    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current_url)
            self.current_url=self.forward_stack.pop()
        else:
            print("Front Stack is empty....")

    def display(self):
        print(f"Current URL: {self.current_url}")
        print(f"Back URL: {self.back_stack.pop()}")
        print(f"Front URL: {self.forward_stack.pop()}")
# obj1=task2()
# obj1.current()
# obj1.current()
# obj1.current()
# obj1.previous()
# obj1.display()

class task3:
    def __init__(self):
        self.stack = []
        self.input1=input("Input: ").lower()
    
    def push(self):
        for i in self.input1:
            self.stack.append(i)

    def check(self):
        reversed_word=""
        while self.stack:
            reversed_word+=self.stack.pop()
        if self.input1==reversed_word:
            print("Output: True.")
        else:
            print("Output: False.")
# obj1=task3()
# obj1.push()
# obj1.check()
