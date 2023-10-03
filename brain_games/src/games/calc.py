import brain_games.src.index
from random import randint


def sum(a, b):
    return a + b


def diff(a, b):
    return a - b


def mult(a, b):
    return a * b


def generate_game_data():
    operations = [['+', sum], ['-', diff], ['*', mult]]
    first_num = randint(1, 25)
    signs_index = randint(0, len(operations) - 1)
    second_num = randint(1, 25)
    [sign, operation] = operations[signs_index]
    question = f'{first_num} {sign} {second_num}'
    answer = str(operation(first_num, second_num))
    return [question, answer]


def start_game():
    question = 'What is the result of the expression?'
    brain_games.src.index.play_game(question, generate_game_data)
