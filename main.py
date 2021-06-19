import os, sys, time, threading, vkbanapi, check, sender, json
from mainwindow import *
from group import *
from user import *
from another import *
from poll import *
from analysis import *
from complain import *
from help import *
from templates import *
from details import *
from captcha import *
from subscribers import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Group(QtWidgets.QMainWindow):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_group()
        self.ui.setupUi(self)
        self.setWindowTitle('Группа')
        self.show()
        self.parent = parent
        self.ui.continue_2.clicked.connect(self.ok)
        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.token.textEdited.connect(self.active_blocked)
        if 'Группа' in parent.object:
            self.ui.id.setText(str(parent.object['Группа']['id']))
            if parent.object['Группа']['token']:
                self.ui.token.setText(parent.object['Группа']['token'])
                self.ui.blocked.setEnabled(True)
                self.ui.blocked.setChecked(parent.object['Группа']['blocked'])
            self.ui.subscribers.setChecked(parent.object['Группа']['subscribers'])

    def active_blocked(self):
        if self.ui.token.text():
            self.ui.blocked.setEnabled(True)
        else:
            self.ui.subscribers.setChecked(True)
            self.ui.blocked.setEnabled(False)

    def remember(self, msg=False):
        obj = {}
        obj['token'] = self.ui.token.text().strip()
        obj['subscribers'] = self.ui.subscribers.isChecked()
        obj['blocked'] = self.ui.blocked.isChecked()
        try:
            obj['id'] = int(self.ui.id.text())
            self.parent.object['Группа'] = obj
            return True
        except ValueError:
            if msg:
                if self.ui.id.text() == '':
                    self.parent.show_error('Заполните поле ID!')
                    return False
                self.parent.show_error('В поле ID могут использоваться только цифры!')
                return False

    def ok(self):
        if not self.remember(True):
            return
        self.close()
        self.parent.ui.load.setEnabled(True)
        self.parent.setEnabled(True)
        self.parent.ui.infoBar.setText('Загрузите список выбранных пользователей')

    def closeEvent(self, QCloseEvent):
        self.remember()
        self.parent.setEnabled(True)

    def cancel(self):
        self.remember()
        self.close()
        self.parent.setEnabled(True)


class User(QtWidgets.QMainWindow):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_user()
        self.ui.setupUi(self)
        self.setWindowTitle('Пользователь')
        self.show()
        self.parent = parent
        self.ui.continue_2.clicked.connect(self.ok)
        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.token.textEdited.connect(self.switch_blocked)
        if 'Пользователь' in parent.object:
            self.ui.id.setText(str(parent.object['Пользователь']['id']))
            self.ui.friends.setChecked(parent.object['Пользователь']['friends'])
            self.ui.followers.setChecked(parent.object['Пользователь']['followers'])
            self.ui.friends2Dim.setChecked(parent.object['Пользователь']['friends2Dim'])
            self.ui.blocked.setChecked(parent.object['Пользователь']['blocked'])
            self.ui.token.setText(parent.object['Пользователь']['token'])
        self.switch_blocked()

    def switch_blocked(self):
        if self.ui.token.text():
            self.ui.blocked.setEnabled(True)
        else:
            self.ui.blocked.setChecked(False)
            self.ui.blocked.setDisabled(True)

    def remember(self, msg=False):
        obj = {}
        obj['friends'] = self.ui.friends.isChecked()
        obj['followers'] = self.ui.followers.isChecked()
        obj['friends2Dim'] = self.ui.friends2Dim.isChecked()
        obj['blocked'] = self.ui.blocked.isChecked()
        obj['token'] = self.ui.token.text()
        try:
            obj['id'] = int(self.ui.id.text())
            self.parent.object['Пользователь'] = obj
            return True
        except ValueError:
            if msg:
                if self.ui.id.text() == '':
                    self.parent.show_error('Заполните поле ID!')
                    return False
                self.parent.show_error('В поле ID могут использоваться только цифры!')
                return False

    def ok(self):
        if not self.remember(True):
            return
        self.close()
        self.parent.ui.load.setEnabled(True)
        self.parent.setEnabled(True)
        self.parent.ui.infoBar.setText('Загрузите список выбранных пользователей')

    def closeEvent(self, QCloseEvent):
        self.remember()
        self.parent.setEnabled(True)

    def cancel(self):
        self.remember()
        self.close()
        self.parent.setEnabled(True)


class Poll(QtWidgets.QMainWindow):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_poll()
        self.ui.setupUi(self)
        self.setWindowTitle('Голосование')
        self.show()
        self.parent = parent
        self.ui.continue_2.clicked.connect(self.ok)
        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.textBrowser.setEnabled(True)
        if 'Голосование' in parent.object:
            self.ui.ownerID.setText(str(parent.object['Голосование']['ownerID']))
            self.ui.ID.setText(str(parent.object['Голосование']['ID']))
            self.ui.answerID.setText(str(parent.object['Голосование']['answerID']))
            self.ui.wall.setChecked(parent.object['Голосование']['wall'])
            self.ui.discussion.setChecked(parent.object['Голосование']['discussion'])

    def remember(self, msg=False):
        obj = {}
        obj['wall'] = self.ui.wall.isChecked()
        obj['discussion'] = self.ui.discussion.isChecked()
        try:
            obj['ownerID'] = int(self.ui.ownerID.text())
            obj['ID'] = int(self.ui.ID.text())
            obj['answerID'] = int(self.ui.answerID.text())
            self.parent.object['Голосование'] = obj
            return True
        except ValueError:
            if msg:
                if not (self.ui.ownerID.text() and self.ui.ID.text() and self.ui.answerID.text()):
                    self.parent.show_error('Заполните поле ID!')
                    return False
                self.parent.show_error('В поле ID могут использоваться только цифры!')
                return False

    def ok(self):
        if not self.remember(True):
            return
        self.close()
        self.parent.ui.load.setEnabled(True)
        self.parent.setEnabled(True)
        self.parent.ui.infoBar.setText('Загрузите список выбранных пользователей')

    def closeEvent(self, QCloseEvent):
        self.remember()
        self.parent.setEnabled(True)

    def cancel(self):
        self.remember()
        self.close()
        self.parent.setEnabled(True)


class Another(QtWidgets.QMainWindow):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_another()
        self.ui.setupUi(self)
        self.setWindowTitle('Другое')
        self.show()
        self.parent = parent
        self.ui.continue_2.clicked.connect(self.ok)
        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.liked.clicked.connect(lambda: self.one_checked(self.ui.liked))
        self.ui.reposted.clicked.connect(lambda: self.one_checked(self.ui.reposted))
        self.ui.commented.clicked.connect(lambda: self.one_checked(self.ui.commented))
        self.ui.likedComments.clicked.connect(lambda: self.one_checked(self.ui.likedComments))
        self.ui.objectType.currentTextChanged.connect(self.discuss_block)
        self.ui.textBrowser.setEnabled(True)
        if 'Другое' in parent.object:
            self.ui.objectType.setCurrentText(parent.object['Другое']['objectType'])
            self.ui.ownerID.setText(str(parent.object['Другое']['ownerID']))
            self.ui.objectID.setText(str(parent.object['Другое']['objectID']))
            self.ui.liked.setChecked(parent.object['Другое']['liked'])
            self.ui.reposted.setChecked(parent.object['Другое']['reposted'])
            self.ui.commented.setChecked(parent.object['Другое']['commented'])
            self.ui.likedComments.setChecked(self.parent.object['Другое']['liked_comments'])

    def one_checked(self, x):
        if not self.ui.liked.isChecked() and not self.ui.reposted.isChecked() and not self.ui.commented.isChecked() and not self.ui.likedComments.isChecked():
            x.setChecked(True)

    def discuss_block(self):
        if self.ui.objectType.currentText() == 'Обсуждение':
            self.ui.liked.setDisabled(True)
            self.ui.reposted.setDisabled(True)
            self.ui.liked.setChecked(False)
            self.ui.reposted.setChecked(False)
            self.one_checked(self.ui.commented)
        else:
            self.ui.liked.setEnabled(True)
            self.ui.reposted.setEnabled(True)
            self.one_checked(self.ui.liked)

    def remember(self, msg=False):
        obj = {}
        obj['objectType'] = self.ui.objectType.currentText()
        obj['liked'] = self.ui.liked.isChecked()
        obj['reposted'] = self.ui.reposted.isChecked()
        obj['commented'] = self.ui.commented.isChecked()
        obj['liked_comments'] = self.ui.likedComments.isChecked()
        obj['objectID'] = self.ui.objectID.text()
        try:
            obj['ownerID'] = int(self.ui.ownerID.text())
            self.parent.object['Другое'] = obj
            return True
        except ValueError:
            if msg:
                if not self.ui.ownerID.text():
                    self.parent.show_error('Заполните поле ID!')
                    return False
                self.parent.show_error('В поле ID могут использоваться только цифры!')
                return False

    def ok(self):
        if not self.remember(True):
            return
        self.close()
        self.parent.ui.load.setEnabled(True)
        self.parent.setEnabled(True)
        self.parent.ui.infoBar.setText('Загрузите список выбранных пользователей')

    def closeEvent(self, QCloseEvent):
        self.remember()
        self.parent.setEnabled(True)

    def cancel(self):
        self.remember()
        self.close()
        self.parent.setEnabled(True)


class Analysis(QtWidgets.QMainWindow):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_analysis()
        self.ui.setupUi(self)
        self.setWindowTitle('Сравнение')
        self.show()
        self.parent = parent
        self.ui.continue_2.clicked.connect(self.ok)
        self.ui.all.clicked.connect(self.all)
        self.ui.noblocked.clicked.connect(self.noblocked)
        self.ui.blocked.clicked.connect(self.blocked)
        self.all()

    def ok(self):
        self.close()
        self.parent.setEnabled(True)

    def closeEvent(self, QCloseEvent):
        self.parent.setEnabled(True)

    def all(self):
        self.ui.listWidget.clear()
        x = list(map(str, self.parent.users))
        self.ui.listWidget.addItems(x)
        self.ui.count.setText(str(self.ui.listWidget.count()))

    def noblocked(self):
        self.ui.listWidget.clear()
        for id in self.parent.users:
            if id not in self.parent.banned:
                self.ui.listWidget.addItem(str(id))

        self.ui.count.setText(str(self.ui.listWidget.count()))

    def blocked(self):
        self.ui.listWidget.clear()
        for id in self.parent.users:
            if id in self.parent.banned:
                self.ui.listWidget.addItem(str(id))

        self.ui.count.setText(str(self.ui.listWidget.count()))


class Help(QtWidgets.QMainWindow):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_help()
        self.ui.setupUi(self)
        self.setWindowTitle('Помощь')
        self.show()
        self.parent = parent

    def closeEvent(self, QCloseEvent):
        self.parent.setEnabled(True)


class Complain(QtWidgets.QMainWindow):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_complain()
        self.ui.setupUi(self)
        self.setWindowTitle('Настройки жалобы')
        self.show()
        self.parent = parent
        self.ui.continue_2.clicked.connect(self.ok)
        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.reason.setCurrentText(parent.complain_reason)
        self.ui.comment.setPlainText(parent.complain_comment)

    def ok(self):
        self.parent.complain_reason = self.ui.reason.currentText()
        self.parent.complain_comment = self.ui.comment.toPlainText()
        self.close()
        self.parent.ui.load.setEnabled(True)
        self.parent.setEnabled(True)

    def closeEvent(self, QCloseEvent):
        self.parent.setEnabled(True)

    def cancel(self):
        self.parent.complain_reason = self.ui.reason.currentText()
        self.parent.complain_comment = self.ui.comment.toPlainText()
        self.close()
        self.parent.setEnabled(True)


class Templates(QtWidgets.QMainWindow):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_templates()
        self.ui.setupUi(self)
        self.setWindowTitle('Сборки')
        self.show()
        self.parent = parent
        self.ui.delete_2.setDisabled(True)
        self.ui.details.setDisabled(True)
        self.ui.modify.setDisabled(True)
        self.ui.apply.setDisabled(True)
        self.ui.templatesList.clicked.connect(self.buttons_enable)
        self.ui.create.clicked.connect(self.add_template)
        self.ui.delete_2.clicked.connect(self.delete_template)
        self.ui.modify.clicked.connect(self.modify_template)
        self.ui.apply.clicked.connect(self.apply)
        self.ui.details.clicked.connect(self.details)
        self.show_templates()

    def closeEvent(self, QCloseEvent):
        self.parent.setEnabled(True)

    def details(self):
        self.second_window = Details(self)

    def buttons_enable(self):
        self.ui.delete_2.setEnabled(True)
        self.ui.details.setEnabled(True)
        self.ui.modify.setEnabled(True)
        self.ui.apply.setEnabled(True)
        self.ui.apply.setDefault(True)

    def get_templates(self):
        x = []
        for i in range(self.ui.templatesList.count()):
            x.append(self.ui.templatesList.item(i).text())

        return x

    def show_templates(self):
        try:
            full_path = str(os.path.abspath(__file__)).split('\\')[:-1]
            path = ''
            for i in full_path:
                path += i + '/'

            mem = open(path + 'templates.txt', 'r')
            templ = json.loads(mem.read())
            for name in templ:
                self.ui.templatesList.addItem(name)

        except:
            pass

    def add_template(self):
        if self.ui.name.text() and self.ui.name.text() not in self.get_templates():
            self.ui.templatesList.addItem(self.ui.name.text())
            try:
                full_path = str(os.path.abspath(__file__)).split('\\')[:-1]
                path = ''
                for i in full_path:
                    path += i + '/'

                mem = open(path + 'templates.txt', 'r')
                data = json.loads(mem.read())
                data[self.ui.name.text()] = []
                mem.close()
            except:
                data = {}
                data[self.ui.name.text()] = []

            full_path = str(os.path.abspath(__file__)).split('\\')[:-1]
            path = ''
            for i in full_path:
                path += i + '/'

            file = open(path + 'templates.txt', 'w')
            file.write(json.dumps(data))
            file.close()
        else:
            self.parent.show_error('Это имя уже используется! Выберите что-то другое')

    def modify_template(self):
        if self.parent.ui.objectType.currentText() == 'Группа' and (not self.parent.ui.groupID.text() or not self.parent.ui.groupToken.text()) or not self.parent.ui.userToken.text():
            self.parent.show_error('Заполните все необходимые поля!')
            return
        self.parent.save()
        full_path = str(os.path.abspath(__file__)).split('\\')[:-1]
        path = ''
        for i in full_path:
            path += i + '/'

        mem = open(path + 'config.txt', 'r')
        cur_config = json.loads(mem.read())
        mem.close()
        mem = open(path + 'templates.txt', 'r')
        templ = json.loads(mem.read())
        mem.close()
        templ[self.ui.templatesList.currentItem().text()].append(cur_config)
        file = open(path + 'templates.txt', 'w')
        file.write(json.dumps(templ))
        file.close()

    def delete_template(self):
        full_path = str(os.path.abspath(__file__)).split('\\')[:-1]
        path = ''
        for i in full_path:
            path += i + '/'

        mem = open(path + 'templates.txt', 'r')
        templ = json.loads(mem.read())
        mem.close()
        templ.pop(self.ui.templatesList.currentItem().text())
        file = open(path + 'templates.txt', 'w')
        file.write(json.dumps(templ))
        file.close()
        self.ui.templatesList.clear()
        self.show_templates()

    def apply(self):
        self.close()
        self.parent.apply_template(self.ui.templatesList.currentItem().text())


class Details(QtWidgets.QMainWindow):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_details()
        self.ui.setupUi(self)
        self.setWindowTitle('Детали')
        self.show()
        self.parent = parent
        full_path = str(os.path.abspath(__file__)).split('\\')[:-1]
        path = ''
        for i in full_path:
            path += i + '/'

        mem = open(path + 'templates.txt', 'r')
        templ = json.loads(mem.read())
        mem.close()
        data = templ[self.parent.ui.templatesList.currentItem().text()]
        self.ui.table.setRowCount(len(data))
        line = 0
        for task in data:
            self.ui.table.setItem(line, 0, QtWidgets.QTableWidgetItem(str(task['objectType'])))
            try:
                self.ui.table.setItem(line, 1, QtWidgets.QTableWidgetItem(str(task['groupID'])))
                self.ui.table.setItem(line, 2, QtWidgets.QTableWidgetItem(str(task['groupToken'])))
            except:
                self.ui.table.setItem(line, 1, QtWidgets.QTableWidgetItem('-'))
                self.ui.table.setItem(line, 2, QtWidgets.QTableWidgetItem('-'))

            self.ui.table.setItem(line, 3, QtWidgets.QTableWidgetItem(str(task['userToken'])))
            self.ui.table.setItem(line, 4, QtWidgets.QTableWidgetItem(str(task['chooseFrom'])))
            try:
                self.ui.table.setItem(line, 5, QtWidgets.QTableWidgetItem(str(task['object'][str(task['chooseFrom'])]['ownerID'])))
                self.ui.table.setItem(line, 6, QtWidgets.QTableWidgetItem(str(task['object'][str(task['chooseFrom'])]['objectID'])))
            except:
                self.ui.table.setItem(line, 5, QtWidgets.QTableWidgetItem('-'))
                self.ui.table.setItem(line, 6, QtWidgets.QTableWidgetItem(str(task['object'][str(task['chooseFrom'])]['id'])))

            self.ui.table.setItem(line, 7, QtWidgets.QTableWidgetItem(str(task['action'])))
            self.ui.table.setItem(line, 8, QtWidgets.QTableWidgetItem(str(task['period'])))
            self.ui.table.setItem(line, 9, QtWidgets.QTableWidgetItem(str(task['reason'])))
            line += 1

        self.ui.table.resizeColumnsToContents()

    def closeEvent(self, QCloseEvent):
        self.parent.setEnabled(True)


class Captcha(QtWidgets.QMainWindow):

    def __init__(self, parent, link):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_captcha()
        self.ui.setupUi(self)
        self.setWindowTitle('Капча')
        self.show()
        self.parent = parent
        self.ui.link.setText('<a href="' + link + '"><span style=" text-decoration: underline; color:#0000ff;">Посмотреть</span></a>')
        self.ui.continue_2.clicked.connect(self.ok)

    def ok(self):
        self.parent.vk.captcha = self.ui.captcha_2.text()
        self.close()
        self.parent.setEnabled(True)

    def closeEvent(self, QCloseEvent):
        self.parent.setEnabled(True)


class Subcscribers(QtWidgets.QMainWindow):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_subscribers()
        self.ui.setupUi(self)
        self.setWindowTitle('Друзья, которые будут заблокированы')
        self.show()
        self.parent = parent
        self.fill()

    def fill(self):
        self.ui.text.setText(str(self.parent.bl_friends))

    def closeEvent(self, QCloseEvent):
        self.parent.setEnabled(True)


class MyWin(QtWidgets.QMainWindow):
    my_signal = QtCore.pyqtSignal(list, name='my_signal')

    def __init__(self, access, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.second_window = None
        self.templ_running = False
        self.exit = False
        self.vk = vkbanapi.VkApi()
        self.object = {}
        self.users = []
        self.banned = []
        self.loading = False
        self.action = False
        self.bl_friends = []
        self.complain_reason = 'Порнография'
        self.complain_comment = ''
        self.ui.chooseUsers.clicked.connect(self.choose_users)
        self.ui.help.clicked.connect(self.help)
        self.ui.look.clicked.connect(self.look)
        self.ui.templates.clicked.connect(self.template)
        self.ui.load.clicked.connect(lambda : self.load(self.my_signal))
        self.ui.compare.clicked.connect(self.analyze)
        self.ui.applyAction.clicked.connect(lambda : self.apply(self.my_signal))
        self.ui.complainSettings.clicked.connect(lambda : self.complain_settings())
        self.ui.objectType.currentTextChanged.connect(lambda : self.ui.load.setDisabled(True))
        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.check.clicked.connect(self.proxy_status)
        self.ui.online.clicked.connect(lambda : self.set_online())
        self.ui.clear.clicked.connect(lambda : self.clear(self.my_signal))
        self.my_signal.connect(self.my_signal_handler, QtCore.Qt.QueuedConnection)
        self.ui.objectType.currentTextChanged.connect(self.obj_type_changed)
        self.ui.groupID.textEdited.connect(self.choose_enable)
        self.ui.groupToken.textEdited.connect(self.choose_enable)
        self.ui.userToken.textEdited.connect(self.choose_enable)
        self.ui.action.currentTextChanged.connect(lambda : self.ui.applyAction.setText(self.ui.action.currentText()))
        self.ui.cancel.hide()
        self.ui.chooseUsers.setDisabled(True)
        self.ui.infoBar.setText('Заполните все поля')
        self.autocomplete()
        self.choose_enable()
        if not access:
            self.ui.groupID.setDisabled(True)
            self.ui.groupToken.setDisabled(True)
            self.ui.userToken.setDisabled(True)
            self.ui.objectType.setDisabled(True)
            self.ui.reason.setDisabled(True)
            self.ui.comment.setDisabled(True)
            self.ui.period.setDisabled(True)
            self.ui.commentVisible.setDisabled(True)
            self.ui.ip.setDisabled(True)
            self.ui.port.setDisabled(True)
            self.ui.digitalBar.setText('Пишите сюда, чтобы купить полную версию: misstepdev@gmail.com')
            self.ui.infoBar.setText('Срок действия пробной версии истек. Приобретите полную версию.')

    def autocomplete(self):
        try:
            full_path = str(os.path.abspath(__file__)).split('\\')[:-1]
            path = ''
            for i in full_path:
                path += i + '/'

            mem = open(path + 'config.txt', 'r')
            data = json.loads(mem.read())
            mem.close()
            self.ui.ip.setText(data['ip'])
            self.ui.port.setText(data['port'])
            self.ui.objectType.setCurrentText(data['objectType'])
            self.ui.groupID.setText(data['groupID'])
            self.ui.groupToken.setText(data['groupToken'])
            self.ui.userToken.setText(data['userToken'])
            self.ui.chooseFrom.setCurrentText(data['chooseFrom'])
            self.ui.reason.setValue(int(data['reason']))
            self.ui.comment.setPlainText(data['comment'])
            self.ui.commentVisible.setChecked(data['commentVisible'])
            self.ui.period.setCurrentText(data['period'])
            self.ui.action.setCurrentText(data['action'])
            self.object = data['object']
        except:
            return

    def save(self):
        full_path = str(os.path.abspath(__file__)).split('\\')[:-1]
        path = ''
        for i in full_path:
            path += i + '/'

        file = open(path + 'config.txt', 'w')
        file.write(json.dumps({'ip': self.ui.ip.text(),
         'port': self.ui.port.text(),
         'objectType': self.ui.objectType.currentText(),
         'groupID': self.ui.groupID.text(),
         'groupToken': self.ui.groupToken.text(),
         'userToken': self.ui.userToken.text(),
         'chooseFrom': self.ui.chooseFrom.currentText(),
         'reason': self.ui.reason.value(),
         'comment': self.ui.comment.toPlainText(),
         'commentVisible': self.ui.commentVisible.isChecked(),
         'period': self.ui.period.currentText(),
         'action': self.ui.action.currentText(),
         'object': self.object}))
        file.close()

    def closeEvent(self, QCloseEvent):
        self.exit = True
        self.cancel()
        self.save()
        self.close()

    def cancel(self):
        self.vk.stop = True

    def proxy_status(self):
        if self.ui.ip and self.ui.port:
            c = 0
            for i in self.ui.ip.text():
                if i == '.':
                    c += 1

            if c != 3:
                self.ui.proxyStatus.setText('Нет соединения')
                return
            self.vk.proxy = {'https': 'https://' + self.ui.ip.text() + ':' + self.ui.port.text()}
            if self.vk.is_working():
                self.ui.proxyStatus.setText('Подключено')
                self.check_connection()
            else:
                self.ui.proxyStatus.setText('Нет соединения')
        else:
            if self.vk.is_working():
                self.ui.proxyStatus.setText('Не требуется')
            else:
                self.ui.proxyStatus.setText('Не подключено')

    def obj_type_changed(self):
        if self.ui.objectType.currentText() == 'Группа':
            self.ui.changesLabel.setText('Уменьшение числа подписчиков на:')
            self.ui.groupID.setEnabled(True)
            self.ui.groupToken.setEnabled(True)
            self.ui.blockSettings.setEnabled(True)
        else:
            if self.ui.objectType.currentText() == 'Страница':
                self.ui.groupID.setText('')
                self.ui.groupToken.setText('')
                self.ui.changesLabel.setText('Уменьшение числа друзей на:')
                self.ui.groupID.setDisabled(True)
                self.ui.groupToken.setDisabled(True)
                self.ui.blockSettings.setDisabled(True)
        self.choose_enable()

    def choose_enable(self):
        self.ui.chooseUsers.setDisabled(True)
        if self.ui.objectType.currentText() == 'Группа':
            if self.ui.groupID.text() and self.ui.groupToken.text() and self.ui.userToken.text():
                gt = self.ui.groupToken.text().strip()
                ut = self.ui.userToken.text().strip()
                if len(gt) == len(ut) == 85:
                    self.ui.infoBar.setText('Выберите группу пользователей')
                    self.ui.chooseUsers.setEnabled(True)
                else:
                    self.ui.infoBar.setText('Токен группы или токен пользователя указаны неверно')
            else:
                self.ui.infoBar.setText('Заполните все поля')
        else:
            if self.ui.objectType.currentText() == 'Страница':
                if len(self.ui.userToken.text().strip()) == 85:
                    self.ui.infoBar.setText('Выберите группу пользователей')
                    self.ui.chooseUsers.setEnabled(True)
                else:
                    self.ui.infoBar.setText('Токен пользователя указан неверно')
                self.ui.load.setDisabled(True)
                self.ui.applyAction.setDisabled(True)
                self.ui.changes.setText('0')

    def show_error(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def my_signal_handler(self, data):
        i, count = int(data[0]), int(data[1])
        self.ui.digitalBar.setText(str(data[0]) + '/' + str(data[1]))
        self.ui.progressBar.setValue(0 if count == 0 else int(i * 100 / count))
        if len(data) == 3:
            self.ui.infoBar.setText(data[2])
        if len(data) == 4:
            self.ui.infoBar.setText(data[2])
            self.second_window = Captcha(self, data[3])

    def choose_users(self):
        self.ui.applyAction.setDisabled(True)
        self.ui.compare.setDisabled(True)
        self.ui.load.setDisabled(True)
        self.setDisabled(True)
        if self.ui.chooseFrom.currentText() == 'Группа':
            self.second_window = Group(self)
        else:
            if self.ui.chooseFrom.currentText() == 'Пользователь':
                self.second_window = User(self)
            else:
                if self.ui.chooseFrom.currentText() == 'Голосование':
                    self.second_window = Poll(self)
                else:
                    if self.ui.chooseFrom.currentText() == 'Другое':
                        self.second_window = Another(self)

    def complain_settings(self):
        self.setDisabled(True)
        self.second_window = Complain(self)

    def analyze(self):
        self.setDisabled(True)
        self.second_window = Analysis(self)

    def help(self):
        self.second_window = Help(self)

    def look(self):
        self.second_window = Subcscribers(self)

    def template(self):
        self.second_window = Templates(self)

    def thread(my_func):
        """
        Запускает функцию в отдельном потоке
        """

        def wrapper(*args, **kwargs):
            my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
            my_thread.start()

        return wrapper

    @thread
    def clear(self, signal):
        if self.loading:
            return
        self.loading = True
        self.vk.signal = signal
        if self.ui.objectType.currentText() == 'Группа':
            banned = self.vk.group_get_banned(self.ui.groupID.text(), self.ui.groupToken.text())
            unban = self.vk.get_vk_banned(banned)
            self.vk.group_unban(self.ui.userToken.text(), self.ui.groupID.text(), unban)
        else:
            banned = self.vk.user_get_banned(self.ui.userToken.text())
            unban = self.vk.get_vk_banned(banned)
            self.vk.user_unban(self.ui.userToken.text(), unban)
        self.loading = False

    @thread
    def apply_template(self, template):
        self.vk.templates = True
        if self.templ_running:
            return
        self.templ_running = True
        full_path = str(os.path.abspath(__file__)).split('\\')[:-1]
        path = ''
        for i in full_path:
            path += i + '/'

        mem = open(path + 'templates.txt', 'r')
        templ = json.loads(mem.read())
        mem.close()
        tasks = templ[template]
        for task in tasks:
            task['ip'] = self.ui.ip.text()
            task['port'] = self.ui.port.text()
            full_path = str(os.path.abspath(__file__)).split('\\')[:-1]
            path = ''
            for i in full_path:
                path += i + '/'

            file = open(path + 'config.txt', 'w')
            file.write(json.dumps(task))
            file.close()
            self.autocomplete()
            self.load(self.my_signal)
            time.sleep(5)
            while 1:
                if self.loading:
                    time.sleep(0.5)

            self.apply(self.my_signal)
            time.sleep(5)
            while self.action:
                time.sleep(0.5)

        self.vk.templates = False
        self.templ_running = False

    @thread
    def set_online(self):
        while self.ui.online.isChecked():
            self.vk.set_online(self.ui.userToken.text())
            if self.exit:
                return

    @thread
    def check_connection(self):
        if not self.vk.is_working():
            self.ui.proxyStatus.setText('Ошибка')
        else:
            for i in range(300):
                if self.exit:
                    return
                time.sleep(1)

            self.check_connection()

    @thread
    def load(self, signal):
        if self.loading:
            return
        self.loading = True
        self.ui.infoBar.setText('Получение списка пользователей...')
        self.ui.cancel.show()
        # self.vk.signal = self.my_signal
        self.vk.signal = signal
        self.vk.group_token = self.ui.groupToken.text().strip()
        self.vk.user_token = self.ui.userToken.text().strip()
        self.users = []
        if self.ui.chooseFrom.currentText() == 'Группа':
            if self.object['Группа']['subscribers']:
                members = self.vk.group_get_members(self.object['Группа']['id'])
                print('members:')
                print(members)
                self.users += members
            elif self.object['Группа']['blocked']:
                blocked = self.vk.group_get_banned(self.object['Группа']['id'], self.object['Группа']['token'])
                print('blocked:')
                print(blocked)
                self.users += blocked
        elif self.ui.chooseFrom.currentText() == 'Пользователь':
            if self.object['Пользователь']['friends']:
                friends = self.vk.user_get_friends(self.object['Пользователь']['id'])
                print('friends:')
                print(friends)
                self.users += friends
            if self.object['Пользователь']['followers']:
                followers = self.vk.user_get_followers(self.object['Пользователь']['id'])
                print('followers:')
                print(followers)
                self.users += followers
            if self.object['Пользователь']['blocked']:
                blocked = self.vk.user_get_banned(self.object['Пользователь']['token'])
                print('blocked:')
                print(blocked)
                self.users += blocked
            if self.object['Пользователь']['friends2Dim']:
                friends = self.vk.user_get_friends(self.object['Пользователь']['id'])
                print('friends:')
                print(friends)
                friends2dim = []
                for id in friends:
                    fr = self.vk.user_get_friends(id)
                    # print(id, fr)
                    friends2dim += fr

                self.users += friends2dim
            self.users.append(self.object['Пользователь']['id'])
        elif self.ui.chooseFrom.currentText() == 'Голосование':
            voters = self.vk.get_voters(self.ui.userToken.text().strip(), self.object['Голосование']['ownerID'], self.object['Голосование']['ID'], self.object['Голосование']['answerID'], int(self.object['Голосование']['discussion']))
            print('voters:')
            print(voters)
            self.users += voters
        elif self.ui.chooseFrom.currentText() == 'Другое':
            ru2en = {'Пост': 'post',
                     'Фото': 'photo',
                     'Аудио': 'audio',
                     'Видео': 'video',
                     'Заметка': 'note',
                     'Товар': 'market',
                     'Комментарий к посту': 'comment',
                     'Комментарий к фото': 'photo_comment',
                     'Комментарий к видео': 'video_comment',
                     'Комментарий в обсуждении': 'topic_comment',
                     'Комментарий к товару': 'market_comment'}
            if self.object['Другое']['objectType'] == 'Обсуждение':
                self.object['Другое']['ownerID'] = abs(self.object['Другое']['ownerID'])
                topics = [self.object['Другое']['objectID']]
                if not self.object['Другое']['objectID']:
                    topics = self.vk.get_topics(self.object['Другое']['ownerID'])
                print('topics', topics)
                comments_id = []
                commented = []
                for topic in topics:
                    tmp = self.vk.get_comments_id(self.object['Другое']['ownerID'], topic)
                    print(tmp)
                    comments_id += tmp[0]
                    commented += tmp[1]

                if self.object['Другое']['commented']:
                    print('commented', commented)
                    self.users += commented
                if self.object['Другое']['liked_comments']:
                    liked = []
                    for c in range(len(comments_id)):
                        liked += self.vk.get_liked('topic_comment', commented[c], comments_id[c])

                    print('liked_comments', liked)
                    self.users += liked
            else:
                if self.object['Другое']['liked']:
                    liked = self.vk.get_liked(ru2en[self.object['Другое']['objectType']], self.object['Другое']['ownerID'], self.object['Другое']['objectID'])
                    print(liked)
                    self.users += liked
                if self.object['Другое']['reposted']:
                    reposted = self.vk.get_reposted(ru2en[self.object['Другое']['objectType']], self.object['Другое']['ownerID'], self.object['Другое']['objectID'])
                    print(reposted)
                    self.users += reposted
                if self.object['Другое']['commented']:
                    commented = self.vk.get_commented(self.object['Другое']['ownerID'], self.object['Другое']['objectID'])[1]
                    print(commented)
                    self.users += commented
                if self.object['Другое']['liked_comments']:
                    liked_comments = self.vk.get_liked_comments(self.object['Другое']['ownerID'], self.object['Другое']['objectID'])
                    print(liked_comments)
                    self.users += liked_comments
        self.ui.infoBar.setText('Получение заблокированных пользователей...')
        self.banned = []
        if self.ui.objectType.currentText() == 'Группа':
            self.banned = self.vk.group_get_banned(self.ui.groupID.text().strip(), self.ui.groupToken.text().strip())
        else:
            if self.ui.objectType.currentText() == 'Страница':
                self.banned = self.vk.user_get_banned(self.ui.userToken.text().strip())
        print('banned:')
        print(self.banned)
        if self.ui.action.currentText() == 'Заблокировать' and self.ui.period.currentText() == 'Навсегда':
            changes = 0
            usr = []
            self.bl_friends = []
            if self.ui.objectType.currentText() == 'Группа':
                usr = self.vk.group_get_members(self.ui.groupID.text().strip())
            elif self.ui.objectType.currentText() == 'Страница':
                usr = self.vk.user_get_friends(self.vk.user_get_id(self.ui.userToken.text().strip()))
            for i in self.users:
                if i in usr and i not in self.banned:
                    changes += 1
                    self.bl_friends.append(i)
            self.ui.changes.setText(str(changes))
        self.loading = False
        self.ui.cancel.hide()
        self.ui.compare.setEnabled(True)
        self.ui.applyAction.setEnabled(True)
        self.ui.infoBar.setText('Список пользователей успешно загружен')
        if self.vk.stop:
            self.ui.infoBar.setText('Операция была отменена. Загрузите список пользователей')
        self.vk.stop = False

    @thread
    def apply(self, signal):
        while self.loading:
            time.sleep(0.5)

        def get_noblocked():
            res = []
            for id in self.users:
                if id not in self.banned:
                    res.append(id)

            return res

        def get_blocked():
            res = []
            for id in self.users:
                if id in self.banned:
                    res.append(id)

            return res

        if self.action:
            return
        self.action = True
        self.ui.cancel.show()
        self.vk.signal = signal
        self.vk.group_token = self.ui.groupToken.text().strip()
        self.vk.user_token = self.ui.userToken.text().strip()
        if self.ui.action.currentText() == 'Заблокировать':
            if self.ui.objectType.currentText() == 'Группа':
                end_date = '"end_date":'
                if self.ui.period.currentText() == 'Год':
                    end_date += str(int(time.time()) + 31536000)
                else:
                    if self.ui.period.currentText() == 'Месяц':
                        end_date += str(int(time.time()) + 2678400)
                    else:
                        if self.ui.period.currentText() == 'Неделя':
                            end_date += str(int(time.time()) + 604800)
                        else:
                            if self.ui.period.currentText() == 'День':
                                end_date += str(int(time.time()) + 86400)
                        end_date += ','
                        if self.ui.period.currentText() == 'Навсегда':
                            end_date = ''
                        self.vk.group_ban(self.ui.userToken.text().strip(), get_noblocked(), self.ui.groupID.text().strip(), end_date, self.ui.reason.value(), self.ui.comment.toPlainText().strip(), int(self.ui.commentVisible.isChecked()))
            else:
                if self.ui.objectType.currentText() == 'Страница':
                    self.vk.user_ban(self.ui.userToken.text().strip(), get_noblocked())
            self.ui.infoBar.setText('Блокирование прошло успешно')
            if self.vk.stop:
                self.ui.infoBar.setText('Операция блокировки была отменена')
        else:
            if self.ui.action.currentText() == 'Разблокировать':
                if self.ui.objectType.currentText() == 'Группа':
                    self.vk.group_unban(self.ui.userToken.text().strip(), self.ui.groupID.text().strip(), get_blocked())
                else:
                    if self.ui.objectType.currentText() == 'Страница':
                        self.vk.user_unban(self.ui.userToken.text().strip(), get_blocked())
                self.ui.infoBar.setText('Разблокировка прошло успешно')
                if self.vk.stop:
                    self.ui.infoBar.setText('Операция разблокировки была отменена')
            else:
                if self.ui.action.currentText() == 'Пожаловаться':
                    reason2type = {'Порнография': 'porn',
                                   'Рассылка спама': 'spam',
                                   'Оскорбительное поведение': 'insult',
                                   'Рекламная страница': 'advertisment'}
                    self.vk.user_report(self.ui.userToken.text().strip(), self.users, reason2type[self.complain_reason], self.complain_comment)
            self.action = False
            self.ui.cancel.hide()
            self.vk.stop = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    x = check.isAccess()
    myapp = MyWin(x)
    myapp.setWindowTitle('BanManager')
    myapp.show()
    sys.exit(app.exec_())
