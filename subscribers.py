from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_subscribers(object):

    def setupUi(self, subscribers):
        subscribers.setObjectName('subscribers')
        subscribers.resize(298, 235)
        self.centralWidget = QtWidgets.QWidget(subscribers)
        self.centralWidget.setObjectName('centralWidget')
        self.text = QtWidgets.QTextBrowser(self.centralWidget)
        self.text.setGeometry(QtCore.QRect(20, 20, 256, 192))
        self.text.setObjectName('text')
        subscribers.setCentralWidget(self.centralWidget)
        self.retranslateUi(subscribers)
        QtCore.QMetaObject.connectSlotsByName(subscribers)

    def retranslateUi(self, subscribers):
        _translate = QtCore.QCoreApplication.translate
        subscribers.setWindowTitle(_translate('subscribers', 'subscribers'))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    subscribers = QtWidgets.QMainWindow()
    ui = Ui_subscribers()
    ui.setupUi(subscribers)
    subscribers.show()
    sys.exit(app.exec_())
