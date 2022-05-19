from wsgi.wsgi import Framework
from user_urls import user_url


def books_controller(request):
    request['books'] = {
        'title': 'Руслан и Людмила',
        'author': 'А.С.Пушкин',
        'genre': 'Поэма'
    }


controller = [books_controller]

app = Framework(user_url, controller)
