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

victoria = {'Name': 'victoria',
    1: 'Tip 1: She was a Queen.',
    2: "Tip 2: She inherited the throne aged 18.",
    3: 'Tip 3: She was raised under close supervision by her German-born mother.',
    4: 'Tip 4: She was the daughter of Prince Edward, Duke of Kent and Strathearn.',
    5: 'Tip 5: Her reign of 63 years and seven months is known as the Victorian era.'
    }
edward = {'Name': 'edward',
    1: 'Tip 1: He was a King.',
    2: 'Tip 2: He came to be known as the "uncle of Europe".',
    3: 'Tip 3: He was fluent in French and German.',
    4: 'Tip 4: He habitually smoked twenty cigarettes and twelve cigars a day.',
    5: 'Tip 5: He died in 1910 in the midst of a constitutional crisis.'
    }
george = {'Name': 'george',
    1: 'Tip 1: He was a King.',
    2: 'Tip 2: He received lessons in constitutional history from J. R. Tanner.',
    3: 'Tip 3: He inherited the throne at a politically turbulent time.',
    4: 'Tip 4: He became the first monarch of the House of Windsor.',
    5: 'Tip 5: He died aged 70.'
    }

royals = {0: victoria, 1: edward, 2: george}


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]['Name'], wordIndex

def tips(missedLetters, royalIndex):
    if len(missedLetters) == 6:
        return
    else:
        num = 0
        for letter in missedLetters:
            num += 1
            print royals[royalIndex][num]
        return

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord, royalIndex):
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

    tips(missedLetters, royalIndex)

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
secretWord, code = getRandomWord(royals)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord, code)

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
            print('Yes! The secret royal is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord, code)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, code = getRandomWord(royals)
        else:
            break
