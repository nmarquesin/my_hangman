# implement of the hangman game from
# The word game Hangman based on 'Invent
# Your Own Computer Games with Python'
# http://inventwithpython.com/chapter9.html
# for Python 2.7 instead of Python 3
#
# by nmarquesin@live.com
#

import random
HANGMANPICS = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']
words = {0: 'Ant', 1: 'Baboon', 2: 'Badger',
    3: 'Bat', 4: 'Bear', 5: 'Beaver',
    6: 'Camel', 7: 'Cat'}

victoria = {'Name': 'victoria',
    'Tip_1': 'Lalala',
    'Tip_2': 'Lalala',
    'Tip_3': 'Lalala'
    }
edward = {'Name': 'edward',
    'Tip_1': 'Lalala',
    'Tip_2': 'Lalala',
    'Tip_3': 'Lalala'
    }
george = {'Name': 'george',
    'Tip_1': 'Lalala',
    'Tip_2': 'Lalala',
    'Tip_3': 'Lalala'
    }

royals = {0: victoria, 1: edward, 2: george}

"""
def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]
"""

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]['Name']

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print HANGMANPICS[len(missedLetters)]
    print ""
    end = ' '
    wordis = ''
    print'Missed letters:', end
    for letter in missedLetters:
        wordis += letter + end
    print wordis
    print ""

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    wordis = ''
    for letter in blanks: # show the secret word with spaces in between each letter
        wordis += letter + end
    print wordis
    print ""

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print 'Guess a letter.'
        guess = raw_input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ""
correctLetters = ""
#secretWord = getRandomWord(words)
secretWord = getRandomWord(royals) #test
gameIsDone = False
print secretWord

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            # secretWord = getRandomWord(words)
            secretWord = getRandomWord(royals) #test
        else:
            break
