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
        self.pushBtAdd.clicked.connect(self.deleteClicked)
        self.pushBtDel.setText("Del")
        self.horizontalLayout.addWidget(self.pushBtDel)

        self.pushBtFind = QtWidgets.QPushButton()
        self.pushBtAdd.clicked.connect(self.find)
        self.horizontalLayout.addWidget(self.pushBtFind)
        self.pushBtFind.setText("Find")

        self.pushBtInc = QtWidgets.QPushButton()
        self.pushBtAdd.clicked.connect(self.incClicked)
        self.horizontalLayout.addWidget(self.pushBtInc)
        self.pushBtInc.setText("Inc")

        self.pushBtShow = QtWidgets.QPushButton()
        self.pushBtAdd.clicked.connect(self.show)
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
        self.comboBoxKey.setEditable(True)
        self.horizontalLayout_3.addWidget(self.comboBoxKey)
        self.comboBoxKey.setCurrentText("Name")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.labelResult = QtWidgets.QLabel()
        self.verticalLayout_4.addWidget(self.labelResult)
        self.labelResult.setText("Result:")

        self.textEdit = QtWidgets.QTextEdit()
        self.verticalLayout_4.addWidget(self.textEdit)

        self.verticalLayout_Vbox = QtWidgets.QVBoxLayout()
        self.verticalLayout_Vbox.addLayout(self.horizontalLayout)
        self.verticalLayout_Vbox.addLayout(self.horizontalLayout_2)
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

    def deleteClicked(self):

    def findClicked(self):

    def incClicked(self):

    def showScoreDB(self):
        self.textEdit.setText("")
        #print(self.scoredb)
        for p in sorted(self.scoredb, key=lambda person: person[self.comboBoxKey.currentText()]):
            for attr in sorted(p):
                self.textEdit.insertPlainText(attr + "=" + str(p[attr]) + "\t")
                if(attr == 'Score'):
                    self.textEdit.insertPlainText('\n')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())