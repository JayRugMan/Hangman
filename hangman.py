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
                       'i love being a mormon',
                       'this is only a test', 
                       'isaiah is awesome',
                       'elijah is awesome', 
                       'suze and me forever',]
    
    int_num_of_word_phrases = len(list_word_Phrases)
    int_random_picker = random.randint(0, (int_num_of_word_phrases - 1))
    str_word_Phrase = list_word_Phrases[int_random_picker]
    
    return str_word_Phrase

        
# Creates a string with all blanks for the random word:
def add_blank(list_wordPhrase):
    list_blanks = []
    for letter in list_wordPhrase:
            if letter.isalpha():
                    list_blanks.append('-')
            else:
                    list_blanks.append(' ')
    str_blanks = ''.join(list_blanks)
    return str_blanks


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
def draw_gallows(int_wrong_guess_count, list_hung_man):
    
    int_wgm1 = int_wrong_guess_count - 1
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
    
    if len(list_hung_man) < int_wrong_guess_count:
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
def update_final_word(str_user_guess, 
                        str_final_word, 
                        str_word_Phrase):
    
    list_final_word = list(str_final_word)
    list_word_Phrase = list(str_word_Phrase)
    iteration_bit = 0
    
    for letter in list_word_Phrase:
        if str_user_guess == letter:
            list_final_word[iteration_bit] = str_user_guess
        iteration_bit += 1
    
    str_final_word = ''.join(list_final_word)
    
    return str_final_word
    

# User guesses a letter
def guess(str_word_Phrase, 
          int_wrong_guess_count, 
          list_wrong_guesses,
          str_final_word):
    
    str_user_guess = ''
    str_wrong_guesses = '-'
    
    for letter in list_wrong_guesses:
        str_wrong_guesses = str_wrong_guesses + letter + '-'
    
    print('\n\tIncorrect letters guessed: %s' % str_wrong_guesses)
    
    # only one letter can be entered to exit loop
    while len(str_user_guess) != 1:
        str_user_guess = raw_input('\n  Guess a letter: ')
    
    # if guess is wrong, and not already guessed
    # then add to wrond guesses
    if (str_user_guess not in str_word_Phrase and 
        str_user_guess not in list_wrong_guesses):
        int_wrong_guess_count += 1
        list_wrong_guesses.append(str_user_guess)
    
    # if guess is right, add it to final word
    elif (str_user_guess in str_word_Phrase and
          str_user_guess not in str_final_word):
          str_final_word = update_final_word(str_user_guess,
                                             str_final_word, 
                                             str_word_Phrase)
    
    return (int_wrong_guess_count, 
            list_wrong_guesses, 
            str_final_word)


# Print the winning Screen
def print_winning_screen(str_final_word):
    
    list_free_man = ['\t\t\t          () ', 
                     '\t\t\t          /|\ ', 
                     '\t\t\t         e | o ', 
                     '\t\t\t          / \ ', 
                     '\t\t\t          | | ', 
                     '\t\t\t          J J ']
    
    # Clears the screen and prints title
    os.system('cls' if os.name == 'nt' else 'clear')
    print_title()
    
    for line in list_free_man:
        print(line)
    
    
    print('\n\t\tThe correct phrase was "%s"!\n' % str_final_word)
    print('\tWinner Winner, Chicken Dinner - you saved a man from hangin')


def main():

    hung_man = []
    wrong_guess_count = 0
    word_Phrase = initialize_wordPhrase()
    final_word = add_blank(word_Phrase)
    wrong_guesses = []
    won = False
    
    print word_Phrase
    
    # loop may play screen and print updates
    while wrong_guess_count <= 12 and won is False:
        # Clears the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print_title()
        
        # Updates and prints the hanging man
        hung_man = draw_gallows(wrong_guess_count, hung_man)
        print_hungman(hung_man)
        
        # Adds correctly-guessed letters to final word and
        # prints it
        final_word
        print('\n\t\t    ' + final_word)
        
        # This skips asking for a guess if the man is hung
        # while still allowing the hanging man to still show
        if wrong_guess_count < 12:
            (wrong_guess_count, 
             wrong_guesses, 
             final_word) = guess(word_Phrase, 
                                 wrong_guess_count,
                                 wrong_guesses, 
                                 final_word)
        else:
            break
        
        # won becomes true once all of the correct letters are guessed
        # and the winning screen prints
        if final_word == word_Phrase:
            won = True
            print_winning_screen(final_word)
        
        print('\n\n')

    print('\n\n')


main()