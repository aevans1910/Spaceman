#I would like to thank Meredith Murphy for helping touch up my is_word_guessed function, 
# Jess Dahmen for helping me fix a bug within my load_word function, this video 
# (https://www.youtube.com/watch?v=jPmBUoSZ6tY)for giving me an idea of where I should go with this project,
# and Ricky Nguyen, George Aoyagi, and Ben Lafferty for helping with everything in this project

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

    words_list = words_list[0].split(' ')
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

    display = ""

    for i in secret_word:
        if i in letters_guessed:
            display += i
        else:
            display += "_"
    return display

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''

    return guess in secret_word

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''

    print ('Hello and welcome to Space Man! For this game we will think of a secret word for you and you will need to guess the letters in the word! You get 7 guesses, if by then you can correctly guess the word, then congrats! Otherwise, you lose.')

    letters_guessed = []

#A function that will chose the amount of lives depending on the length of the secret word
    if len(secret_word) >= 3 and len(secret_word) <= 7:
        life = len(secret_word) + 1
    elif len(secret_word) < 3:
        life = len(secret_word) + 2
    elif len(secret_word) >= 9:
        life = len(secret_word) - 1
    else:
        life = len(secret_word)

#Runing the game
    while life > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print ("Here is your word so far: " + get_guessed_word(secret_word, letters_guessed))
        print ("Lives left: " + str(life))
        guess = input ('Guess a letter! ')
        print("Your guess: " + guess)
        print ("Past guesses: " + str(letters_guessed))
        letters_guessed.append(guess)

        correct = is_guess_in_word(guess, secret_word)
        if correct:
            print ('Good job! Good guess :)')
        else:
            print ('Sorry, incorrect guess :(')
            life -= 1

        is_word_guessed (letters_guessed, secret_word)

    if life == 0:
        print ('Sorry, you lose. Your word was: ' + secret_word)
    if is_guess_in_word == True:
        print ('Good job! :)')

secret_word = load_word()
spaceman(secret_word) 

def test_spaceman():
    assert is_guess_in_word("a", "cat") == True
    assert is_guess_in_word("b", "cat") == False
    assert is_word_guessed(["a", "c", "t"], "cat") == True
    assert is_word_guessed(["a", "b", "t"], "cat") == True, "Word is not guessed"
    assert get_guessed_word("cat", ["a", "t", "b"]) == "_at"


if __name__ == "__main__":
    test_spaceman()