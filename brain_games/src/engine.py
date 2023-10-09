import prompt


def play_game(question, generate_round_data):
    correct_answers_count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    win_answers_count = 3
    print(question)
    while (correct_answers_count < win_answers_count):
        round_question, r_ans = generate_round_data()
        print(f'Question: {round_question}')
        ans = prompt.string('Your answer: ')
        if (ans == r_ans):
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
