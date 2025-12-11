from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 340)
        self.lineEditUsername = QtWidgets.QLineEdit(Dialog)
        self.lineEditUsername.setGeometry(QtCore.QRect(130, 60, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditUsername.setFont(font)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(130, 130, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.labelOutpot = QtWidgets.QLabel(Dialog)
        self.labelOutpot.setGeometry(QtCore.QRect(110, 200, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelOutpot.setFont(font)
        self.labelOutpot.setText("")
        self.labelOutpot.setObjectName("labelOutpot")
        self.LoginButton = QtWidgets.QPushButton(Dialog)
        self.LoginButton.setGeometry(QtCore.QRect(130, 250, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LoginButton.setFont(font)
        self.LoginButton.setObjectName("LoginButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEditUsername.setPlaceholderText(_translate("Dialog", "Username"))
        self.lineEditPassword.setPlaceholderText(_translate("Dialog", "Password"))
        self.LoginButton.setText(_translate("Dialog", "Login"))
