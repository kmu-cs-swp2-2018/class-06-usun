from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())        # 랜덤하게 단어 선택
    hangman = Hangman()
    maxTries = hangman.getLife()        # 최대 시도 횟수

    while guess.numTries < maxTries:        # 목숨이 남아있을 때

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
# guess.haveGuess char()...?
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        # 한글, 영어 대문자, 기호, 숫자를 입력했을 경우 : 아스키코드로 판별
        if guessedChar != (guessedChar.lower() or guessedChar.isalpha()):
            print('Please input in English lower case')
            continue

        if guess.guess(guessedChar):
            break

    if (maxTries - guess.numTries) > 0:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()