import random

def ask_for_int():
    while True:
        try:
            guess = int(input('Guess the number: '))
        except:
            print('The input needs to be an integer')
        else:
            return guess

while True:
    
    print('Guess the number between 1 and 100')
    secret_number = random.randrange(1, 101)
    guess = ask_for_int()
    counter = 0

    while guess != secret_number:
        counter += 1
        if guess > secret_number:
            print('Too high')
        elif guess < secret_number:
            print('Too low')
        guess = ask_for_int()

    print('Correct!!')
    print(f'It took you {counter} guesses')
    play_again = input('Would you like to play again? (y/n): ')
    
    while play_again != 'y' and play_again != 'n':
       play_again = input('Please input y or n: ')

    if play_again == 'n':
        break
    else:
        pass
    

