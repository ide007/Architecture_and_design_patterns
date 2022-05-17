from pprint import pprint

from request import Request


def app(environ, start_response):
    # pprint(environ)
    # request = Request(environ)
    # print(request.headers)
    # print(request.body.read())
    data = b'Hello world from a simple WSGI application!\n'
    start_response('200 OK', [('Content-Type', 'text/html'),
                              ("Content-Length", str(len(data)))
                              ])
    return iter([data])
