import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('adivinhe um entre o número 1 e {}: '.format(x)))
        if guess < random_number:
            print('Sinto muito, você errou. Muito baixo')
        elif guess > random_number:
            print('Sinto muito, você errou. Muito alto')

    print('Aeee, parabens. {} era o número correto!!'.format(random_number))

guess(10)