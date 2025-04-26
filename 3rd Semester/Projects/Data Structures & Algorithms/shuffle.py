import pandas as pd
import os
import random
import pygame
from sortings import sorting_menu
df=pd.read_csv('songs_data.csv')

class stack:
    def __init__(self):
        self.stack=[]
    
    def add(self):
        for i in range (len(df['name'])):
            song=df['name'][i]
            self.stack.append(song)
            print(f"{song} added to the stack.\n")
        random.shuffle(self.stack)
        print("\n Playlist Shuffled!\n")
    
    def remove(self):
        if len(self.stack)==0:
            print("Stack is empty.\n")
            return
        else:
            choice=input("Enter song name you want to remove: ").lower()
            try:
                index=self.stack.index(choice)
                song=self.stack.pop(index)
                print(f"{song} removed from the stack.\n")
                return
            except ValueError:
                print("Song not found in the stack.\n")
    
    def display_playlist(self):
        if len(self.stack)==0:
            print("Stack is empty.\n")
        else:
            count=1
            for i in range(len(self.stack)):
                print(f"{count}. {self.stack[i]}.")
                count+=1
    
    def play_playlist(self):
        pygame.mixer.init()
        if len(self.stack)==0:
            print("No songs in the queue.\n")
            return
        while len(self.stack)>0:
            self.display_playlist()
            name=self.stack.pop(0)
            for i in range(len(df)):
                if df['name'][i].lower() == name:
                    song_path = os.path.join('music', df['path'][i])
                    break
            print(f"\nNow playing: {name}")
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                command=input("Enter:\n 'n' for next song\n 'p' to pause song\n 'r' to resume song\n 'q' to quit\n--> ").lower()
                if command == 'n':
                    pygame.mixer.music.stop()
                    break
                elif command == 'p':
                    pygame.mixer.music.pause()
                    while True:
                        resume_command = input("...Song paused...\n Enter:\n 'r' to resume\n 'n' for next song\n 'q' to quit\n--> ").lower()
                        if resume_command == 'r':
                            pygame.mixer.music.unpause()
                            break
                        elif resume_command == 'n':
                            pygame.mixer.music.stop()
                            break
                        elif resume_command == 'q':
                            pygame.mixer.music.stop()
                            print("Exiting the playlist.\n")
                            return
                        else:
                            print("Invalid command.\n")
                elif command == 'r':
                    pygame.mixer.music.unpause()
                    print("Resumed playing.\n")
                elif command == 'q':
                    pygame.mixer.music.stop()
                    print("Exiting the playlist.\n")
                    return
                else:
                    print("Invalid command.\n")
    
    def display_data_base(self):
        if len(df) == 0:
            print("No songs in the database.\n")
        else:
            print("Available songs in the database:")
            for i in range(len(df)):
                print(f"Name: {df['name'][i]}")
                print(f"Length: {df['length'][i]} seconds")
                print(f"Rating: {df['rating'][i]}")
                print("-" * 30)

def shuffle_menu():
    obj=stack()
    while True:
        print("=" * 60)
        print("🎧 STACK SHUFFLE MUSIC PLAYER MENU 🎧".center(60))
        print("=" * 60)
        print("1. 🎼 Display Songs in Database")
        print("2. 🗂️ Display Songs by Sorting")
        print("3. ➕ Add Song(s) to Playlist")
        print("4. ❌ Remove Song from Playlist")
        print("5. 📜 Display Current Playlist")
        print("6. ▶️ Play Playlist")
        print("7. 🚪 Exit")
        print("=" * 60)
        choice1=input("Enter your choice (1-7): ")
        if choice1 =='1':
            obj.display_data_base()
        elif choice1 =='2':
            sorting_menu()
        elif choice1 == '3':
            obj.add()
        elif choice1== '4':
            obj.remove()
        elif choice1 == '5':
            obj.display_playlist()
        elif choice1 == '6':
            obj.play_playlist()
        elif choice1 == '7':
            print("Exiting the Shuffle player.🎧")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.\n")

# shuffle_menu()