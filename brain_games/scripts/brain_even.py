#!/usr/bin/env python3
import brain_games.cli
import prompt
from random import randint

def is_even(num):
    return num % 2 == 0

def main():
    name = brain_games.cli.welcome_user()
    win_count = 3
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while(count < win_count):
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if (answer == 'yes' and is_even(random_number)):
            print("Correct!")
        elif (answer == 'no' and not is_even(random_number)):
            print("Correct!")
        else:
            if(answer == 'no'):
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, Bill!")
            return
        count = count + 1
    print("Congratulations, " + name + "!")

if __name__ == '__main__':
    main()