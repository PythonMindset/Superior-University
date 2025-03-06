def LHUN():
    card=input("Enter the Card Number: ")
    total=0
    reverse_card=card[::-1]
    for i in range (len(reverse_card)):
        num=int(reverse_card[i])
        if i%2==1:
            num*=2
            if num>9:
                num-=9
        total+=num
    if total%10==0:
        print("Valid Card.")
    else:
        print("Invalid Card.")
# LHUN()

def puncutations():
    print("This program will be used to remove all the strings from the sentance.")
    input1=input("Enter the sentance: ")
    kick={",",".","?",",","!","(",")","[","]","{","}","\"","\'","`","@","/","\\","`"}
    for i in input1:
        if i in kick:
            input1=input1.replace(i,"")
    print(input1)
# puncutations()

def order():
    lines=input("Enter the sentence: ")
    word=lines.split()

    for i in range(len(word)-1):
        for j in range(len(word)-i-1):
            if word[j]>word[j+1]:
                word[j],word[j+1]=word[j+1],word[j]
    
    sorted_lines=" ".join(word)
    print(f"Sorted Lines: {sorted_lines}")
# order()