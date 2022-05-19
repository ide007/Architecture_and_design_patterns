import os
from datetime import datetime
from wsgi.response import rendering
from books import books


def home_view(request):
    return '200 OK', rendering('index.html', books=books)


def poem_view(request):
    return '200 OK', rendering('book.html', books=books[0])


def romance_view(request):
    return '200 OK', rendering('book.html', books=books[1])


def drama_view(request):
    return '200 OK', rendering('book.html', books=books[2])


def about_view(request):
    return '200 OK', 'About page'


def contact_view(request):
    if request['method'] == 'post':
        time_stamp = datetime.now()
        data = request['data']
        title = data['title']
        message = data['text']
        email = data['email']
        if not os.path.exists('messages'):
            os.mkdir('messages')

        with open(f'messages/message_{time_stamp.strftime("%d.%m.%Y")}_'
                  f'{time_stamp.strftime("%H:%M:%S")}.txt', 'w',
                  encoding='utf-8') as f:
            f.write(f'We received a message {time_stamp.strftime("%d.%m.%Y")}'
                    f' in {time_stamp.strftime("%H:%M:%S")}\n'
                    f'Sender: {email}\n'
                    f'Title: {title}\n'
                    f'Message: {message}')
        return '200 OK', rendering('contacts.html')
    else:
        return '200 OK', rendering('contacts.html')
