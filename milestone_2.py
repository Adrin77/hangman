
import random
word_list = ['apple', 'orange', 'lemon', 'watermelon', 'pear']
word=random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print('Good guess! {} is in the word'.format(guess))
    else:
         print('Sorry, {} is not in the word. Try again'.format(guess))

def ask_for_input():
    while True:
        guess = input('Enter a single letter ')
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

    check_guess(guess)


ask_for_input()
       



        


