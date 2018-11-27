import random
from guess import Guess

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        self.wordLength = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1
            if self.wordLength < len(word):
                self.wordLength = len(word)

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self,minLength):

        r = random.randrange(self.count)

        while True :
            if len(self.words[r]) >= minLength:
                return self.words[r]

