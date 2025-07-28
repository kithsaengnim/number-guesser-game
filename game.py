import random

def get_player_guess():
    return int(input("Enter your guess (1-100): "))

def check_guess(secret, guess):
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You win!")

def play_game():
    print("Starting game...")  
    secret_number = random.randint(1, 100)
    guess = None

    while guess != secret_number:
        guess = get_player_guess()
        check_guess(secret_number, guess)

if __name__ == "__main__":
    print("Running from main")  
    play_game()
