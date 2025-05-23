"""
Calculator Application
DONE BY ELYES
Copyright (c) 2024-2025 ELYES
All rights reserved.
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    fontname = "SF Pro"
    diml = 1280
    dimw = 720
    btw = 256
    bth = 125
    lew = 1260
    leh = 120
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Calculator")
        MainWindow.setFixedSize(self.diml, self.dimw)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFixedSize(self.lew, self.leh)
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 5)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)

        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setFixedSize(self.btw, self.bth)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 1, 0, 1, 1)
        self.pushButton_1.clicked.connect(lambda: self.setEditText(self.pushButton_1, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_5.clicked.connect(lambda: self.setEditText(self.pushButton_5, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_9.clicked.connect(lambda: self.setEditText(self.pushButton_9, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_13, 1, 3, 1, 1)
        self.pushButton_13.clicked.connect(lambda: self.setEditText(self.pushButton_13, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_17, 1, 4, 1, 1)
        self.pushButton_17.clicked.connect(lambda: self.setEditText(self.pushButton_17, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_2.clicked.connect(lambda: self.setEditText(self.pushButton_2, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.pushButton_6.clicked.connect(lambda: self.setEditText(self.pushButton_6, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.pushButton_10.clicked.connect(lambda: self.setEditText(self.pushButton_10, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_14, 2, 3, 1, 1)
        self.pushButton_14.clicked.connect(lambda: self.setEditText(self.pushButton_14, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_18, 2, 4, 1, 1)
        self.pushButton_18.clicked.connect(lambda: self.setEditText(self.pushButton_18, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_3.clicked.connect(lambda: self.setEditText(self.pushButton_3, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_7, 3, 1, 1, 1)
        self.pushButton_7.clicked.connect(lambda: self.setEditText(self.pushButton_7, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_11, 3, 2, 1, 1)
        self.pushButton_11.clicked.connect(lambda: self.setEditText(self.pushButton_11, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_15, 3, 3, 1, 1)
        self.pushButton_15.clicked.connect(lambda: self.setEditText(self.pushButton_15, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_19, 3, 4, 1, 1)
        self.pushButton_19.clicked.connect(lambda: self.clear(self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.pushButton_4.clicked.connect(lambda: self.setEditText(self.pushButton_4, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_8, 4, 1, 1, 1)
        self.pushButton_8.clicked.connect(lambda: self.setEditText(self.pushButton_8, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_12, 4, 2, 1, 1)
        self.pushButton_12.clicked.connect(lambda: self.setEditText(self.pushButton_12, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_16, 4, 3, 1, 1)
        self.pushButton_16.clicked.connect(lambda: self.setEditText(self.pushButton_16, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont(self.fontname)
        font.setPointSize(12)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.setFixedSize(self.btw, self.bth)
        self.gridLayout.addWidget(self.pushButton_20, 4, 4, 1, 1)
        self.pushButton_20.clicked.connect(lambda: self.button_clicked(self.lineEdit))
        self.lineEdit.setFocus()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 683, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pushButton_1.setText(_translate("MainWindow", "7"))
        self.pushButton_5.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_13.setText(_translate("MainWindow", "/"))
        self.pushButton_17.setText(_translate("MainWindow", "("))
        self.pushButton_2.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_10.setText(_translate("MainWindow", "6"))
        self.pushButton_14.setText(_translate("MainWindow", "*"))
        self.pushButton_18.setText(_translate("MainWindow", ")"))
        self.pushButton_3.setText(_translate("MainWindow", "1"))
        self.pushButton_7.setText(_translate("MainWindow", "2"))
        self.pushButton_11.setText(_translate("MainWindow", "3"))
        self.pushButton_15.setText(_translate("MainWindow", "-"))
        self.pushButton_19.setText(_translate("MainWindow", "ClrScr"))
        self.pushButton_4.setText(_translate("MainWindow", "0"))
        self.pushButton_8.setText(_translate("MainWindow", "00"))
        self.pushButton_12.setText(_translate("MainWindow", "."))
        self.pushButton_16.setText(_translate("MainWindow", "+"))
        self.pushButton_20.setText(_translate("MainWindow", "=")) 
    def setEditText(self, pushButton, lineEdit):
        num = pushButton.text()
        lineEdit.setText(str(self.lineEdit.text()+num))
    def evaluateExp(self, expression):
        try:
            result = eval(expression)
        except (ValueError, SyntaxError, ArithmeticError):
            result = "Error manual" + str(type(Exception))
        return result
    def clear(self, lineEdit):
        self.lineEdit.setText('')
    def button_clicked(self, ledit):
        exp = ledit.text()
        res = str(self.evaluateExp(exp))
        ledit.setText(res)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Calculator - DONE BY ELYES © 2024-2025")
    MainWindow.show()
    sys.exit(app.exec_())
