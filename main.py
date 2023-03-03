import random

def loadWords(level):

  if level == 0:
    inputFile = open('wordsEasy.txt', 'r')

  if level == 1:
    inputFile = open('wordsMedium.txt', 'r')

  if level == 2:
    inputFile = open('wordsHard.txt', 'r')


  wordString = inputFile.read()
  wordList = wordString.split('\n')
  inputFile.close()

    
  return wordList

def pickWord(wordList):
  return int(random.randint(0, len(wordList)))

def checkLetter(secretWord, mistakesMade):

  if mistakesMade == 8:
    return None, None, None

  #First need to check whether the word is of the right length (aka 1 letter only)
  guess = guessLetter()

  word_as_list = list(secretWord)

  try:
    #if the guess is not in the word
    assert guess in word_as_list, 'Wrong guess! You have %i attempts left!' %(7-mistakesMade)
    correctPos = []
    for val, i in enumerate(word_as_list):
      if guess == i: correctPos.append(val)
    return guess, correctPos, mistakesMade

  except AssertionError as msg:
    print(msg)
    mistakesMade += 1
    return checkLetter(secretWord, mistakesMade)

guessedLetters = []

def guessLetter():
  #Check whether the length of guess is correct
  try:    
    guess = input('Guess a letter: ')
    assert len(guess) == 1, 'You have entered more than one letter! Please try again!'
    #Check if the letter has been guessed before
    if guess not in guessedLetters:
      guessedLetters.append(guess)
    elif guess in guessedLetters:
      print('You have already guessed this letter! Try again!')
      return guessLetter()
    return guess
  except AssertionError as msg:
    print(msg)
    return guessLetter()


def gameplay(level, admin = False):
  words = loadWords(level)
  secretWord = words[pickWord(words)]

  if admin == True:
    print(secretWord)

  outDash = []
  for i in range(len(secretWord)):
    outDash.append('_')
  outDash_s = ''.join(outDash)
  print(outDash_s)

  mistakesMade = 0  
  while True:

      guess, correctVals, mistakesMade = checkLetter(secretWord, mistakesMade)
      if mistakesMade == None:
        print('Unfortunately you have no attempts left!! The word was %s.' %secretWord)
        exit()
      else:
        for i in correctVals:
          outDash[i] = guess
      outDash_s = ''.join(outDash)
      print(outDash_s)

      outDash_s_list = list(outDash_s)
      if '_' not in outDash_s_list:
        print('Congratulations! You guessed the word correctly!')
        exit()


def main():
  levelS = input('Please select your level (Easy/Medium/Hard) (For now there is only Easy): ')
  if levelS == 'easy' or levelS == 'Easy': gameplay(0)
  elif levelS == 'medium' or levelS == 'Medium': gameplay(1)
  elif levelS == 'hard' or levelS == 'Hard': gameplay(2)
  elif levelS == 'test' or levelS == 'Test': gameplay(0, admin = True)

  else:
    print('You have entered an incorrect difficulty! Please try again!')
    main()

if __name__ == '__main__':
  print('Welcome to Hangman!')
  main()