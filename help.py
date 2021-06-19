# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_help(object):
    def setupUi(self, help):
        help.setObjectName("help")
        help.resize(661, 357)
        self.centralWidget = QtWidgets.QWidget(help)
        self.centralWidget.setObjectName("centralWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 641, 311))
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.mail = QtWidgets.QLabel(self.centralWidget)
        self.mail.setGeometry(QtCore.QRect(20, 330, 281, 21))
        self.mail.setOpenExternalLinks(True)
        self.mail.setObjectName("mail")
        self.telegram = QtWidgets.QLabel(self.centralWidget)
        self.telegram.setGeometry(QtCore.QRect(320, 330, 131, 20))
        self.telegram.setObjectName("telegram")
        help.setCentralWidget(self.centralWidget)

        self.retranslateUi(help)
        QtCore.QMetaObject.connectSlotsByName(help)

    def retranslateUi(self, help):
        _translate = QtCore.QCoreApplication.translate
        help.setWindowTitle(_translate("help", "help"))
        self.textBrowser.setHtml(_translate("help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:10pt;\">Использование прокси</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:10pt;\">Если в вашей стране недоступен сайт Вконтакте, тогда, чтобы использовать программу вам необходимо использовать прокси. Не используйте их просто так, т. к. они замедляют процесс работы. Найдите в поисковых системах сайт со списком прокси адресов. Важно: выбранный прокси должен работать по протоколу HTTPS. Скопируйте ip адрес(например: 170.79.16.19) и порт(обычно 8080) в соответствующие поля. Если все в порядке то справа статус прокси изменится на &quot;Подключено&quot;.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:10pt;\">Как получить токен группы?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:10pt;\">Заходим на сайт своей группы &gt; Управление сообществом &gt; Настройки &gt; Работа с API &gt; Создать ключ &gt; Ставим галочку &quot;Разрешить приложению доступ к управлению сообществом&quot; &gt; Создать. Далее вам придет подтверждение о создании ключа, вы вводите код и сайт выдает Вам ключ доступа. Это и есть токен группы.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:10pt;\">Как получить токен администратора?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:10pt;\">Для этого вам нужно обязательно быть авторизованным в качестве админа/модератора в группе. Переходим по </span><a href=\"https://oauth.vk.com/authorize?client_id=6475224&amp;display=page&amp;redirect_uri=https://oauth.vk.com/blank.html&amp;scope=friends,groups,offline&amp;response_type=token&amp;v=7.54\"><span style=\" font-family:\'.SF NS Text\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">специальной ссылке.</span></a><span style=\" font-family:\'.SF NS Text\'; font-size:10pt;\"> Разрешаем приложению доступ к общей информации и группам. После этого в адресной строке браузера изменится текст, откуда нужно будет скопировать токен. Это последовательность символов, начинающаяся после &quot;access_token=&quot; и заканчивающаяся перед текстом &quot;&amp;expires_in&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:10pt;\">Причина бана:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#758eac;\" style=\" margin-top:5px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px; font-style:italic; color:#000000;\">0</span><span style=\" font-size:13px; color:#000000;\"> — другое (по умолчанию);</span></li>\n"
"<li style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#758eac;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px; font-style:italic; color:#000000;\">1</span><span style=\" font-size:13px; color:#000000;\"> — спам;</span></li>\n"
"<li style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#758eac;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px; font-style:italic; color:#000000;\">2</span><span style=\" font-size:13px; color:#000000;\"> — оскорбление участников;</span></li>\n"
"<li style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#758eac;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px; font-style:italic; color:#000000;\">3</span><span style=\" font-size:13px; color:#000000;\"> — нецензурные выражения;</span></li>\n"
"<li style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#758eac;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px; font-style:italic; color:#000000;\">4</span><span style=\" font-size:13px; color:#000000;\"> — сообщения не по теме.</span></li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Как пользоваться программой?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Для начала заполните все поля в &quot;Настройках группы&quot;. В ID группы укажите идентификатор той группы, в черный список которой будут добавляться пользователи. Выбираем тип объекта, откуда будем получать ID пользователей, которых потом сможем заблокировать. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Нажмите &quot;Выбрать пользователей&quot;, появится окно с дополнительными настройками. Заполните все необходимые поля и нажмите &quot;Продолжить&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Загрузка</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Теперь вы можете загрузить список выбранных пользователей, просто кликните &quot;Загрузить&quot;. Если после этого загрузка не началась, то, вероятно вы неверно указали какую-либо информацию. Проверьте, что если вы выбирали объект &quot;Голосование&quot; или &quot;Другое&quot; и владельцем является группа, вы указали знак &quot;-&quot; перед ID владельца объекта.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Если произошла ошибка</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Если вы неправильно ввели какую-то информацию и в работе программы произошла ошибка, рекомендуется открыть программу заново, т.к. эта ошибка может привести к ошибкам в последующей работе программы.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Анализ пользователей</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">После того как программа закончит загрузку, вы можете сравнить список  полученных пользователей и уже заблокированных в вашей группе, нажав на кнопку &quot;Сравнить&quot;. При этом, если был загружен большой список пользователей, окно может ненадолго зависнуть, дождитесь открытия нового окна.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Блокировка</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Теперь, загрузив список пользователей, вы можете начать процесс блокировки их в вашей группе. Выберите параметры блокировки в &quot;Настройках блокировки&quot;. Также можно оставить комментарий, но это крайне не рекомендуется, т.к. увеличит количество запросов на сервера ВК и может привести к нестабильной работе программы. Далее нажмите на кнопку &quot;Заблокировать&quot; и если вы выполнили все шаги правильно, начнется процесс блокировки. Если что-то пошло не так проверьте правильность введеной информации, а также удостоверьтесь что пользователь, чей токен вы вводили в поле &quot;Токен администратора&quot; обладает правами администратора/модератора в данной группе.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Почему блокируются не все пользователи?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Очень часто число загруженных пользователей и число забаненных будет не совпадать. Это происходит потому, что странницы этих пользователей либо удалены, либо заблокированны администрацией ВК.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Планы работ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:10pt; color:#000000;\">Сначала нужно создать новую сборку. Введите название и нажмите &quot;Создать&quot;. После этого выберите созданную сборку, нажав на нее в специальном поле выше и Вам будут доступны действия с данной сборкой: удалить, подробнее (там Вы можете посмотреть, какие действия записаны в данной сборке), добавить текущее задание (т.е. то что записано в главном окне программы), активировать.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,system-ui,Roboto,Helvetica Neue,sans-serif\'; font-size:13pt; color:#000000;\"><br /></p></body></html>"))
        self.mail.setText(_translate("help", "<html><head/><body><p>По всем вопросам: <a href=\"mailto:misstepdev@gmail.com?subject=BanManager\"><span style=\" text-decoration: underline; color:#0000ff;\">misstepdev@gmail.com</span></a></p></body></html>"))
        self.telegram.setText(_translate("help", "Telegram: @MReese"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    help = QtWidgets.QMainWindow()
    ui = Ui_help()
    ui.setupUi(help)
    help.show()
    sys.exit(app.exec_())

