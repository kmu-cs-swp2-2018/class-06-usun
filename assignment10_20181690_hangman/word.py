class Word:
    def __init__(self, filename):
        # 파일을 읽어서 단어 데이터베이스 초기화한 다음, 파일 닫음
        self.word = []
        file = open(filename, 'r')
        lines = file.readline()
        file.close()

    def randFromDB(self):
        # word.txt에서 임의의 단어를 선택
        pass

