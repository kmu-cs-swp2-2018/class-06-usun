import random

class Word:
    def __init__(self, filename):
        # 파일을 읽어서 단어 데이터베이스 초기화한 다음, 파일 닫음
        self.words = []
        file = open(filename, 'r')
        lines = file.readlines()     # 행별로 구분
        file.close()

        for line in lines:
            word = line.rstrip()    # 오른쪽 공백 제거
            self.words.append(word)

    def randFromDB(self):
        # word.txt에서 임의의 개수만큼 임의의 단어들을 선택
        randWords = []
        randInt = random.randrange(5,11)
        for i in range(randInt):
            randWords.append(self.words[random.randrange(len(self.words))])
        return randWords

if __name__ == '__main__':
    word = Word("words.txt")
    print(word.randFromDB())
    print(word.randFromDB())
    print(word.randFromDB())
