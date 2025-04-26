import pandas as pd
import os
import pygame
from sortings import sorting_menu
df=pd.read_csv('songs_data.csv')

class repeat_player:
    def __init__(self,name,song_path):
        self.name=name
        self.song_path=song_path
        self.next=None
        self.prev=None

class CDLL(repeat_player):
    def __init__(self):
        self.head=None
    
    def add_song_to_playlist(self):
        name=input("Enter the song name: ").lower()
        song_found=False
        for i in range(len(df)):
            if df['name'][i]==name:
                song_found=True
                song_path=df['path'][i]
                break
        if not song_found:
            print("Song not found in the database.\n")
        else:
            new_song=repeat_player(name,song_path)
            if self.head is None:
                self.head=new_song
                new_song.next=new_song
                new_song.prev=new_song
            else:
                tail=self.head.prev
                tail.next=new_song
                new_song.prev=tail
                new_song.next=self.head
                self.head.prev=new_song
            print("Song added to the playlist.\n")
    
    def remove_song_from_playlist(self):
        name=input("Enter the song name to remove: ").lower()
        if self.head is None:
            print("No songs in the playlist.\n")
            return
        current=self.head
        while True:
            if current.name==name:
                if current.next==current:
                    self.head=None
                else:
                    current.prev.next=current.next
                    current.next.prev=current.prev
                    if current == self.head:
                        self.head = current.next
                print("Song has been removed from the playlist.\n")
                return
            current=current.next
            if current==self.head:
                break
        print("Song not found in the playlist.\n") 
    
    def display_playlist(self):
        if self.head is None:
            print("No songs in the playlist.\n")
            return
        current=self.head
        count=1
        print("Songs in the playlist:")
        while True:
            print(f"{count}. {current.name}")
            count+=1
            current=current.next
            if current==self.head:
                break
    
    def play_playlist(self):
        pygame.mixer.init()
        if self.head is None:
            print("No songs in the playlist.\n")
            return
        current=self.head
        while True:
            self.display_playlist()
            name=current.name
            for i in range(len(df)):
                if df['name'][i].lower() == name:
                    song_path = os.path.join('music', df['path'][i])
                    break
            print(f"\nNow playing: {current.name}")
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                command=input("Enter:\n 'n' for next song\n 'b' for previous song\n 'p' to pause song\n 'r' to resume song\n 'q' to quit\n--> ").lower()
                if command == 'n':
                    current = current.next
                    break
                if command == 'b':
                    current = current.prev
                    break
                elif command == 'p':
                    pygame.mixer.music.pause()
                    while True:
                        resume_command = input("...Song paused...\n Enter:\n 'r' to resume\n 'n' for next song\n 'b' for previous song\n 'q' to quit\n--> ").lower()
                        if resume_command == 'r':
                            pygame.mixer.music.unpause()
                            break
                        elif resume_command == 'n':
                            pygame.mixer.music.stop()
                            current = current.next
                            break
                        elif resume_command == 'b':
                            pygame.mixer.music.stop()
                            current = current.prev
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

def Repeat_menu():
    obj=CDLL()
    while True:
        print("=" * 60)
        print("🎧 REPEAT MUSIC PLAYER MENU 🎧".center(60))
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
            choice2=int(input("How many songs do you want to add: "))
            obj.display_data_base()
            for i in range(choice2):
                obj.add_song_to_playlist()
        elif choice1== '4':
            obj.remove_song_from_playlist()
        elif choice1 == '5':
            obj.display_playlist()
        elif choice1 == '6':
            obj.play_playlist()
        elif choice1 == '7':
            print("Exiting the repeat player.🎧")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.\n")

# obj1=CDLL()
# obj1.display_data_base()
# obj1.add_song_to_playlist()
# obj1.add_song_to_playlist()
# obj1.play_playlist()

# Repeat_menu()