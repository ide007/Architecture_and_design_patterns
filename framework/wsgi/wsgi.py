class Framework:

    def __init__(self, urls: dict, controllers: list):
        self.urls = urls
        self.controllers = controllers

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        #
        # if path[-1] != '/':
        #     path = f'{path}/'

        method = environ['REQUEST_METHOD'].lower()
        input_data = self._get_wsgi_input_data(environ)
        parsed_data = self._parse_wsgi_input(input_data)

        query_string = environ['QUERY_STRING']
        query_params = self._parse_input_data(query_string)

        if path in self.urls:

            view = self.urls[path]
            request = {'method': method,
                       'data': parsed_data,
                       'request_params': query_params
                       }
            for controller in self.controllers:
                controller(request)
            status_code, text = view(request)
            start_response(status_code, [('Content-Type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            start_response('404 Page Not Found',
                           [('Content-Type', 'text/html')])
            return [b'Page Not Found']

    def _get_wsgi_input_data(self, environ):
        length_of_data = environ.get('CONTENT_LENGTH')
        content_length = int(length_of_data) if length_of_data else 0
        data = environ['wsgi.input'].read(content_length) \
            if content_length > 0 else b''
        return data

    def _parse_wsgi_input(self, data: bytes):
        result = {}
        if data:
            data_string = data.decode(encoding='utf-8')
            result = self._parse_input_data(data_string)
        return result

    def _parse_input_data(self, data: str):
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
