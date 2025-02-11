import random
def mini1():
    print("Welcome to Fizz And Buzz.")
    print("There will be 5 rounds in total.")
    print("Rules:")
    print("\t 1. If the number is divisible by 3, Enter Fizz.")
    print("\t 2. If the number is divisible by 5, Enter Buzz.")
    print("\t 3. If the number is divisible by both 3 and 5, Enter FizzBuzz.")
    print("\t 4. If the number is not divisible by 3 or 5, Enter None.")
    times=1
    a1=0
    while times<=5:
        guess=random.randint(0,50)
        a2=a1
        a1=guess
        print(f"Guess: {guess}")
        user_guess=input("Enter your guess: ").lower()
        if user_guess=="fizzbuzz" and (a1+a2)%3==0 and (a1+a2)%5==0:
            print("Correct")
        elif user_guess=="fizz" and (a1+a2)%3==0:
            print("Correct")
        elif user_guess=="buzz" and (a1+a2)%5==0:
            print("Correct")
        elif user_guess=="none" and (a1+a2)%3!=0 and (a1+a2)%5!=0:
            print("Correct")
        elif user_guess != "none" and user_guess != "fizz" and user_guess != "buzz" and user_guess != "fizzbuzz":
            print("Invalid Input! Game Over ~~ XD")
            break
        else: 
            print("Wrong")
        times+=1
# mini1()

def mini2():
    movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
    ]
    input1=int(input("Enter the number of movies: \n"))
    for i in range (input1):
        movie_name=input("Enter the movie name: ")
        movie_budget=int(input("Enter the movie budget: "))
        print("\n")
        movies.append((movie_name,movie_budget))
    print("Calculating Average Budgets.....\n")
    for i in range(len(movies)):
        total = total + movies[i][1]
    avg=total/len(movies)
    print(f"The average budget of the movies is {int(avg)}\n")
    print("The movies that are above Average Budget:\n")
    total_abv_avg=0
    for i in movies:
        if i[1] > avg:
            print(f"Name: {i[0]}.")
            print(f"Budget: {i[1]}.\n")
            total_abv_avg+=1
    print(f"Total number of movies above average budget: {total_abv_avg}.")
# mini2()