def task1():
    students=[
        ("Ali",92),
        ("Reshail",86),
        ("Sufiyan",75),
        ("Azan",63),
        ("Abdul Ahad",78),
        ("Rafay",89),
        ("Ahmad",75)
    ]
    def sorting(students):
        print(f"Before Sort: {students}.")
        for i in range(len(students)-1):
            for j in range(len(students)-1-i):
                if students[j][1]<students[j+1][1]:
                    students[j],students[j+1]=students[j+1],students[j]
    sorting(students)
    print(f"After Sort: {students}.")
# task1()

def task2():
    words = ["apple", "banana", "kiwi", "grape", "cherry", "pear", "blueberry"]
    def sorting(words):
        print(f"Before Sort: {words}.")
        for i in range(len(words)-1):
            for j in range(len(words)-i-1):
                if len(words[j])>len(words[j+1]):
                    words[j],words[j+1]=words[j+1],words[j]
                elif len(words[j])==len(words[j+1]):
                    if words[j]>words[j+1]:
                        words[j],words[j+1]=words[j+1],words[j]
    sorting(words)
    print(f"After Sort: {words}.")
# task2()