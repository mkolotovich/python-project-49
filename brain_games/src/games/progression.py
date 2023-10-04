import brain_games.src.index
from random import randint


def make_progression(progression_start, step, length):
    progression = []
    progression_item = progression_start
    i = 0
    while (i < length):
        progression.append(progression_item)
        progression_item += step
        i += 1
    return progression


def generate_game_data():
    min_length = 5
    progression_start = 5
    step = 2
    length = 10
    if (length > min_length):
        progression = make_progression(progression_start, step, length)
    else:
        progression = make_progression(progression_start, step, min_length)
    modifyed_numbers = progression[:]
    random_index = randint(0, len(progression))
    modifyed_numbers[random_index] = '..'
    question = ''
    for num in modifyed_numbers:
        question = f'{question} {num}'
    answer = str(progression[random_index])
    return [question, answer]


def start_game():
    question = 'What number is missing in the progression?'
    brain_games.src.index.play_game(question, generate_game_data)
