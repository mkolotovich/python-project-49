import prompt


def playGame(question, generateRoundData):
    correctAnswersCount = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    winAnswersCount = 3
    print(question)
    while (correctAnswersCount < winAnswersCount):
        [roundQuestion, r_ans] = generateRoundData()
        print(f'Question: {roundQuestion}')
        ans = prompt.string('Your answer: ')
        if (ans == r_ans):
            print('Correct!')
            correctAnswersCount += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
