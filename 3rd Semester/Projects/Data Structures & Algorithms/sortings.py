import pandas as pd
import os
import pygame
df=pd.read_csv('songs_data.csv')

def alphabet_sort():
    def bubble_sort(words):
        n = len(words)
        for i in range(n):
            for j in range(0, n-i-1):
                if words[j].lower() > words[j+1].lower():
                    words[j], words[j+1] = words[j+1], words[j]
        return words
    names=[]
    for i in range(len(df)):
        names.append(df['name'][i])
    sorted_words = bubble_sort(names)
    count=1
    print("=" * 60)
    print("Sorted By Alphabets".center(60))
    for i in range(len(sorted_words)):
        print(f"{count}. {sorted_words[i]}.")
        count+=1
    print("=" * 60)

def length_sorting():
    def insertion_sort(numbers):
        for i in range(1, len(numbers)):
            key = numbers[i]
            j = i - 1
            while j >= 0 and numbers[j] > key:
                numbers[j + 1] = numbers[j]
                j -= 1
            numbers[j + 1] = key
        return numbers
    times=[]
    for i in range(len(df)):
        times.append(df['length'][i])
    insertion_sort(times)
    names=[]
    used=[]
    for t in times:
        for i in range(len(df)):
            if df["length"][i] == t and i not in used:
                used.append(i)
                names.append(df["name"][i])
    count=1
    print("=" * 60)
    print("Sorted By Length".center(60))
    for i in range(len(names)):
        print(f"{count}. {names[i]}.")
        count+=1
    print("=" * 60)

def rating_sort():
    def selection_sort(rating):
        for i in range(len(rating)):
            min_index = i
            for j in range(i + 1, len(rating)):
                if rating[j] < rating[min_index]:
                    min_index = j
            rating[i], rating[min_index] = rating[min_index], rating[i]
        return rating
    rating=[]
    for i in range(len(df)):
        rating.append(df["rating"][i])
    selection_sort(rating)
    rating.reverse()
    names=[]
    used=[]
    for r in rating:
        for i in range(len(df)):
            if df["rating"][i] == r and i not in used:
                used.append(i)
                names.append(df["name"][i])
    count=1
    print("=" * 60)
    print("Sorted By Rating".center(60))
    for i in range(len(names)):
        print(f"{count}. {names[i]}.")
        count+=1
    print("=" * 60)

def sorting_menu():
    while True:
        print("=" * 60)
        print("🎧 SORTING MUSIC PLAYER MENU 🎧".center(60))
        print("=" * 60)
        print("1. 🎼 Sort the database by Alphabets.")
        print("2. ➕ Sort the database by Length.")
        print("3. ❌ Sort the database by Rating.")
        print("4. 🚪 Exit")
        print("=" * 60)
        choice=int(input("Enter your choice (1-4): "))
        if choice == 1:
            alphabet_sort()
        elif choice ==2:
            length_sorting()
        elif choice ==3:
            rating_sort()
        elif choice==4:
            print("Exiting the Sorting Menu.🎧")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.\n")

# alphabet_sort()
# length_sorting()
# rating_sort()

# sorting_menu()