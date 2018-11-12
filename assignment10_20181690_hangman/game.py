from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())        # 랜덤하게 단어 선택

    finished = True
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
        if chr(97) > chr(ord(guessedChar)) or chr(122) < chr(ord(guessedChar)): # 아스키코드 99~122 가 영어 소문자
            print('Please input in English lower case')
            continue

# 플래그 변수 없엘려고 노력해야 됨
        if finished == guess.guess(guessedChar):
            break

    if finished == guess.guess(guessedChar):
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()