#I would like to thank Meredith Murphy for helping touch up my is_word_guessed function and this video 
# (https://www.youtube.com/watch?v=jPmBUoSZ6tY)for giving me an idea of where I should go with this project,
# and Ricky Nguyen and George Aoyagi for helping with everything in this project

import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    # words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    counter = 0
    for i in secret_word:
        if i in letters_guessed:
            counter += 1
    
    if counter == len(secret_word):
        return True 
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    display = ""
    #display.extend(secret_word)

    for i in secret_word:
        if i in letters_guessed:
            display += i
        else:
            display += "_"
    return display

#Test function
print(get_guessed_word("cat","ca"))

       # display[i] = ("_")


    # for letter in secret_word:
    #     if letters_guessed == letter:
    #         print (letter) in display
    #     else: 
    #         return letters_guessed 


#loop through secret word
    #check if letters guessed



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word


    return guess in secret_word


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''


    #TODO: show the player information about the game according to the project spec

    print ('''Hello and welcome to Space Man! For this game we will think of a secret word for you 
              and you will need to guess the letters in the word! You get 7 guesses, if by then you can correctly guess the word,
              then congrats! Otherwise, you lose.''')

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    letters_guessed = []
    life = 3
    while life > 0 and is_word_guessed == False:
        guess = input ('''Guess a letter! ''')
        letters_guessed.append(letters_guessed)

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        correct = is_guess_in_word(guess, secret_word)
        if correct:
            print ('''Good job! Good guess''')
        else:
            print ('''Sorry, incorrect guess :(''')
            life -= 1

        #TODO: show the guessed word so far
        print (get_guessed_word(secret_word, letters_guessed))

        #TODO: check if the game has been won or lost
        is_word_guessed (letters_guessed, secret_word)

    if life == 0:
        print ('''Sorry, you lose''')
    if is_guess_in_word == True:
        print ('''Good job!''')

# These function calls that will start the game

secret_word = load_word()
spaceman(secret_word) 