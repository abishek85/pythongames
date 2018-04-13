# Words with Friends
# Author: A. Kashinath

import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, \
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,\
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords(inputFile):
    """        
    Reads a file containing words that are strings of lowercase letters.
    
    inputFile: srting indicating the location of the input file
    returns: a list of valid words.
    """
    print("Loading word list from file...")
    # inFile: file (that contains the word list)
    inFile = open(inputFile, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
        
    # close the file
    inFile.close()

    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integers to count the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    returns: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    # if letter exists increment by 1, else add new key and then increment by 1
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE required for additional points)
    returns: int (score >= 0)
    """
    wordScore = 0
    
    if word == '':
        wordScore = 0
    else:
        # calculate how many times a letter appears in the word
        frequency = getFrequencyDict(word)
        # calculate word score as a sum of the product number of letters and 
        # score of each letter
        for letter in frequency.keys():
            wordScore += frequency[letter]*SCRABBLE_LETTER_VALUES[letter]            
        wordScore *= len(word)
    # Bonus if all the letters are used
    if len(word) == n:
        wordScore += 50
    
    return wordScore

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1}) prints out
        a x x l l l e

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for i in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print empty line

def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    # select vowels at random
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    # select remaining letters from consonants  
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    It does not modify hand.

    hand: dictionary (string -> int)    
    word: string
    returns: dictionary (string -> int)
    """
    rem_hand = hand.copy()
    # get num of occurences of each letter in word
    frequency = getFrequencyDict(word)
    # subtract this from hand
    for letter in frequency.keys():
        rem_hand[letter] = rem_hand.get(letter) - frequency.get(letter)
        
    return rem_hand

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # first check if letters in word are in hand
    handCopy = hand.copy()
    
    for letter in word:
        handCopy[letter] = handCopy.get(letter,0)-1
        if (handCopy[letter] < 0):
            return False
        
    # second check if word belongs to wordList
    if (word.lower() in wordList):
        return True
    else:
        return False

def calculateHandLen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    sum = 0
    for item in hand.keys():
        sum += hand[item]
    
    return sum


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    total_score = 0
    remaininghand = hand.copy()
    
    # As long as there are still letters left in the hand:
    while (calculateHandLen(remaininghand) > 0):
    
        # Display the hand
        displayHand(remaininghand)
        
        # Ask user for input
        word = input('Enter word, or a "." to indicate that you are finished: ')
        
        # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            break          
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(word, remaininghand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.')
                print('\n')
            # Otherwise (the word is valid):
            else: 
                 
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = getWordScore(word, n)
                total_score += score
                print('"'+word+'" earned '+str(score)+" points. Total: "+str(total_score)+" points")
                print('\n')
                # Update the hand 
                remaininghand = updateHand(remaininghand,word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if word == '.':
        print('Goodbye! Total score:' + str(total_score) + ' points.')
    else:
        print('Ran out of letters. Total score:' + str(total_score) + ' points.')

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    currentHand = {}
    toPlay = True
        
    while toPlay:
        # ask for user input
        playChoice= input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        
        if playChoice == 'n':
            # deal a new hand and play it
            currentHand = dealHand(HAND_SIZE)
            playHand(currentHand, wordList, HAND_SIZE)           
        elif playChoice == 'r':
            # if currentHand is empty ask user to re-input data
            if currentHand == {}:
                print('You have not played a hand yet. Please play a new hand first!')
            # else play the last hand again
            else:
                playHand(currentHand, wordList, HAND_SIZE)
        elif playChoice == 'e':
            # exit the game
            toPlay = False
        else:
            # invlaid input
            print('Invalid command.')
        

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords(WORDLIST_FILENAME)
    playGame(wordList)
