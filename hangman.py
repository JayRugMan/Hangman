# hangman.py
""" Version 1.1 - Defining functions
- 
"""

import os
import sys
import random
import time

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



# Prints the games title in ascii art:
def print_title():

    # requires file ascii_title.txt
    # See Zimm3r's anwer in
    # https://stackoverflow.com/questions/4060221
    absolute_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    absolute_path_2_title_file = absolute_path + '/' + 'ascii_title.txt'
    
    with open(absolute_path_2_title_file, 'r') as title:
        print title.read()

    
    
# draws more of the gallows as each guess is incorrect
def draw_gallows(int_wrong_guesses, list_hung_man):
    
    int_wgm1 = int_wrong_guesses - 1
    list_hanging_man = ['\t\t    =================', 
                       '\t\t\t||', 
                       '\t\t\t||', 
                       '\t\t\t||', 
                       '\t\t\t||        J J', 
                       '\t\t\t||        | |', 
                       '\t\t\t||        / \\', 
                       '\t\t\t||       e | o', 
                       '\t\t\t||        /|\\', 
                       '\t\t\t||        ()', 
                       '\t\t\t|/         |', 
                       "\t\t   He's hung, you lost!\n\n\t\t\t+==========|"]
    
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

        
# Builds the word with correct guesses
# def build_word(str_user_guess, list_correct_guesses):
        
    
# User guesses a letter
def guess(str_word_Phrase, 
          int_wrong_guesses, 
          list_guessed_letters):
    
    str_user_guess = ''
    str_guessed_letters = '-'
    
    for letter in list_guessed_letters:
        str_guessed_letters = str_guessed_letters + letter + '-'
    
    print('\n\tIncorrect letters guessed: %s' % str_guessed_letters)
    
    # only one letter can be entered to exit loop
    while len(str_user_guess) != 1:
        str_user_guess = raw_input('\n  Guess a letter: ')
    
    if (str_user_guess not in str_word_Phrase and 
        str_user_guess not in list_guessed_letters):
        int_wrong_guesses += 1
        list_guessed_letters.append(str_user_guess)
        
    return (int_wrong_guesses, list_guessed_letters)

    
def main():

    hung_man = []
    wrong_guesses = 0
    word_Phrase = initialize_wordPhrase()
    guessed_letters = []
    correct_guesses = []
    won = False
    
    print word_Phrase
    
    while wrong_guesses <= 12 and won is False:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_title()
        
        hung_man = draw_gallows(wrong_guesses, hung_man)
        print_hungman(hung_man)
        
        # This skips asking for a guess if the man is hung
        # while still allowing the hanging man to still show
        if wrong_guesses < 12:
            (wrong_guesses, 
             guessed_letters) = guess(word_Phrase, 
                                      wrong_guesses,
                                      guessed_letters)
        else:
            break
        
        print('\n\n')

    print('\n\n')


main()