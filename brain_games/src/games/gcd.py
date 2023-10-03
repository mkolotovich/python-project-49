import brain_games.src.index
from random import randint


def find_gcd(first_num, second_num):
    bigger = first_num if (first_num > second_num) else second_num
    smaller = second_num if (first_num > second_num) else first_num
    if (bigger % smaller == 0):
        return smaller
    return find_gcd(smaller, bigger % smaller)


def generate_game_data():
    firstNum = randint(1, 101)
    second_num = randint(1, 101)
    question = f'{firstNum} {second_num}'
    answer = str(find_gcd(firstNum, second_num))
    return [question, answer]


def start_game():
    question = 'Find the greatest common divisor of given numbers.'
    brain_games.src.index.play_game(question, generate_game_data)
