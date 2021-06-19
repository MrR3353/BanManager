import requests, time, datetime, math

class VkApi:
    templates = False
    signal = None
    stop = False
    proxy = None
    group_token = ''
    service_key = '*'
    user_token = ''
    base_url = 'https://api.vk.com/method/'
    version = 7.54
    err2text = {1: 'Произошла неизвестная ошибка. Попробуйте повторить запрос позже.',
     2: 'Приложение выключено. Необходимо включить приложение в настройках.',
     3: 'Передан неизвестный метод.',
     4: 'Неверная подпись.',
     5: 'Авторизация пользователя не удалась.',
     6: 'Слишком много запросов в секунду.',
     7: 'Нет прав для выполнения этого действия.',
     8: 'Неверный запрос.',
     9: 'Слишком много однотипных действий.',
     10: 'Произошла внутренняя ошибка сервера. Попробуйте повторить запрос позже.',
     11: 'В тестовом режиме приложение должно быть выключено или пользователь должен быть залогинен.',
     14: 'Требуется ввод кода с картинки(Captcha).',
     15: 'Доступ запрещён.',
     16: 'Требуется выполнение запросов по протоколу HTTPS.',
     17: 'Требуется валидация пользователя.',
     18: 'Страница удалена или заблокирована.',
     20: 'Данное действие запрещено для не Standalone приложений.',
     21: 'Данное действие разрешено только для Standalone и Open API приложений.',
     23: 'Метод был выключен.',
     24: 'Требуется подтверждение со стороны пользователя.',
     27: 'Ключ доступа сообщества недействителен.',
     28: 'Ключ доступа приложения недействителен.',
     29: 'Достигнут количественный лимит на вызов метода.',
     100: 'Один из необходимых параметров был не передан или неверен.',
     101: 'Неверный API ID приложения.',
     113: 'Неверный идентификатор пользователя.',
     150: 'Неверный timestamp.',
     203: 'Доступ к группе запрещён.',
     500: 'Действие запрещено.'}
    captcha = ''
    captcha_sid = ''
    summary = 0
    iter_count = 0
    iter_remain = 0

    def remaining(self):
        return datetime.timedelta(seconds=int(self.summary / self.iter_count * self.iter_remain))

    def is_working(self):
        method = 'users.get'
        try:
            response = requests.get(self.base_url + method, params={'access_token': self.service_key,
             'user_ids': 1,
             'v': self.version}, proxies=self.proxy, timeout=10)
            return response.status_code == 200
        except:
            return False

    def set_online(self, token):
        method = 'account.setOnline'
        try:
            response = requests.get(self.base_url + method, params={'access_token': token,
             'v': self.version}, proxies=self.proxy)
            return
        except:
            self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
            return

    def is_banned(self, user_id):
        method = 'users.get'
        try:
            response = requests.get(self.base_url + method, params={'access_token': self.service_key,
             'user_ids': user_id,
             'v': self.version}, proxies=self.proxy)
            return response.json()
        except:
            self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
            return

    def user_get_id(self, token):
        method = 'users.get'
        id = 0
        response = requests.get(self.base_url + method, params={'access_token': token,
         'v': self.version}, proxies=self.proxy)
        if response.status_code == requests.codes.ok:
            response = response.json()
            if 'error' in response:
                response = response['error']
                code = response['error_code']
                self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                return
            response = response['response'][0]['id']
        else:
            self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
        return response

    def get_vk_banned(self, users_id):
        method = 'users.get'
        id = []
        i = 0
        request_count = 1
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': self.service_key,
                 'user_ids': users_id[i:i + request_count],
                 'v': self.version}, proxies=self.proxy)
                if response.status_code == requests.codes.ok:
                    response = response.json()
                    if 'error' in response:
                        response = response['error']
                        code = response['error_code']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        return id
                    response = response['response']
                    for user in response:
                        if 'deactivated' in user:
                            id.append(user['id'])

                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    count = len(users_id)
                    self.iter_remain = (count - i) / request_count if count > i else 0
                    self.signal.emit([i, count, 'Проверка заблокированных пользователей...  Осталось: ' + self.remaining()])
                    i += request_count
                    if i >= count:
                        self.signal.emit([count, count])
                        break
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break

        return id

    def get_members_count(self, group_id):
        method = 'groups.getMembers'
        count = 0
        response = requests.get(self.base_url + method, params={'access_token': self.service_key,
         'group_id': group_id,
         'offset': 0,
         'v': self.version}, proxies=self.proxy)
        if response.status_code == requests.codes.ok:
            response = response.json()
            if 'error' in response:
                response = response['error']
                code = response['error_code']
                self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                return
            response = response['response']
            count = response['count']
        else:
            self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
        return count



    def group_get_banned(self, group_id, token):
        """
        Uses only if you had access to this group(admin/group group_token)
        :return: list of banned users and groups(only id)
        {'group': [...], 'profile': [...]}

        Totally, as i understand is 2 types of banned users: profile/group
        """
        method = 'groups.getBanned'
        id = []
        i = 0
        request_count = 200
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': token,
                 'group_id': group_id,
                 'fields': 'id',
                 'count': request_count,
                 'offset': i,
                 'v': self.version}, proxies=self.proxy)
                if response.status_code == requests.codes.ok:
                    response = response.json()
                    if 'error' in response:
                        response = response['error']
                        code = response['error_code']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        return id
                    response = response['response']
                    items = response['items']
                    for d in items:
                        if d['type'] == 'profile':
                            id.append(d['profile']['id'])

                    count = response['count']
                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    self.iter_remain = (count - i) / request_count if count > i else 0
                    self.signal.emit([i, count, 'Получение списка заблокированных пользователей...  Осталось: ' ])
                    i += request_count
                    if i >= count:
                        self.signal.emit([count, count])
                        break
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break

        return id

    def user_get_banned(self, token):
        """
        Uses only if you had access to this user
        :return: list of banned users and groups(only id)
        {'group': [...], 'profile': [...]}

        Totally, as i understand is 2 types of banned users: profile/group
        """
        method = 'account.getBanned'
        id = []
        i = 0
        request_count = 200
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': token,
                 'count': request_count,
                 'offset': i,
                 'v': self.version}, proxies=self.proxy)
                if response.status_code == requests.codes.ok:
                    response = response.json()
                    if 'error' in response:
                        response = response['error']
                        code = response['error_code']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        return id
                    response = response['response']
                    items = response['items']
                    id += items
                    count = response['count']
                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    self.iter_remain = (count - i) / request_count if count > i else 0
                    self.signal.emit([i, count, 'Получение списка заблокированных пользователей...  Осталось: ' + self.remaining()])
                    i += request_count
                    if i >= count:
                        self.signal.emit([count, count])
                        break
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break
        return id

    def group_get_members(self, group_id):
        """
        You can have not straight access to this group
        :param group_id:
        :return: dict with normal users, banned and deleted
        """
        method = 'groups.getMembers'
        id = []
        i = 0
        request_count = 1000
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': self.service_key,
                 'group_id': group_id,
                 'count': request_count,
                 'offset': i,
                 'v': self.version}, proxies=self.proxy)
                if response.status_code == requests.codes.ok:
                    response = response.json()
                    if 'error' in response:
                        response = response['error']
                        code = response['error_code']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        return id
                    response = response['response']
                    items = response['items']
                    count = response['count']
                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    self.iter_remain = (count - i) / request_count if count > i else 0
                    self.signal.emit([i, count, 'Получение списка участников группы...  Осталось: ' + self.remaining()])
                    id += items
                    i += request_count
                    if i >= count:
                        self.signal.emit([count, count])
                        break
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break

        return id

    def user_get_friends(self, user_id):
        """
        Returns friends of given user
        :param user_id:
        :return:
        """
        method = 'friends.get'
        id = []
        i = 0
        request_count = 5000
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': self.service_key,
                 'user_id': user_id,
                 'count': request_count,
                 'offset': i,
                 'v': self.version}, proxies=self.proxy)
                if response.status_code == requests.codes.ok:
                    response = response.json()
                    if 'error' in response:
                        response = response['error']
                        code = response['error_code']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        return id
                    response = response['response']
                    items = response['items']
                    count = response['count']
                    id += items
                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    self.iter_remain = (count - i) / request_count if count > i else 0
                    self.signal.emit([i, count, 'Получение списка друзей...  Осталось: ' + str(self.remaining())])
                    i += request_count
                    if i >= count and i >= count:
                        self.signal.emit([count, count])
                        break
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break

        return id

    # def user_get_followers(self, user_id):
    #     """
    #     Returns followers of user
    #     :param user_id:
    #     :return:
    #     """
    #     method = 'users.getFollowers'
    #     id = []
    #     i = 0
    #     request_count = 1000
    #     self.summary = 0
    #     self.iter_count = 0
    #     self.iter_remain = 0
    #     while 1:
    #         if not self.stop:
    #             start = time.time()
    #             response = requests.get(self.base_url + method, params={'access_token': self.service_key,
    #              'user_id': user_id,
    #              'count': request_count,
    #              'offset': i,
    #              'v': self.version}, proxies=self.proxy)
    #             if response.status_code == requests.codes.ok:
    #                 response = response.json()
    #                 if 'error' in response:
    #                     response = response['error']
    #                     code = response['error_code']
    #                     self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
    #                     return id
    #                 response = response['response']
    #                 items = response['items']
    #                 count = response['count']
    #                 id += items
    #                 lap = time.time() - start
    #                 self.summary += lap
    #                 self.iter_count += 1
    #                 self.iter_remain = (count - i) / request_count if count > i else 0
    #                 i += request_count
    #                 if i >= count:
    #                     break
    #             else:
    #                 self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
    #                 break
    #
    #     return id

    def get_liked(self, object_type, owner_id, item_id):
        """
        Returns list of users which liked this post
        :param object_type: type of object (post,comment,photo,audio,video,note,market,photo_comment,video_comment,topic_comment,market_comment,sitepage)
        :param owner_id:
        :param item_id:
        :return:
        """
        method = 'likes.getList'
        id = []
        i = 0
        request_count = 1000
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': self.service_key,
                 'owner_id': owner_id,
                 'item_id': item_id,
                 'type': object_type,
                 'count': request_count,
                 'offset': i,
                 'v': self.version}, proxies=self.proxy)
                if response.status_code == requests.codes.ok:
                    response = response.json()
                    if 'error' in response:
                        response = response['error']
                        code = response['error_code']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        return id
                    response = response['response']
                    items = response['items']
                    count = response['count']
                    id += items
                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    self.iter_remain = (count - i) / request_count if count > i else 0
                    self.signal.emit([i, count, 'Получение списка лайкнувших...  Осталось: ' + self.remaining()])
                    i += request_count
                    if i >= count:
                        self.signal.emit([count, count])
                        break
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break

        return id

    def get_reposted(self, object_type, owner_id, item_id):
        """
        Returns list of users which liked this post
        :param object_type: type of object (post,comment,photo,audio,video,note,market,photo_comment,video_comment,topic_comment,market_comment,sitepage)
        :param owner_id:
        :param item_id:
        :return:
        """
        method = 'likes.getList'
        id = []
        i = 0
        request_count = 1000
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': self.service_key,
                 'owner_id': owner_id,
                 'item_id': item_id,
                 'type': object_type,
                 'filter': 'copies',
                 'count': request_count,
                 'offset': i,
                 'v': self.version}, proxies=self.proxy)
                if response.status_code == requests.codes.ok:
                    response = response.json()
                    if 'error' in response:
                        response = response['error']
                        code = response['error_code']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        return id
                    response = response['response']
                    items = response['items']
                    count = response['count']
                    id += items
                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    self.iter_remain = (count - i) / request_count if count > i else 0
                    self.signal.emit([i, count, 'Получение списка репостнувших...  Осталось: ' + self.remaining()])
                    i += request_count
                    if i >= count:
                        self.signal.emit([count, count])
                        break
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break

        return id

    def get_commented(self, owner_id, post_id):
        method = 'wall.getComments'
        owners_id = []
        comments_id = []
        i = 0
        request_count = 100
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': self.service_key,
                 'owner_id': owner_id,
                 'post_id': post_id,
                 'count': request_count,
                 'offset': i,
                 'v': self.version}, proxies=self.proxy)
                if response.status_code == requests.codes.ok:
                    response = response.json()
                    if 'error' in response:
                        response = response['error']
                        code = response['error_code']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        return id
                    response = response['response']
                    items = response['items']
                    count = response['count']
                    for rec in items:
                        owners_id.append(rec['from_id'])
                        comments_id.append(rec['id'])

                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    self.iter_remain = (count - i) / request_count if count > i else 0
                    self.signal.emit([i, count, 'Получение списка комментировавших...  Осталось: ' + self.remaining()])
                    i += request_count
                    if i >= count:
                        self.signal.emit([count, count])
                        break
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break

        return [
         comments_id, owners_id]

    def get_liked_comments(self, owner_id, post_id):
        x = self.get_commented(owner_id, post_id)
        comments = x[0]
        res = []
        for c in range(len(comments)):
            res += self.get_liked('comment', owner_id, comments[c])

        return res

    def get_voters(self, user_token, owner_id, poll_id, answer_ids, is_board):
        """
        Returns voters of specified answer
        :param owner_id: group/user id
        :param poll_id: take from code in 'Get code', this link specified in poll
        :param answer_ids: go to browser, click on specified variant -> showElementCode
         (click mouse on button with needed variant)
        (Example:  <a class="summary_tab2" onclick="WkPoll.tab(983189218)" id="wk_poll_opt983189218">)
        :return:
        """
        method = 'polls.getVoters'
        id = []
        i = 0
        request_count = 1000
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': user_token,
                 'owner_id': owner_id,
                 'poll_id': poll_id,
                 'answer_ids': answer_ids,
                 'is_board': is_board,
                 'count': request_count,
                 'offset': i,
                 'v': self.version}, proxies=self.proxy)
                if response.status_code == requests.codes.ok:
                    response = response.json()
                    if 'error' in response:
                        response = response['error']
                        code = response['error_code']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        return id
                    response = response['response'][0]['users']
                    items = response['items']
                    count = response['count']
                    id += items
                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    self.iter_remain = (count - i) / request_count if count > i else 0
                    self.signal.emit([i, count, 'Получение списка проголосовавших...  Осталось: ' + self.remaining()])
                    i += request_count
                    if i >= count:
                        self.signal.emit([count, count])
                        break
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break

        return id

    def get_topics(self, group_id):
        """
        Returns list of topics from group
        :return:
        """
        method = 'board.getTopics'
        id = []
        i = 0
        request_count = 100
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': self.service_key,
                 'group_id': group_id,
                 'count': request_count,
                 'offset': i,
                 'v': self.version}, proxies=self.proxy)
                if response.status_code == requests.codes.ok:
                    response = response.json()
                    if 'error' in response:
                        response = response['error']
                        code = response['error_code']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        return id
                    response = response['response']
                    items = response['items']
                    count = response['count']
                    for item in items:
                        id += [item['id']]

                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    self.iter_remain = (count - i) / request_count if count > i else 0
                    self.signal.emit([i, count, 'Получение списка тем...  Осталось: ' + self.remaining()])
                    i += request_count
                    if i >= count:
                        self.signal.emit([count, count])
                        break
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break

        return id

    def get_comments_id(self, group_id, topic_id):
        """
        Returns list of ids of comments
        :return:
        """
        method = 'board.getComments'
        comments_id = []
        owners_id = []
        i = 0
        request_count = 100
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': self.service_key,
                 'group_id': group_id,
                 'topic_id': topic_id,
                 'count': request_count,
                 'offset': i,
                 'v': self.version}, proxies=self.proxy)
                if response.status_code == requests.codes.ok:
                    response = response.json()
                    if 'error' in response:
                        response = response['error']
                        code = response['error_code']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        print(response)
                        return
                    response = response['response']
                    items = response['items']
                    count = response['count']
                    for item in items:
                        comments_id += [item['id']]
                        owners_id += [item['from_id']]

                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    self.iter_remain = (count - i) / request_count if count > i else 0
                    self.signal.emit([i, count, 'Получение списка комментариев...  Осталось: ' + self.remaining()])
                    i += request_count
                    if i >= count:
                        self.signal.emit([count, count])
                        break
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break

        return [
         comments_id, owners_id]

    def user_get_followers(self, user_id):
        """
        Returns followers of user
        :param user_id:
        :return:
        """
        method = 'users.getFollowers'

        request_count = 1000

        params = {'access_token': self.service_key,
                'user_id': user_id,
                'count': request_count,
                'v': self.version}

        description = "Получение списка подписчиков"
        code1 = '''
response = response['response']
max_count += [response['count']]
response = response['items']
max_count = max_count[0]
res += response
        '''
        code = '''
response = []'''
#         code = "response = response['response']\n" \
#                "count = response['count']\n" \
#                "response = response['items']\n" \
#                "print(response)\n"

        self.get(method, 1000, params, True, code, description)

    def get(self, method, step, params_base, is_offset, response_process, description):
        '''
        Wrapper for functions which get sth from vk api
        :param method: method of vk api, which invokes
        :param step: how much users (oe sth other will process at 1 cycle)
        :param params_base: base of params in requests (sth, what willn't change)
        :param is_offset: do we need add offset changes to params? <{'offset': i}>
         Looks like: <params_changes = {'offset': i}> or <{}> usually
        :param response_process: code which i'll execute after getting response(different for few functions)
        :param description: description for info bar
        :return:
        '''
        summary = 0
        max_count = []  # common count of users (or sth other)
        res = []
        i = 0
        while not self.stop:
            start = time.time()
            offset = {}
            if is_offset:
                offset = {'offset': i}
            response = requests.get(self.base_url + method, params={**params_base, **offset}, proxies=self.proxy)
            if response.status_code == requests.codes.ok:
                response = response.json()
                if 'error' in response:
                    response = response['error']
                    code = response['error_code']
                    self.signal.emit([0, 0, 'Ошибка {0}: {1}'.format(code, self.err2text[code])])
                    return None
                # print(response)
                exec(response_process)
                print(response)
                # print(max_count)
                # print(res)
                # res += response
                i += step
                if i >= max_count:
                    # self.signal.emit([count, count])
                    break
                summary += (time.time() - start)
                time_left = summary / (i / step) * math.ceil(max_count / step - (i / step))
                # self.signal.emit([i, count, description + '... Осталось: ' + str(datetime.timedelta(seconds=time_left))])
            else:
                self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                return None
        # self.signal.emit([count, count, description + '. Выполнено.'])
        return res

    def post(self, method, token, users, users_step, repeat, delay, code_part, code_values, description):
        '''
        Wrapper for functions which post sth with vk api
        :param method: which method of vk api is invokes
        :param token: group or user token
        :param users: users id
        :param users_step: how many users we take in 1 call
        :param repeat: how many calls we do without pause
        :param delay: delay between calls
        :param code_part: part of code for Vk, where defines 'a' variable
        :param code_values: values which inserts in the code, []
        :param description: Description of action for status bar
        :return: void
        '''

        def put_commas(arr):
            res = ''
            for i in arr:
                res += str(i) + ','
            return res[:-1]

        print(method)
        time_left = (math.ceil(len(users) / users_step / repeat) - 1) * users_step * repeat

        i = 0
        self.signal.emit([i, len(users),
                          description + ' Осталось: ' + str(datetime.timedelta(seconds=time_left))])

        while i < len(users):
            if self.stop:
                return
            if not i % (repeat * users_step) and i != 0:  # pause
                time_left = math.ceil((len(users) - i) / users_step / repeat) * users_step * repeat
                for j in range(delay):
                    if self.stop:
                        return
                    time.sleep(1)
                    if time_left > 0:
                        time_left -= 1
                    self.signal.emit([i, len(users),
                                      description + '... Осталось: ' + str(datetime.timedelta(seconds=time_left))])

            users2post = put_commas(users[i:i + users_step])
            code = ('var u = [{0}];'
                    'var r = "";'
                    'var i = 0;'
                    'var t = "";'
                    'while (i < u.length){{' +
                    code_part +
                    't = t + a;'
                    'if (t != "") {{'
                    'r = r + i + " ";}}'
                    't = "";'
                    'i = i + 1;}}'
                    'return r;'
                    '').format(users2post, *code_values)

            response = requests.get(self.base_url + method, params={'access_token': token,
                                                                    'code': code,
                                                                    'v': self.version}, proxies=self.proxy)
            if response.status_code == requests.codes.ok:
                print(response.text)
            else:
                print('ERROR')
                self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
            i += users_step
        self.signal.emit([len(users), len(users), description + '. Выполнено.'])

    def group_ban(self, user_token, users_id, group_id, end_date, reason=0, comment='', comment_visible=0):
        method = 'execute'
        description = 'Блокировка пользователей'
        code_part = 'var a = API.groups.ban({{"group_id": {1}, "owner_id": u[i], "access_token": "{2}", {3} ' \
                    '"reason": {4}, "comment": "{5}", "comment_visible" : {6}}});'
        code_values = [group_id, user_token, end_date, reason, comment, comment_visible]
        self.post(method, user_token, users_id, 20, 3, 60, code_part, code_values, description)

    def user_ban(self, user_token, users_id):
        method = 'execute'
        description = 'Блокировка пользователей'
        code_part = 'var a = API.account.ban({{"owner_id": u[i], "access_token": "{1}"}});'
        code_values = [user_token]
        self.post(method, user_token, users_id, 10, 3, 60, code_part, code_values, description)

    def group_unban(self, user_token, group_id, users_id):
        method = 'execute'
        description = 'Разблокировка пользователей'
        code_part = 'var a = API.groups.unban({{"owner_id": u[i], "access_token": "{1}", "group_id": {2}}});'
        code_values = [user_token, group_id]
        self.post(method, user_token, users_id, 20, 6, 1, code_part, code_values, description)

    def user_unban(self, user_token, users_id):
        method = 'execute'
        description = 'Разблокировка пользователей'
        code_part = 'var a = API.account.unban({{"owner_id": u[i], "access_token": "{1}"}});'
        code_values = [user_token]
        self.post(method, user_token, users_id, 10, 3, 30, code_part, code_values, description)

    def user_report(self, token, users_id, reason, comment):
        method = 'users.report'
        i = 0
        self.summary = 0
        self.iter_count = 0
        self.iter_remain = 0
        while 1:
            if not self.stop:
                start = time.time()
                response = requests.get(self.base_url + method, params={'access_token': token,
                                                                        'user_id': users_id[i],
                                                                        'type': reason,
                                                                        'comment': comment,
                                                                        'captcha_sid': self.captcha_sid,
                                                                        'captcha_key': self.captcha,
                                                                        'v': self.version}, proxies=self.proxy)
                if self.captcha:
                    self.captcha = ''
            if response.status_code == requests.codes.ok:
                response = response.json()
                if 'error' in response:
                    response = response['error']
                    code = response['error_code']
                    print(response)
                    if int(code) == 14:
                        self.captcha_sid = response['captcha_sid']
                        link = response['captcha_img']
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code]), link])
                        while 1:
                            if not self.captcha:
                                time.sleep(0.5)
                        continue
                        self.signal.emit([0, 0, ('Ошибка {0}: {1}').format(code, self.err2text[code])])
                        return
                    print(response)
                    lap = time.time() - start
                    self.summary += lap
                    self.iter_count += 1
                    self.iter_remain = (len(users_id) - i) / 1 if len(users_id) > i else 0
                    self.signal.emit([i, len(users_id), 'Получение списка заблокированных пользователей...  Осталось: ' + self.remaining()])
                    i += 1
                    if i >= len(users_id):
                        self.signal.emit([len(users_id), len(users_id)])
                        break
                    time.sleep(1)
                else:
                    self.signal.emit([0, 0, 'Произошла ошибка подключения!'])
                    break


vk = VkApi()
vk.user_get_followers(303250564)