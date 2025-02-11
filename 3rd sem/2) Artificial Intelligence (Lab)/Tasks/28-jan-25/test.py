def try1():
    temp1=int(input("Enter the current temperature: "))
    if temp1<22:
        print("The heater is turned on....")
    elif temp1>=22:
        print("The heater is turned off....")
# try1()

class temp:
    def __init__(self):
        self.temp1=None
    def precieve(self):
        self.temp1=int(input("Enter the current temperature: "))
    def act(self):
        if self.temp1<22:
            print("The heater is turned on....")
        elif self.temp1>=22:
            print("The heater is turned off....")
# obj1=temp()
# obj1.precieve()
# obj1.act()

class try2:
    def __init__(self,temp):
        self.desired_temp=temp
    def precieve(self):
        return int(input("Enter the current temperature: "))
    def act(self,temp):
        if temp>self.desired_temp:
            print(f"Temperature: {temp}, Action: Turn the Heater off....")
        else:
            print(f"Temperature: {temp}, Action: Turn the Heater on....")
# obj2=try2(int(input("Enter the desired temperature: ")))
# obj2.act(obj2.precieve())

class try3:
    def __init__(self,temp):
        self.desired_temp=temp
    def act(self,temp):
        if temp>self.desired_temp:
            return (f"Temperature: {temp}, Action: Turn the Heater off....")
        else:
            return (f"Temperature: {temp}, Action: Turn the Heater on....")
# obj3=try3(int(input("Enter the desired temperature: ")))
# rooms={
#     "Living room": 22,
#     "Dining room": 20,
#     "Bedroom": 16,
#     "Library": 12,
# }
# for room,temp10 in rooms.items():
#     print(f"Room: {room}  -- {obj3.act(temp10)}.")

def puncutations():
    print("This program will be used to remove all the strings from the sentance.")
    input1=input("Enter the sentance: ")
    # print(input1.replace(",","").replace(".","").replace("?","").replace("!","").replace(":","").replace(";","").replace("-","").replace("(","").replace(")","").replace("[","").replace("]","").replace("{","").replace("}","").replace("\"","").replace("\'","").replace("`",""))
    kick={",",".","?",",","!","(",")","[","]","{","}","\"","\'","`","@","/","\\","`"}
    for i in input1:
        if i in kick:
            input1=input1.replace(i,"")
    print(input1)
puncutations()

def sort_alphabet():
    pass