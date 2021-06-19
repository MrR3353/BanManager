from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_captcha(object):

    def setupUi(self, captcha):
        captcha.setObjectName('captcha')
        captcha.resize(274, 154)
        self.centralWidget = QtWidgets.QWidget(captcha)
        self.centralWidget.setObjectName('centralWidget')
        self.continue_2 = QtWidgets.QPushButton(self.centralWidget)
        self.continue_2.setGeometry(QtCore.QRect(70, 110, 121, 31))
        self.continue_2.setObjectName('continue_2')
        self.link = QtWidgets.QLabel(self.centralWidget)
        self.link.setGeometry(QtCore.QRect(9, 9, 251, 31))
        self.link.setText('')
        self.link.setAlignment(QtCore.Qt.AlignCenter)
        self.link.setOpenExternalLinks(True)
        self.link.setObjectName('link')
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 251, 51))
        self.layoutWidget.setObjectName('layoutWidget')
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName('label')
        self.horizontalLayout.addWidget(self.label)
        self.captcha_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.captcha_2.setObjectName('captcha_2')
        self.horizontalLayout.addWidget(self.captcha_2)
        captcha.setCentralWidget(self.centralWidget)
        self.retranslateUi(captcha)
        QtCore.QMetaObject.connectSlotsByName(captcha)

    def retranslateUi(self, captcha):
        _translate = QtCore.QCoreApplication.translate
        captcha.setWindowTitle(_translate('captcha', 'captcha'))
        self.continue_2.setText(_translate('captcha', 'Продолжить'))
        self.label.setText(_translate('captcha', 'Captcha:'))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    captcha = QtWidgets.QMainWindow()
    ui = Ui_captcha()
    ui.setupUi(captcha)
    captcha.show()
    sys.exit(app.exec_())
