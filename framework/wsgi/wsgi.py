import urllib.parse


class Framework:

    def __init__(self, urls: dict, controllers: list):
        """
        :param urls: словарь связок urls : view
        :param controllers: список контроллеров
        """
        self.urls = urls
        self.controllers = controllers

    def add_route(self, url):
        def inner(view):
            self.urls[url] = view
        return inner

    def __call__(self, environ, start_response):
        # текущий url
        path = environ['PATH_INFO']

        # # добавление закрывающего слеша
        # if path[-1] != '/':
        #     path = f'{path}/'

        # Получаем данные запроса
        method = environ['REQUEST_METHOD'].lower()
        input_data = self._get_wsgi_input_data(environ)
        parsed_data = self._parse_wsgi_input(input_data)

        query_string = environ['QUERY_STRING']
        query_params = self._parse_input_data(query_string)

        if path in self.urls:
            # Получаем view по url
            view = self.urls[path]
            # параметры запросов
            request = {'method': method,
                       'data': parsed_data,
                       'request_params': query_params
                       }
            # добавляем данные из контроллеров
            for controller in self.controllers:
                controller(request)
            # вызываем view, получаем результат
            status_code, text = view(request)
            start_response(status_code, [('Content-Type', 'text/html')])
            # возвращаем тело ответа
            return [text.encode('utf-8')]
        else:
            # если url нет в словаре доступных urls, возвращаем
            # "404 Страница не найдена"
            start_response('404 Page Not Found',
                           [('Content-Type', 'text/html')])
            return [b'Page Not Found']

    def _get_wsgi_input_data(self, environ):
        # Определяем объем контента
        length_of_data = environ.get('CONTENT_LENGTH')
        content_length = int(length_of_data) if length_of_data else 0
        data = environ['wsgi.input'].read(content_length) \
            if content_length > 0 else b''
        return data

    def _parse_wsgi_input(self, data: bytes):
        """
        :param data: принимает байты, декодирует и передает строку
            в функцию _parse_input_data.
        :return: возвращает словарь с декодированными данными.
        """
        result = {}
        if data:
            data_string = data.decode(encoding='utf-8').replace('+', ' ')
            data_string = urllib.parse.unquote(data_string)
            result = self._parse_input_data(data_string)
        return result

    def _parse_input_data(self, data: str):
        """
        :param data: принимает строку, разделяет по & и формирует словарь.
        :return: возвращает сформированный словарь.
        """
        result = {}
        if data:
            params = data.split('&')
            for i in params:
                key, value = i.split('=')
                if result.get(key):
                    result[key] = value
                else:
                    result[key] = value

        return result


class DebugApplication(Framework):

    def __init__(self, url, controller):
        self.application = Framework(url, controller)
        super().__init__(url, controller)

    def __call__(self, environ, start_response):
        print('Debug mode ')
        return self.application(environ, start_response)


class FakeApplication(Framework):

    def __init__(self, url, controller):
        self.application = Framework(url, controller)
        super().__init__(url, controller)

    def __call__(self, environ, start_response):
        print('FakeApplication mode ')
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from Fake']
