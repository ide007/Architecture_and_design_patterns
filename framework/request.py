class Request:
    def __init__(self, environ):
        self.headers = self._get_headers(environ)
        self.method = self._get_method(environ)
        self.body = environ.get('wsgi.input')
        self.path = environ['PATH_INFO']
        # self.query_params = 0

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].capitalize()] = value
                # headers[key[5:].lower()] = value
        return headers

    def _get_method(self, environ):
        methods = ['GET', 'PUT', 'POST', 'DELETE', 'HEAD', 'CONNECT',
                   'OPTIONS', 'PATCH']
        for key, value in environ.items():
            if key.startswith('REQUEST_METHOD'):
                if value in methods:
                    return value
                return b'Request received with unknown method.'
            return None
