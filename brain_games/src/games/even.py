import brain_games.src.index
from random import randint


def isEven(number):
    return number % 2 == 0


def generateGameData():
    question = randint(0, 20)
    answer = 'yes' if isEven(question) else 'no'
    return [question, answer]


def startGame():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    brain_games.src.index.playGame(question, generateGameData)
