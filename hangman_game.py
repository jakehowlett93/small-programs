import random

already_guessed = ''
word_list = ['heineken', 'mouse', 'popcorn']
play_game = True

def guess_letter():

    # verifies that user input is a letter and that it hasnt been input before

    while True:
        guess = input('Guess a letter: ')
        if guess in already_guessed:
            print("You've already guessed that letter")
        elif guess.isalpha():
            return guess
        else:
            print('Please enter a letter!')
            continue

while play_game == True:

    lives = 11
    secret_word = random.choice(word_list)

    print('--Welcome to Hangman!--')
    print('Try to guess the word correctly.')
    print('You begin with 11 lives')

    while lives > 0:

        
        guess = guess_letter()
        display_word = ''
        already_guessed += guess

        if guess in secret_word:
            print('Correct!')
            # for each character in the secret_word if the character has already been guessed then display it otherwise show '-'
            for char in secret_word:
                if char in already_guessed:
                    display_word = display_word + char
                else:
                    display_word = display_word + '-'
            print(display_word)
        else:
            print('Unlucky!')
            lives -= 1
            print(f'{lives} lives remaining')
        
        if display_word == secret_word:
            break
        else:
            pass


    if lives == 0:
        print("You've run out of lives!")
    else:
        print('Congratulations! You win!')

    play_again = input('Would you like to play again? (y/n): ')

    if play_again == 'y':
        continue
    else:
        print('Thanks for playing!')
        play_game = False


        