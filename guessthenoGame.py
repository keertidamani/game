import random

def feedback(computer_choice, guess):
    difference = abs(computer_choice - guess)
    if difference <= 5:
        if computer_choice > guess:
            return 'Your guess is a little low.'
        else:
            return 'Your guess is a little high.'
    else:
        if computer_choice > guess:
            return 'Your guess is too low.'
        else:
            return 'Your guess is too high.'

def no_guesses(attempts, i):
    if attempts - i != 0:
        print('Guess again')
        return f"You have {attempts - i} attempts remaining to guess the number."
    else:
        return f'You are out of guesses {name}, Do you wanna play again?'

def guess_number(computer_choice, attempts):
    count=0
    print(f"You have {attempts} attempts remaining to guess the number!")
    for i in range(1, attempts + 1):
        count=count+1
        guess = int(input('\nMake a guess: '))
        if guess == computer_choice:
            print(f'Fantastic {name}! Your guess is right... The answer was {computer_choice}. You used {count} attempts.')
            break
        else:
            print(feedback(computer_choice, guess))
            print(no_guesses(attempts, i))

print('Let me think of a number between 1 to 50.')
num_list = list(range(1, 51))
computer_choice = random.choice(num_list)
name= input("Enter your name: ")
while True:
    try:
        attempts = int(input("Challenge! How many attempts do you need to guess the number? "))
        guess_number(computer_choice, attempts)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number of attempts.")
