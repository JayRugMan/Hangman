# hangman.py
""" Version 1.1 - Defining functions
- 
"""

import os
import sys
import random

# lists the files containing words or phrases
# def list_wordPhrase_lists(str_absolute_path):

    # Gets list of files with .hmwl extension
    # Loops thorugh files, numbering each
    # displays numbers and prompts for a selection

# Initializes a list of words/phrases for 
# player to guess
def initialize_wordPhrase(str_absolute_path):
    
    # Requires wordList files
    str_word_file = str_absolute_path + '/' + 'wordList_1.hmwl'

    # Opens a file in the same directory and makes a list of words
    # from each line of that file
    with open(str_word_file, 'r') as words:
        list_word_Phrases = [line.strip() for line in words]
    
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
def print_title(str_absolute_path):

    # requires file ascii_title.txt
    str_title_file = str_absolute_path + '/' + 'ascii_title.txt'
    
    with open(str_title_file, 'r') as title:
        print title.read()

    
# draws more of the gallows as each guess is incorrect
def draw_gallows(int_wrong_guess_count, list_hung_man):
    
    int_wgm1 = int_wrong_guess_count - 1
    list_hanging_man = ['\t    =================', 
                        '\t\t||', 
                        '\t\t||', 
                        '\t\t||        J J', 
                        '\t\t||        | |', 
                        '\t\t||        / \\', 
                        '\t\t||       e | o', 
                        '\t\t||        /|\\', 
                        '\t\t||        ()', 
                        '\t\t|/         |', 
                        "\t   He's hung, you lost!\n\n\t\t+==========|"]
    
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
    
    # creates a string of wrong guesses with dashes 
    # between the letters in list of wrong guesses
    for letter in list_wrong_guesses:
        str_wrong_guesses = str_wrong_guesses + letter + '-'
    
    print('\n\tIncorrect letters guessed: \n\t%s' % str_wrong_guesses)
    
    # only one letter can be entered to exit loop
    while len(str_user_guess) != 1:
        str_user_guess = raw_input('\n\tGuess a letter: ')
    
    # if guess is wrong, and not already guessed
    # then adds to wrong guesses
    if (str_user_guess not in str_word_Phrase and 
        str_user_guess not in list_wrong_guesses):
        int_wrong_guess_count += 1
        list_wrong_guesses.append(str_user_guess)
    
    # if guess is right, adds it to final word
    elif (str_user_guess in str_word_Phrase and
          str_user_guess not in str_final_word):
          str_final_word = update_final_word(str_user_guess,
                                             str_final_word, 
                                             str_word_Phrase)
    
    return (int_wrong_guess_count, 
            list_wrong_guesses, 
            str_final_word)


# Print the winning Screen
def print_winning_screen(str_final_word, str_absolute_path):
    
    list_free_man = ['\t        O () ', 
                     '\t         \/|\ ', 
                     '\t           | o ', 
                     '\t          / \ ', 
                     '\t          | | ', 
                     '\t          d L ', 
                     '\t===============']
    
    # Clears the screen and prints title
    os.system('cls' if os.name == 'nt' else 'clear')
    print_title(str_absolute_path)
    
    for line in list_free_man:
        print(line)
    
    
    print('\n The correct phrase was "%s"!\n' % str_final_word)
    print(' Winner Winner, Chicken Dinner \n You saved a man from hangin\'!')


def main():
    
    # See Zimm3r's answer in
    # https://stackoverflow.com/questions/4060221
    absolute_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    
    hung_man = []
    wrong_guess_count = 0
    word_Phrase = initialize_wordPhrase(absolute_path)
    final_word = add_blank(word_Phrase)
    wrong_guesses = []
    won = False
    
    # loop play screen and print updates 
    # until man is hung or word is guessed
    while wrong_guess_count <= 11 and won is False:
        
        # Updates the hanging man
        hung_man = draw_gallows(wrong_guess_count, hung_man)
        
        # Clears the screen and prints updated values
        os.system('cls' if os.name == 'nt' else 'clear')
        print_title(absolute_path)
        print_hungman(hung_man)
        print('\n\t    ' + final_word)
        
        # This skips asking for a guess if the man is hung
        # while still allowing the hanging man to print
        if wrong_guess_count < 11:
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
            print_winning_screen(final_word, absolute_path)
        
        print('\n\n')

    print('\n\n')


main()
