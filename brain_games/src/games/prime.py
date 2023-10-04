import brain_games.src.index
from random import randint


def is_prime(num):
    if (num < 2):
        return False
    i = 2
    while (i <= num / 2):
        if (num % i == 0):
            return False
        i += 1
    return True


def generate_game_data():
    question = randint(1, 10)
    answer = 'yes' if is_prime(question) else 'no'
    return [question, answer]


def start_game():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    brain_games.src.index.play_game(question, generate_game_data)
