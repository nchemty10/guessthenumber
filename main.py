import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f' Guess a number between 1 and {x}:  '))
        if guess < random_number:
            print('Sorry mah dude, low ball')
        elif guess > random_number:
            print('Almost mah dude, overdid it')

    print(f'Woo bacc baby, im jackin it. Thats a fact , number {random_number} was valid')
        

guess(10)