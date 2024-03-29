import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)

import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit,QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        self.centralwidget = QtWidgets.QWidget()

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.pushBtAdd = QtWidgets.QPushButton()
        self.pushBtAdd.clicked.connect(self.addClicked)
        self.pushBtAdd.setText("Add")
        self.horizontalLayout.addWidget(self.pushBtAdd)

        self.pushBtDel = QtWidgets.QPushButton()
        self.pushBtDel.clicked.connect(self.deleteClicked)
        self.pushBtDel.setText("Del")
        self.horizontalLayout.addWidget(self.pushBtDel)

        self.pushBtFind = QtWidgets.QPushButton()
        self.pushBtFind.clicked.connect(self.findClicked)
        self.horizontalLayout.addWidget(self.pushBtFind)
        self.pushBtFind.setText("Find")

        self.pushBtInc = QtWidgets.QPushButton()
        self.pushBtInc.clicked.connect(self.incClicked)
        self.horizontalLayout.addWidget(self.pushBtInc)
        self.pushBtInc.setText("Inc")

        self.pushBtShow = QtWidgets.QPushButton()
        self.pushBtShow.clicked.connect(self.show)
        self.horizontalLayout.addWidget(self.pushBtShow)
        self.pushBtShow.setText("Show")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()

        self.labelName = QtWidgets.QLabel()
        self.horizontalLayout_2.addWidget(self.labelName)
        self.labelName.setText("Name:")
        self.nameEdit = QtWidgets.QLineEdit()
        self.horizontalLayout_2.addWidget(self.nameEdit)

        self.labelAge = QtWidgets.QLabel()
        self.horizontalLayout_2.addWidget(self.labelAge)
        self.labelAge.setText("Age:")
        self.ageEdit = QtWidgets.QLineEdit()
        self.horizontalLayout_2.addWidget(self.ageEdit)

        self.labelScore = QtWidgets.QLabel()
        self.horizontalLayout_2.addWidget(self.labelScore)
        self.labelScore.setText("Score:")
        self.scoreEdit = QtWidgets.QLineEdit()
        self.horizontalLayout_2.addWidget(self.scoreEdit)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()

        self.labelAmount = QtWidgets.QLabel()
        self.horizontalLayout_3.addWidget(self.labelAmount)
        self.labelAmount.setText("Amount:")
        self.amountEdit = QtWidgets.QLineEdit()
        self.horizontalLayout_3.addWidget(self.amountEdit)

        self.labeKey = QtWidgets.QLabel()
        self.horizontalLayout_3.addWidget(self.labeKey)
        self.labeKey.setText("Key:")

        self.comboBoxKey = QtWidgets.QComboBox()
        self.comboBoxKey.setToolTip("")
        self.comboBoxKey.setEditable(False)
        self.horizontalLayout_3.addWidget(self.comboBoxKey)
        self.comboBoxKey.addItems(["Name","Age","Score"])
        self.comboBoxKey.setCurrentText("Name")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.labelResult = QtWidgets.QLabel()
        self.verticalLayout_4.addWidget(self.labelResult)
        self.labelResult.setText("Result:")

        self.textEdit = QtWidgets.QTextEdit()
        self.verticalLayout_4.addWidget(self.textEdit)

        self.verticalLayout_Vbox = QtWidgets.QVBoxLayout()
        self.verticalLayout_Vbox.addLayout(self.horizontalLayout_2)
        self.verticalLayout_Vbox.addLayout(self.horizontalLayout)
        self.verticalLayout_Vbox.addLayout(self.horizontalLayout_3)
        self.verticalLayout_Vbox.addLayout(self.verticalLayout_4)

        self.setLayout(self.verticalLayout_Vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def addClicked(self):
        try:
            record = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())}
            self.scoredb.append(record)
            self.showScoreDB()

        except IndexError:
            self.errorMBox("Index Error!", "잘못입력된 값이 있습니다.", "이름, 나이, 성적을 정확히 입력해주세요.")

        except ValueError:
            self.errorMBox("Value Error!","잘못입력된 값이 있습니다.","나이, 성적을 정수로 입력해주세요.")

    def deleteClicked(self):
        try:
            isRemoved = False
            for p in self.scoredb[:]:
                if p['Name'] == self.nameEdit.text():
                    self.scoredb.remove(p)
                    isRemoved = True
                    self.showScoreDB()

            if not isRemoved:  # 에러처리 : 잘못된 이름을 입력했을 때
                self.errorMBox("Name Error!","잘못된 이름이 입력되었습니다.","이름을 정확히 입력해주세요.")

        except IndexError:
            self.errorMBox("Index Error!", "잘못입력된 값이 있습니다.","삭제할 이름을 입력해주세요.")

    def findClicked(self):
        try:
            findShow = ""
            count = 0

            for p in sorted(self.scoredb, key=lambda person: person['Name']):
                    if self.nameEdit.text() == p['Name']:
                        for attr in sorted(p):
                            count = 1
                            findShow += str(attr) + "=" + str(p[attr]) + '\t'
            findShow += '\n'

            if count == 0 :
                self.errorMBox("Index Error!", "잘못입력된 값이 있습니다.", "검색할 이름을 정확히 입력해주세요.")

            self.textEdit.setPlainText(findShow)

        except IndexError:
            self.errorMBox("Index Error!","잘못입력된 값이 있습니다.","검색할 이름을 정확히 입력해주세요.")


    def incClicked(self):
        try:
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    p['Score'] = int(p['Score'] + int(self.amountEdit.text()))
                    break
                else:  # 에러처리 : 잘못된 이름을 입력했을 때
                    self.errorMBox("Name Error!","잘못된 이름이 입력되었습니다.","정확한 이름을 입력해 주세요.")
            self.showScoreDB()

        except ValueError:
            self.errorMBox("Value Error!","입력된 점수가 정수가 아닙니다.","점수를 정확히 입력해주세요.")

        except IndexError:
            self.errorMBox("Index Error!","잘못입력된 값이 있습니다.","이름, 점수를 정확히 입력해주세요.")

    def showScoreDB(self):
        self.textEdit.setText("")
        for p in sorted(self.scoredb, key=lambda person: person[self.comboBoxKey.currentText()]):
            for attr in sorted(p):
                self.textEdit.insertPlainText(attr + "=" + str(p[attr]) + "\t")
                if(attr == 'Score'):
                    self.textEdit.insertPlainText('\n')


    def errorMBox(self,title,text,informationtext):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setWindowTitle(title)
        message_box.setText(text)
        message_box.setInformativeText(informationtext)
        message_box.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())