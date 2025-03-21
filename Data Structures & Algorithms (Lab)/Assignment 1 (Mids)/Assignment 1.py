### Task1
class stack():
    def __init__(self):
        self.stack=[]
    def push(self):
        value=input("Enter the element you want to Push: ")
        self.stack.append(value)
    def pop(self):
        print("Popped element is: ",self.stack.pop())
        print(f"The Top element is: {self.stack[-1]}")
    def peek(self):
        print(f"The Top element is: {self.stack[-1]}")
    def is_empty(self):
        if not self.stack:
            print("True.")
        else:
            print("False.")
    def size(self):
        print(f"The size of stack is: {len(self.stack)}.")
# obj1=stack()
# obj1.push()
# obj1.push()
# obj1.push()
# obj1.pop()
# obj1.peek()
# obj1.size()
# obj1.is_empty()

### Task2
class queue():
    def __init__(self):
        self.queue=[]
    def enqueue(self):
        value=input("Enter the element you want to Enqueue: ")
        self.queue.append(value)
    def dequeue(self):
        print("Dequeued element is: ",self.queue.pop(0))
        print(f"The Front element is: {self.queue[0]}")
    def front(self):
        print(f"The Front element is: {self.queue[0]}")
    def is_empty(self):
        if not self.queue:
            print("True.")
        else:
            print("False.")
    def size(self):
        print(f"The size of queue is: {len(self.queue)}.")
# obj2=queue()
# obj2.enqueue()
# obj2.enqueue()
# obj2.enqueue()
# obj2.dequeue()
# obj2.front()
# obj2.size()
# obj2.is_empty()

### Task3
import random
import time
def bubble(list1):
    # print(f"Before Sort: {list1}.")
    for i in range(len(list1)-1):
        for j in range(len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    # print(f"After Sort: {list1}.")
# bubble([64, 34, 25, 12, 22, 11, 90])
def selection(list2):
    # print(f"Before Sort: {list2}.")
    for i in range(len(list2)-1):
        small=i
        for j in range(i+1,len(list2)):
            if list2[j]<list2[small]:
                small=j
        list2[i],list2[small]=list2[small],list2[i]
    # print(f"After Sort: {list2}.")
# selection([64, 34, 25, 12, 22, 11, 90])
def insertion(list3):
    # print(f"Before Sort: {list3}.")
    for i in range(1,len(list3)):
        key=list3[i]
        j=i-1
        while j>=0 and key<list3[j]:
            list3[j+1]=list3[j]
            j=j-1
        list3[j+1]=key
    # print(f"After Sort: {list3}.")
# insertion([64, 34, 25, 12, 22, 11, 90])
def comparison():
    final_arr=[]
    for i in range(1000):
        final_arr.append(random.randint(1,1000))

    bubble_copy=final_arr.copy()
    start=time.time()
    bubble(bubble_copy)
    end=time.time()
    print(f"Bubble Sort Time: {end-start: .3f} seconds.")

    selection_copy=final_arr.copy()
    start=time.time()
    selection(selection_copy)
    end=time.time()
    print(f"Selection Sort Time: {end-start: .3f} seconds.")

    insertion_copy=final_arr.copy()
    start=time.time()
    insertion(insertion_copy)
    end=time.time()
    print(f"Insertion Sort Time: {end-start: .3f} seconds.")
# comparison()

### Task4
def sorted_insertion(arr):
    element=int(input("Enter the element to be inserted: "))
    arr.append(element)
    for i in range(len(arr) -1, 0,-1):
        if arr[i]<arr[i-1]:
            arr[i], arr[i-1]=arr[i-1], arr[i]
        else:
            break
    print(arr)
sorted_list = [10,20,30,40,50]
sorted_insertion(sorted_list)