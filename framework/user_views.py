import os
import datetime

from models import TrainingSite
from wsgi.response import rendering
from log_module import Logger

site = TrainingSite()
logger = Logger('main')


def home(request):
    logger.log('Список курсов')
    return '200 OK', rendering('index.html', objects_list=site.courses)


def create_course(request):
    if request['method'] == 'post':
        data = request['data']
        print('<==>', data['name'].encode('utf-8').decode('utf-8'))
        course_name = data['name'].encode('utf-8').decode('utf-8')
        category_id = data.get('category_id')
        print('category_id: ', category_id)
        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))
            new_course = site.create_course(type_='он-лайн', name=course_name,
                                            category=category)
            site.courses.append(new_course)
        return '200 OK', rendering('create_course.html')
    else:
        categories = site.categories
        return '200 OK', rendering('create_course.html', categories=categories)


def create_category(request):
    if request['method'] == 'post':
        data = request['data']
        print('==>', data['name'].encode('utf-8').decode('utf-8'))
        category_name = data['name'].encode('utf-8').decode('utf-8')
        category_id = data.get('category_id')
        category = None

        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_category = site.create_category(category_name, category)
        site.categories.append(new_category)
        return '200 OK', rendering('create_category.html')
    else:
        categories = site.categories
        return '200 OK', rendering('create_category.html',
                                   categories=categories)


def about_view(request):
    return '200 OK', rendering('about.html')


def contact_view(request):
    if request['method'] == 'post':
        time_stamp = datetime.datetime.now()
        data = request['data']

        input_data = {}
        for key, value in data.items():
            input_data[key] = value
        # print(type(input_data), input_data)

        title = input_data['title']
        message = input_data['message']
        email = input_data['email']
        if not os.path.exists('messages'):
            os.mkdir('messages')

        with open(f'messages/message_{time_stamp.strftime("%d-%m-%Y")}'
                  f'_{time_stamp.strftime("%H%M%S")}.txt', 'w',
                  encoding='utf-8') as f:
            f.write(f'We received a message {time_stamp.strftime("%d-%m-%Y")}'
                    f' in {time_stamp.strftime("%H:%M:%S")}\n'
                    f'Sender: {email}\n'
                    f'Title: {title}\n'
                    f'Message: {message}')
        return '200 OK', rendering('contacts.html')
    else:
        return '200 OK', rendering('contacts.html')
