# Hangman game
# Author: A. Kashinath

import random

# file containing word list is hard-coded
# TO-DO: change to accept any file
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """        
    Returns a list of valid words. Words are strings of lowercase letters.    
    """
    print("Loading word list from file...")
    # inFile: file (that contains the word list)
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words/strings

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    Function to check if the player has guessed the word correctly
    
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in 
             lettersGuessed; False otherwise
    '''
    listSecretWord = list(secretWord)
    
    for l in listSecretWord:
        if l not in lettersGuessed:
            return False
    
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    Create string using the letters of the secret word that have been guessed 
    so far and underscores to represent the hidden letters
    
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
 
    listWord = list(secretWord)
    for ic in range(len(listWord)):
        if listWord[ic] not in lettersGuessed:
            listWord[ic] = '_ '
    
    return ''.join(listWord)

def getAvailableLetters(lettersGuessed):
    '''
    Create string with letters that can still be chosen by the player
    
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    import string
    
    allAlphabets = list(string.ascii_lowercase)
    
    for l in lettersGuessed:
        allAlphabets.remove(l)
        
    return ''.join(allAlphabets)

def hangman(secretWord):
    '''
    Starts up an interactive game of Hangman.

    1. At the start of the game, let the user know how many 
      letters the secretWord contains.

    2. Ask the user to supply one guess (i.e. letter) per round.

    3. The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    4. After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    secretWord: string, the secret word to guess.
    '''
    import string
    
    numGuess = 8
    availLetters = ''.join(string.ascii_lowercase)
    lettersGuessed = []
    guessedWord = getGuessedWord(secretWord, lettersGuessed)

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')
    
    while (not isWordGuessed(secretWord, lettersGuessed)) and (numGuess > 0):
        print('You have ' + str(numGuess)+ ' guesses left.')
        print('Available letters: ' + availLetters)
        
        guess = input('Please guess a letter: ').lower()
        
        if guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter:' + 
                  guessedWord)
            print('-------------')
        else:
            lettersGuessed.append(guess)
            availLetters = getAvailableLetters(lettersGuessed)
            if guess in list(secretWord):
                guessedWord = getGuessedWord(secretWord, lettersGuessed)
                print('Good guess: ' + guessedWord)
                print('-------------')
            else:
                numGuess -= 1
                print('Oops! That letter is not in my word: ' + guessedWord)
                print('-------------')
    
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')


# testing 
secretWord = 'testing'
hangman(secretWord)

# running
# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
