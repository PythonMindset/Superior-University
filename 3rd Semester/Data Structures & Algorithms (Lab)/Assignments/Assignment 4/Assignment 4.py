def task1(arr1):
    print(f"Input Array: {arr1}.")
    for i in range(len(arr1)-1):
        small=i
        for j in range(i+1,len(arr1)):
            if arr1[j]<arr1[small]:
                small=j
        arr1[i],arr1[small]=arr1[small],arr1[i]
    print(f"Output Array: {arr1}.")
# task1([29, 10, 14, 37, 14])

def task2(arr2):
    print(f"Input Array: {arr2}.")
    for i in range(len(arr2)-1):
        small=i
        for j in range(i+1,len(arr2)):
            if arr2[j]<arr2[small]:
                small=j
        arr2[i],arr2[small]=arr2[small],arr2[i]
    print(f"Output Array: {arr2}.")
# task2(["apple","orange","banana","kiwi"])

def task3(arr3):
    print(f"Input Array: {arr3}.")
    for i in range(len(arr3)-1):
        small=i
        for j in range(i+1,len(arr3)):
            if arr3[j]<arr3[small]:
                small=j
        arr3[i],arr3[small]=arr3[small],arr3[i]
    arr3.reverse()
    print(f"Output Array: {arr3}.")
# task3([12, 4, 45, 23, 18])

def task4(arr4):
    print(f"Input Array: {arr4}.")
    for i in range(len(arr4)-1):
        small=i
        for j in range(i+1,len(arr4)):
            if arr4[j][1]<arr4[small][1]:
                small=j
        arr4[i],arr4[small]=arr4[small],arr4[i]
    print(f"Output Array: {arr4}.")
# task4(["cat", "bat", "apple", "car"])

def task5(arr5):
    print(f"Input Array: {arr5}.")
    swaps=0
    for i in range(len(arr5)-1):
        small=i
        for j in range(i+1,len(arr5)):
            if arr5[j]<arr5[small]:
                small=j
        arr5[i],arr5[small]=arr5[small],arr5[i]
        swaps+=1
    print(f"Output Array: {arr5}.")
    print(f"Total Swaps Taken: {swaps}.")
# task5([29, 10, 14, 37, 14])

### Part2 ###
def task6(arr):
    print(f"Input Array: {arr}.")
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >= 0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j + 1]=key
    print(f"Output Array: {arr}.")
# task6([12, 11, 13, 5, 6])

def task7(arr):
    print("Not Attempted.")
    pass
# task7("True")

def task8(arr):
    print("Not Attempted.")
    pass
# task8("True")

def task9(arr):
    print(f"Input Array: {arr}.")
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >= 0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j + 1]=key
    print(f"Output Array: {arr}.")
# task9([(1,3),(4,1),(2,2)])

def task10(arr):
    print(f"Input Array: {arr}.")
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >= 0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j + 1]=key
    arr.reverse()
    print(f"Output Array: {arr}.")
# task10([12, 11, 13, 5, 6])

def task11(arr):
    print(f"Input Array: {arr}.")
    counter=0
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >= 0 and key<arr[j]:
            counter+=1
            arr[j+1]=arr[j]
            j-=1
        arr[j + 1]=key
    print(f"Output Array: {arr}.")
    print(f"Total Swaps Taken: {counter}.")
# task11([12, 11, 13, 5, 6])

def task12(matrix):
    print(f"Input Matrix: {matrix}.")
    for r in matrix:
        for i in range(1, len(r)):
            key=r[i]
            j=i - 1
            while j >= 0 and key < r[j]:
                r[j + 1]=r[j]
                j-=1
            r[j + 1] = key
    print(f"Output Matrix: {matrix}.")
# task12([[5, 1, 4],[3, 9, 2],[8, 6, 7]])