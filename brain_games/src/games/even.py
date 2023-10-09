import brain_games.src.engine
from random import randint


def is_even(number):
    return number % 2 == 0


def generate_game_data():
    question = randint(0, 20)
    answer = 'yes' if is_even(question) else 'no'
    return [question, answer]


def start_game():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    brain_games.src.engine.play_game(question, generate_game_data)
