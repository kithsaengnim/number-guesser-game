import random

def get_player_guess():
    pass  # TODO: implement this function

def check_guess(secret, guess):
    pass  # TODO: implement this function

def play_game():
    secret_number = random.randint(1, 100)
    guess = None

    while guess != secret_number:
        guess = get_player_guess()
        check_guess(secret_number, guess)
