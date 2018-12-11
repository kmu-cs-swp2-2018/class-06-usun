from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from word import Word
from search import SearchWord
import sys



class WordGame():


    def __init__(self, MainWindow):
        #추가
        self.word = Word('words.txt')

        MainWindow.resize(672, 559)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowTitle("Word Game")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 611, 281))

        self.vLayout_wordsTE = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vLayout_wordsTE.setContentsMargins(0, 0, 0, 0)
        self.wordsEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        # 추가
        self.vLayout_wordsTE.addWidget(self.wordsEdit)
        font = self.wordsEdit.font()
        self.wordsEdit.setFontPointSize(font.pointSize() + 2.2)
        self.wordsEdit.setAlignment(Qt.AlignVCenter)
        self.wordsEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 310, 611, 61))

        self.vLayout_resultTE = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vLayout_resultTE.setContentsMargins(0, 0, 0, 0)
        self.resultEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.resultEdit.setFontPointSize(font.pointSize() + 2.2)
        self.vLayout_resultTE.addWidget(self.resultEdit)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(170, 400, 391, 61))

        self.vLayout_inputTE = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.vLayout_inputTE.setContentsMargins(0, 0, 0, 0)
        self.inputEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        #추가
        self.inputEdit.setFont(font)
        self.inputEdit.setAlignment(Qt.AlignCenter)
        self.vLayout_inputTE.addWidget(self.inputEdit)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 480, 111, 33))

        self.hLayout_BtOK = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hLayout_BtOK.setContentsMargins(0, 0, 0, 0)
        self.OKButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.hLayout_BtOK.addWidget(self.OKButton)
        self.OKButton.setText("OK")
        self.OKButton.clicked.connect(self.searchClicked)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(360, 480, 111, 33))

        self.hLayout_BtCancle = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.hLayout_BtCancle.setContentsMargins(0, 0, 0, 0)
        self.cancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.hLayout_BtCancle.addWidget(self.cancelButton)
        self.cancelButton.setText("NewGame")
        self.cancelButton.clicked.connect(self.startGame)

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(110, 400, 61, 61))

        self.vLayout_inputlabel = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.vLayout_inputlabel.setContentsMargins(0, 0, 0, 0)
        self.inputlabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.vLayout_inputlabel.addWidget(self.inputlabel)
        self.inputlabel.setText("Input :  ")

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startGame()

    def startGame(self):
        self.search = SearchWord()
        self.search.newGame()

        self.wordsEdit.setText(self.search.getDisplay())
        self.inputEdit.clear()
        self.resultEdit.clear()

    def searchClicked(self):
        word = self.inputEdit.text()
        if word in self.search.searchedList:
            self.resultEdit.setText("You already searched the word")
        else:
            if self.search.searching(word.lower()):

                st = ""
                for i in range(len(self.search.searchedList)):
                    st = st + self.search.searchedList[i] + "\t"
                self.resultEdit.setText(st)
                self.wordsEdit.setText(self.search.getDisplay())
            else:
                self.resultEdit.setText("Try again")
                if word == "help!":
                    self.resultEdit.setText(self.search.randWords[0])

        print(set(self.search.searchedList))
        print(set(self.search.randWords))


        if len(word) == 0:
            warning_box = QMessageBox()
            warning_box.setIcon(QMessageBox.Warning)
            warning_box.setWindowTitle("Value Error")
            warning_box.setText("입력 오류")
            warning_box.setInformativeText("input에 단어를 입력해주세요")
            warning_box.exec()

        if len(self.search.randWords) == 0:
            success_box = QMessageBox()
            success_box.setWindowTitle("Success!")
            success_box.setText("Congraturation!")
            success_box.setInformativeText(self.search.getTimeMessage())
            success_box.exec()

        self.inputEdit.clear()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter:
            print("enter")
            self.searchClicked()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ADgame = WordGame(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

