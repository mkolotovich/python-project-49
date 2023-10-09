import brain_games.src.engine
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
    progression = make_progression(progression_start, step, min_length)
    modifyed_numbers = progression[:]
    random_index = randint(0, len(progression) - 1)
    modifyed_numbers[random_index] = '..'
    question = ''
    for num in modifyed_numbers:
        question = f'{question} {num}'
    answer = str(progression[random_index])
    sliced_question = question[1:]
    return [sliced_question, answer]


def start_game():
    question = 'What number is missing in the progression?'
    brain_games.src.engine.play_game(question, generate_game_data)
