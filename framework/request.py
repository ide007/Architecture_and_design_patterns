class Request:
    def __init__(self, environ):
        self.headers = self._get_headers(environ)
        self.method = environ['REQUEST_METHOD'].lower()
        self.body = environ.get('wsgi.input')
        self.path = environ['PATH_INFO']
        self.query_params = self._get_query_params(environ)

    def _get_query_params(self, environ):
        query_param = {}
        data = environ['QUERY_STRING'].split('&')
        for el in data:
            if el:
                key, value = el.split('=')
                if query_param.get(key):
                    query_param[key].append(value)
                else:
                    query_param[key] = [value]
        return query_param

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].lower()] = value
        return headers
