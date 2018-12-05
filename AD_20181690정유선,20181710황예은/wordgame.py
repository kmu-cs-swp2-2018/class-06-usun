from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class WordGame:

    def initUi(self, MainWindow):
        MainWindow.resize(672, 559)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowTitle("Word Game")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 611, 281))

        self.vLayout_wordsTE = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vLayout_wordsTE.setContentsMargins(0, 0, 0, 0)
        self.wordsEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.vLayout_wordsTE.addWidget(self.wordsEdit)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 310, 611, 61))

        self.vLayout_resultTE = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vLayout_resultTE.setContentsMargins(0, 0, 0, 0)
        self.resultEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.vLayout_resultTE.addWidget(self.resultEdit)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(170, 400, 391, 61))

        self.vLayout_inputTE = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.vLayout_inputTE.setContentsMargins(0, 0, 0, 0)
        self.inputEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.vLayout_inputTE.addWidget(self.inputEdit)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 480, 111, 33))

        self.hLayout_BtOK = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hLayout_BtOK.setContentsMargins(0, 0, 0, 0)
        self.OKButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.hLayout_BtOK.addWidget(self.OKButton)
        self.OKButton.setText("OK")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(360, 480, 111, 33))

        self.hLayout_BtCancle = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.hLayout_BtCancle.setContentsMargins(0, 0, 0, 0)
        self.cancleButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.hLayout_BtCancle.addWidget(self.cancleButton)
        self.cancleButton.setText("Cancle")

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(110, 400, 61, 61))

        self.vLayout_inputlabel = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.vLayout_inputlabel.setContentsMargins(0, 0, 0, 0)
        self.inputlabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.vLayout_inputlabel.addWidget(self.inputlabel)
        self.inputlabel.setText("Input :  ")

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = WordGame()
    ui.initUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

