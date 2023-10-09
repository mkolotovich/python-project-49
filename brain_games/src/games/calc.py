import brain_games.src.engine
from random import randint


def sum(a, b):
    return a + b


def diff(a, b):
    return a - b


def mult(a, b):
    return a * b


def generate_game_data():
    signs = ['+', '-', '*']
    random_sign = signs[randint(0, len(signs) - 1)]
    operations = {'+': sum, '-': diff, '*': mult}
    first_num = randint(1, 25)
    second_num = randint(1, 25)
    operation = operations[random_sign]
    question = f'{first_num} {random_sign} {second_num}'
    answer = str(operation(first_num, second_num))
    return [question, answer]


def start_game():
    question = 'What is the result of the expression?'
    brain_games.src.engine.play_game(question, generate_game_data)
