import random
import time

#Checks to see if the number to guess is prime (hint)
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_hint(number_to_guess):
    if is_prime(number_to_guess):
        return f"Hint: it's a prime number."
    else:
        return f"Hint: it's not a prime number."

#Converts to binary (hint)   
def binary(number_to_guess):
    return f"Hint: The number is {bin(number_to_guess)[2:]}"

#Checks the difference between last guess and correct answer (hint)
def diff_hint(number_to_guess, last_guess):
    if last_guess is None:
        return None
    else:
        difference = abs(number_to_guess - last_guess)
        return f"Hint: The difference between your last guess and the correct number is {difference}."

#List of hints
def get_hint(number_to_guess, last_guess):
      
    hints_list = [
        "Hint: it's an even number." if random.randint(1,2) == 1 else "Hint: it's an odd mumber.",
        lambda number_to_guess: get_prime_hint(number_to_guess),
        lambda number_to_guess: binary(number_to_guess),
        lambda number_to_guess: diff_hint(number_to_guess, last_guess) if last_guess is not None else None,
        "Hint: it's a lucky mumber!" if number_to_guess == 7 else
        "Hint: it's an unlucky number!" if number_to_guess == 4 else
        "Hint: it's associated with a certain rapper!" if number_to_guess == 21 else 
        "Hint: it's associated with a certain rapper!" if number_to_guess == 50 else
        "Hint: it's the answer to life, the universe, and everything!" if number_to_guess == 42  else 
        "Guess the number in the middle of the range!"
    ]

    #grabs random hints
    while True:
            hint = random.choice(hints_list)
            if callable(hint):  # If the hint is a lambda function, call it
                hint = hint(number_to_guess)
            if hint is not None:
                return hint

#main function for game loop
def game():
    print("Hello! This is a number guessing game.\n" 
          "You have 30s to guess the number in the range given to you.\n"
          "Once you guess the right answer, an additional 10s is added to your time and you have to guess a new number from the wider range.\n"
          "Sounds easy, simple, and fun right?\n" 
          "You have three chances to guess the right answer. \n" 
          "Good luck!")

    lower_bound = 1
    upper_bound = 10
    base_time_limit = 30
    time_limit = base_time_limit
    chances = 4
    correct_counter = 0 #counts how many correct guesses they've had
    last_guess = None

    #This starts the main game loop
    while True:
        number_to_guess = random.randint(lower_bound+1, upper_bound-1)
        print(f"Guess a number between {lower_bound} and {upper_bound}.")
            
        start_time = time.time()
        attempts = 0
        last_guess = None
        
        
        while attempts < chances:
            elapsed_time = time.time() - start_time
            remaining_time = max(0, time_limit - elapsed_time)
            if elapsed_time > time_limit:
                    print(f"Time's up! The number was {number_to_guess}.")
                    lower_bound = 1
                    upper_bound = 10
                    time_limit = base_time_limit
                    break  # Exit the inner loop and start a new round
            
            user_input = input(f"You have {remaining_time:.0f} seconds to guess: ") 

            try:             
                   user_guess = int(user_input)
            except ValueError:
                    print("Invalid input....enter an integer.")
                    break
            
            if user_guess == number_to_guess:
                                print("Congratulations! You guessed the number!")
                                upper_bound += 10
                                last_guess = None
                                correct_counter += 1
                                time_limit = remaining_time + 10
                                if correct_counter == 3:
                                    print("You've guessed the number three times! Your lives have been restored and the timer has been reset!")
                                    attempts = 0
                                    correct_counter = 0
                                    time_limit = base_time_limit
                                break
            
            elif user_guess < number_to_guess:
                                print(f"Too low! You have {chances - attempts - 1} attempts left.")
                                attempts += 1
                                last_guess = user_guess

            elif user_guess > number_to_guess:
                                print(f"Too high! You have {chances - attempts - 1} attempts left.")
                                attempts += 1
                                last_guess = user_guess
                        
            if attempts == chances:
                            print(f"Game over! The number was {number_to_guess}.")
                            lower_bound = 1
                            upper_bound = 10
                            time_limit = base_time_limit
         
if __name__ == "__main__":
    game()