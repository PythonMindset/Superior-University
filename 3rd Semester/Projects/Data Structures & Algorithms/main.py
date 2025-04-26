from repeat_playlist import Repeat_menu
from single_playlist import single_menu
from play_all import play_all_menu
from shuffle import shuffle_menu
from sortings import sorting_menu

def main():
    while True:
        print("-" * 60)
        print("🎧 Welcome to Music Player 🎧".center(60))
        print("=" * 60)
        print("1. ♻️ Goto Repeat Playlist Maker.")
        print("2. 🎶 Goto Single Play Playlist Maker.")
        print("3. 🔀 Goto Shuffle Playlist Maker.")
        print("4. 🕹️ Goto Play All Playlist Maker.")
        print("5. 📋 Goto Sorting Database.")
        print("6. 🏃‍♂️ Exit")
        print("-" * 60)
        choice1=input("Enter your choice (1-6): ")
        if choice1 =='1':
            Repeat_menu()
        elif choice1 =='2':
            single_menu()
        elif choice1 == '3':
            shuffle_menu()
        elif choice1== '4':
            play_all_menu()
        elif choice1 == '5':
            sorting_menu()
        elif choice1 == '6':
            print("Exiting the music player. Goodbye! 🎧")
            return
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")

main()