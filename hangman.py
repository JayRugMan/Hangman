# hangman.py
""" Version 1.1 - Defining functions
- Issue in the order of the screen clear,
    gallows drawing, and guess fundtion calls
    in while loop
    - even after losing, a guess is prompted
"""

import os
import random

# Initializes a list of words/phrases for 
# player to guess
def initialize_wordPhrase():
    list_word_Phrases = ['python is fun', 
                       'hello world', 
                       'I love being a Mormon',
                       'This is only a test', 
                       'Isaiah is awesome',
                       'Elijah is awesome', 
                       'Suze and me forever',]
    
    int_num_of_word_phrases = len(list_word_Phrases)
    int_random_picker = random.randint(0, (int_num_of_word_phrases - 1))
    str_word_Phrase = list_word_Phrases[int_random_picker]
    
    return str_word_Phrase


# draws more of the gallows as each guess is incorrect
def draw_gallows(int_wrong_guesses, list_hung_man):
    
    int_wgm1 = int_wrong_guesses - 1
    list_hanging_man = ['    =================', 
                       '\t||', 
                       '\t||', 
                       '\t||', 
                       '\t||        J J', 
                       '\t||        | |', 
                       '\t||        / \\', 
                       '\t||       e | o', 
                       '\t||        /|\\', 
                       '\t||        ()', 
                       '\t|/         |', 
                       "   He's hung, you lost!\n\n\t+==========|"]
    
    if len(list_hung_man) < int_wrong_guesses:
        list_hung_man.append(
            list_hanging_man[int_wgm1]
            )
    
    return list_hung_man
    
    
# Prints out the hanging man, lines 
# equal to the number of wrong guesses
def print_hungman(list_hung_man):
    for line in reversed(list_hung_man):
        print line

    
# User guesses a letter
def guess(str_word_Phrase, int_wrong_guesses):
    
    str_user_guess = ''
    
    while len(str_user_guess) != 1:
        str_user_guess = raw_input('\n  Guess a letter: ')
    
    if str_user_guess not in str_word_Phrase:
        int_wrong_guesses += 1
    
    return int_wrong_guesses

    
def main():

    hung_man = []
    wrong_guesses = 0
    word_Phrase = initialize_wordPhrase()
    won = False
    
    print word_Phrase
    
    while wrong_guesses <= 12 and won is False:
        os.system('cls' if os.name == 'nt' else 'clear')
        hung_man = draw_gallows(wrong_guesses, hung_man)
        print_hungman(hung_man)
        wrong_guesses = guess(word_Phrase, wrong_guesses)
        print('\n\n')


main()