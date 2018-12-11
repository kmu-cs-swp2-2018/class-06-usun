from word import Word
import random
import time

class SearchWord:

    def __init__(self):
        self.word = Word('words.txt')

        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                   'h', 'i', 'j', 'k', 'l', 'm', 'n',
                   'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z']

        self.stringList = []
        self.searchedList = []

    def newGame(self):
        self.startTime = time.time()
        for i in range(10):
            string = ""
            for j in range(31):
                string += self.alphabet[random.randrange(len(self.alphabet))]
            self.stringList.append(string)

        num = []
        self.answerDic = {}
        self.randWords = self.word.randFromDB()
        print(self.randWords)
        for k in range(len(self.randWords)):
            while(True):
                (i, j) = (random.randrange(10), random.randrange(31))
                if ( (i, j), (i, j+len(self.randWords[k])), (i, j-1), (i, j+1) ) not in num:
                    if (j + len(self.randWords[k]) < 31):

                        self.stringList[i] = self.stringList[i][:j] + self.randWords[k]\
                                             + self.stringList[i][j+len(self.randWords[k]):]
                        self.answerDic[self.randWords[k]] = (i,j)
                        for n in range(len(self.randWords[k])):
                            num.append((i,j + n))
                        break

    def searching(self, word):
        if word in self.randWords:
            self.randWords.remove(word)
            self.searchedList.append(word)
            (i, j) = self.answerDic[word]
            self.stringList[i] = self.stringList[i][:j] + "*" * len(word)\
                + self.stringList[i][j+len(word):]
            return True
        return False

    def getDisplay(self):
        string = ""
        for i in range(10):
            st = ""
            for c in self.stringList[i]:
                st = st + c + " "
            string = string + st + "\n"
        print(string)
        return string

    def getTimeMessage(self):
        measuredTime = time.time() - self.startTime
        print(measuredTime)
        if measuredTime < 90:
            message = "Wow! You are the best\n\n" + str(measuredTime)
        elif measuredTime < 180:
            message = "excellent!\n\n" + str(measuredTime)
        elif measuredTime < 270:
            message = "Great!\n\n" + str(measuredTime)
        else:
            message = "You'll do well next time.\n\n" + str(measuredTime)
        return message




if __name__ == '__main__':
    s = SearchWord()
    s.newGame()
    s.getDisplay()