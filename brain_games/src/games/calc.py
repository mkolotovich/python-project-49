import brain_games.src.index
from random import randint


def sum(a, b):
    return a + b


def diff(a, b):
    return a - b


def mult(a, b):
    return a * b


def generateGameData():
    operations = [['+', sum], ['-', diff], ['*', mult]]
    firstNum = randint(1, 25)
    signsIndex = randint(0, len(operations) - 1)
    secondNum = randint(1, 25)
    [sign, operation] = operations[signsIndex]
    question = f'{firstNum} {sign} {secondNum}'
    answer = str(operation(firstNum, secondNum))
    return [question, answer]


def startGame():
    question = 'What is the result of the expression?'
    brain_games.src.index.playGame(question, generateGameData)
