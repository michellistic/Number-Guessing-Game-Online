import random
import time

#list of hints

#List of hints
hints_list = [
     "haven't filled this one out yet"
]

#List of hardships
hardship_list = [
     "Not done"
]
#grabs random hints
def get_hint()
     hint = random.choice(hints_list)

#grabs random hardships
def hardship()
     shinzo = random.choice(hardship_list))

#main function for game loop
def game():
    print("Hello! This is a number guessing game.\n You have 30s to guess the number in the range given to you.\n　Once you guess the right answer, an additional 10s is added to your time and you have to guess a new number from the wider range.\nSounds easy, simple, and fun right?\n You have three chances to guess the right answer. \n 行きましょう！")

    lower_bound = 1
    upper_bound = 10
    time_limit = 30
    chances = 3

    #This starts the main game loop
    number_to_guess = random.randint(lower_bound, upper_bound)
        print(f"Guess a number between {lower_bound} and {upper_bound}.")
        
        start_time = time.time()
        attempts = 0
        
        while attempts < chances:
            try:
                user_guess = int(input(f"You have {time_limit} seconds to guess: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue

        if user_guess == number_to_guess:
                print("Congratulations! You guessed the number!")
                lower_bound += 10
                upper_bound += 10
                time_limit += 10
                break  # Exit the inner loop and start a new round
            else:
                print(f"Wrong guess. You have {chances - attempts - 1} attempts left.")
                attempts += 1
            
            elapsed_time = time.time() - start_time
            if elapsed_time > time_limit:
                print(f"Time's up! The number was {number_to_guess}.")
                lower_bound = 1
                upper_bound = 10
                time_limit = 30
                break  # Exit the inner loop and start a new round
        
        if attempts == chances:
            print(f"Game over! The number was {number_to_guess}.")
            lower_bound = 1
            upper_bound = 10
            time_limit = 30

        while attempts < chances:
            hint = input("Would you like a hint? It will take 10 seconds off your timer.(y/n) ")
                if hint = 'y':
                    time_limit -= 10
                    hint = get_hint()
                    print(hint)
            shinzo = input("If you increase the difficulty, I'll give you an extra life. What do you say? (y/n): ")    
                if shinzo = 'y':
                    chances += 1
                    hardship = (hardship_list)
                    print(hardship)
        
