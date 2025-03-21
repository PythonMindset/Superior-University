# def orting():
#     list1=[9,4,2,0,1]
#     print(list1)
#     for i in range(len(list1)-1):
#         for j in range(len(list1)-1-i):
#             if list1[j]>list1[j+1]:
#                 list1[j],list1[j+1]=list1[j+1],list1[j]
#             print(list1)
# orting()

# class b_sort:
#     def __init__(self):
#         self.arr=[]
#         self.limit=int(input("Enter the limit:"))
    
#     def adding(self):
#         for i in range(self.limit):
#             self.arr.append(int(input("Enter the number:")))
    
#     def sorting(self):
#         counter=0
#         print(f"Default Array: {self.arr}.")
#         for i in range(len(self.arr)-1):
#             flag = False
#             for j in range(len(self.arr)-1-i):
#                 if self.arr[j]>self.arr[j+1]:
#                     counter+=1
#                     self.arr[j],self.arr[j+1]=self.arr[j+1],self.arr[j]
#                     flag = True
#                     print(f"Pass {counter}: {self.arr}.")
#             if flag == False:
#                 print("Not swapped exiting early.....")
#                 break
    
# obj1=b_sort()
# obj1.adding()
# obj1.sorting()

arr=[5,4,2,9,3,0]
def bubble(arr):
    counter=0
    print(f"Default Array: {arr}.")
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                flag = True
                counter+=1
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(f"Pass {counter}: {arr}.")
        if flag == False:
            print("Not swapped exiting early.....")
            break
    print(f"Total swaps: {counter}")
    return(counter)
bubble_sort=bubble(arr)

arr=[5,4,2,9,3,0]
def insertion(arr):
    shifts=0
    print(f"Default Array: {arr}.")
    for i in range(1, len(arr)):
        shifts+=1
        key=arr[i]
        j=i - 1
        while j>=0 and arr[j]>key:
            arr[j + 1]=arr[j]
            j-=1
        arr[j + 1]=key
        print(f"Pass {i}: {arr}.")
    print(f"Total swaps: {shifts}")
    return(shifts)
insertion_sort=insertion(arr)

if bubble_sort<insertion_sort:
    print("Bubble sort is better")
elif insertion_sort<bubble_sort:
    print("Insertion sort is better")
else:
    print("Both are same")
