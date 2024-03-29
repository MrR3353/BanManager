from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_complain(object):

    def setupUi(self, complain):
        complain.setObjectName('complain')
        complain.resize(324, 260)
        self.centralWidget = QtWidgets.QWidget(complain)
        self.centralWidget.setObjectName('centralWidget')
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 181))
        self.groupBox.setObjectName('groupBox')
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 30, 281, 141))
        self.widget.setObjectName('widget')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName('verticalLayout')
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName('label')
        self.horizontalLayout.addWidget(self.label)
        self.reason = QtWidgets.QComboBox(self.widget)
        self.reason.setObjectName('reason')
        self.reason.addItem('')
        self.reason.addItem('')
        self.reason.addItem('')
        self.reason.addItem('')
        self.horizontalLayout.addWidget(self.reason)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName('label_2')
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comment = QtWidgets.QPlainTextEdit(self.widget)
        self.comment.setObjectName('comment')
        self.horizontalLayout_2.addWidget(self.comment)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 200, 221, 51))
        self.layoutWidget.setObjectName('layoutWidget')
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.cancel.setObjectName('cancel')
        self.horizontalLayout_3.addWidget(self.cancel)
        self.continue_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.continue_2.setDefault(True)
        self.continue_2.setObjectName('continue_2')
        self.horizontalLayout_3.addWidget(self.continue_2)
        complain.setCentralWidget(self.centralWidget)
        self.retranslateUi(complain)
        QtCore.QMetaObject.connectSlotsByName(complain)

    def retranslateUi(self, complain):
        _translate = QtCore.QCoreApplication.translate
        complain.setWindowTitle(_translate('complain', 'complain'))
        self.groupBox.setTitle(_translate('complain', 'Настройки жалобы'))
        self.label.setText(_translate('complain', 'Причина'))
        self.reason.setItemText(0, _translate('complain', 'Порнография'))
        self.reason.setItemText(1, _translate('complain', 'Рассылка спама'))
        self.reason.setItemText(2, _translate('complain', 'Оскорбительное поведение'))
        self.reason.setItemText(3, _translate('complain', 'Рекламная страница'))
        self.label_2.setText(_translate('complain', 'Комментарий'))
        self.comment.setToolTip(_translate('complain', 'Для более быстрой работы, оставьте это поле пустым'))
        self.cancel.setText(_translate('complain', 'Отмена'))
        self.continue_2.setText(_translate('complain', 'Продолжить'))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    complain = QtWidgets.QMainWindow()
    ui = Ui_complain()
    ui.setupUi(complain)
    complain.show()
    sys.exit(app.exec_())
