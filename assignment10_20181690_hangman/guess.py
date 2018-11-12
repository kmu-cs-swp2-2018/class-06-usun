from hangman import Hangman

class Guess:

    def __init__(self,word):
        # 비밀로 선택된 단어를 기록
        # 이미 추측했던 문자들을 저장할 리스트 초기화
        # 추측 실패 횟수 기록을 위한 변수 초기화
        # 알아낸 글자들과 그 위치 가리키는 데이터를 초기화
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0  # 실패횟수
        self.remainingTries = 0       # 남은 횟수를 볼 수 있게
        self.currentStatus = '*' * len(word)        # secretWord 글자 수 볼 수 있게 * 추가

    def display(self):
        # 알아낸 문자들과 그 위치 가리키는 데이터를 화면에 출력
        # 이미 시도한 문자들을 출력
        # 추측 실패 횟수를 화면에 출력
        print("Current : ", self.currentStatus)
        self.guessedChars.sort()        # 이미 시도한 글자 들을 순서대로 볼 수 있게 정렬
        print("Already tried : ", self.guessedChars)
        self.remainingTries = (len(Hangman.draw) - 1) - self.numTries
        print("Tries : ", self.numTries, '\t\t\t\tRemaining Tries : ', self.remainingTries)

    def guess(self,character):
        # 입력한 문자를 리스트에 추가
        # 비밀단어에 입력한 문자가 없으면 실패 횟수 증가
        # 알아낸 문자와 그 위치를 가리키는 데이터 갱신
        # 단어를 맞췄는지 리턴
        self.guessedChars.append(character)
        if character not in self.secretWord:
            self.numTries +=1
        else:
            for i in range (len(self.secretWord)):
                if character == self.secretWord[i]:
                    self.currentStatus = self.currentStatus[:i]+ character + self.currentStatus[i+1:]

            if self.currentStatus == self.secretWord:
                result = True
            else:
                result = False

            return result
