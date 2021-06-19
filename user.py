from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_user(object):

    def setupUi(self, user):
        user.setObjectName('user')
        user.resize(263, 347)
        self.centralWidget = QtWidgets.QWidget(user)
        self.centralWidget.setObjectName('centralWidget')
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 271))
        self.groupBox.setObjectName('groupBox')
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 33, 221, 231))
        self.widget.setObjectName('widget')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName('verticalLayout')
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName('label')
        self.horizontalLayout.addWidget(self.label)
        self.id = QtWidgets.QLineEdit(self.widget)
        self.id.setObjectName('id')
        self.horizontalLayout.addWidget(self.id)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName('horizontalLayout_5')
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName('label_4')
        self.horizontalLayout_5.addWidget(self.label_4)
        self.token = QtWidgets.QLineEdit(self.widget)
        self.token.setObjectName('token')
        self.horizontalLayout_5.addWidget(self.token)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName('label_2')
        self.horizontalLayout_2.addWidget(self.label_2)
        self.friends = QtWidgets.QCheckBox(self.widget)
        self.friends.setText('')
        self.friends.setObjectName('friends')
        self.horizontalLayout_2.addWidget(self.friends)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName('label_3')
        self.horizontalLayout_3.addWidget(self.label_3)
        self.followers = QtWidgets.QCheckBox(self.widget)
        self.followers.setText('')
        self.followers.setObjectName('followers')
        self.horizontalLayout_3.addWidget(self.followers)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName('horizontalLayout_11')
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName('label_10')
        self.horizontalLayout_11.addWidget(self.label_10)
        self.friends2Dim = QtWidgets.QCheckBox(self.widget)
        self.friends2Dim.setEnabled(True)
        self.friends2Dim.setText('')
        self.friends2Dim.setObjectName('friends2Dim')
        self.horizontalLayout_11.addWidget(self.friends2Dim)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName('horizontalLayout_10')
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName('label_9')
        self.horizontalLayout_10.addWidget(self.label_9)
        self.blocked = QtWidgets.QCheckBox(self.widget)
        self.blocked.setEnabled(False)
        self.blocked.setText('')
        self.blocked.setObjectName('blocked')
        self.horizontalLayout_10.addWidget(self.blocked)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 290, 221, 51))
        self.layoutWidget.setObjectName('layoutWidget')
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName('horizontalLayout_4')
        self.cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.cancel.setObjectName('cancel')
        self.horizontalLayout_4.addWidget(self.cancel)
        self.continue_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.continue_2.setEnabled(True)
        self.continue_2.setCheckable(False)
        self.continue_2.setChecked(False)
        self.continue_2.setAutoRepeat(False)
        self.continue_2.setAutoDefault(False)
        self.continue_2.setDefault(True)
        self.continue_2.setObjectName('continue_2')
        self.horizontalLayout_4.addWidget(self.continue_2)
        user.setCentralWidget(self.centralWidget)
        self.retranslateUi(user)
        QtCore.QMetaObject.connectSlotsByName(user)

    def retranslateUi(self, user):
        _translate = QtCore.QCoreApplication.translate
        user.setWindowTitle(_translate('user', 'user'))
        self.groupBox.setTitle(_translate('user', 'Настройки пользователя'))
        self.label.setText(_translate('user', 'ID'))
        self.label_4.setText(_translate('user', 'Токен'))
        self.token.setToolTip(_translate('user', 'Необходим для получения заблокированных на страннице пользователей.'))
        self.label_2.setText(_translate('user', 'Друзья'))
        self.label_3.setText(_translate('user', 'Подписчики'))
        self.label_10.setText(_translate('user', 'Друзья друзей'))
        self.label_9.setText(_translate('user', 'Заблокированные'))
        self.cancel.setText(_translate('user', 'Отмена'))
        self.continue_2.setText(_translate('user', 'Продолжить'))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user = QtWidgets.QMainWindow()
    ui = Ui_user()
    ui.setupUi(user)
    user.show()
    sys.exit(app.exec_())
