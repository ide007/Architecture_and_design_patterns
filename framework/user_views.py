import os
import datetime
from urllib.parse import unquote

from mapper import MapperRegistry
from wsgi.unit_of_work import UnitOfWork
from wsgi.CBV import CreateView, ListView, TemplateView
from models import TrainingSite, SmsNotifier, EmailNotifier
from wsgi.response import rendering
from log_module import Logger, debug

site = TrainingSite()
logger = Logger('main')
sms_notifier = SmsNotifier()
email_notifier = EmailNotifier()
UnitOfWork.new_current()
UnitOfWork.get_current().set_mapper_registry(MapperRegistry)


def course_list(request):
    logger.log('Список курсов')
    return '200 OK', rendering('index.html', objects_list=site.courses)


@debug
def create_course(request):
    logger.log('Создание курса')
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
            new_course.observers.append(sms_notifier)
            new_course.observers.append(email_notifier)
            site.courses.append(new_course)
        categories = site.categories
        return '200 OK', rendering('create_course.html', categories=categories)
    else:
        categories = site.categories
        return '200 OK', rendering('create_course.html', categories=categories)


class CategoryCreateView(CreateView):

    template_name = 'create_category.html'
    logger.log('Создание категории')

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = site.categories
        return context

    def create_obj(self, data: dict):
        name = unquote(data['name'])
        category_id = data.get('category_id')

        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_category = site.create_category(name, category)
        site.categories.append(new_category)


class CategoryListView(ListView):

    queryset = site.categories
    template_name = 'category_list.html'
    logger.log('Список категорий')


class StudentCreateView(CreateView):

    template_name = 'create_student.html'
    logger.log('Регистрация студента')

    def create_object(self, data: dict):
        name = unquote(data['name'])
        new_student = site.create_user('student', name)
        site.students.append(new_student)
        new_student.mark_new()
        UnitOfWork.get_current().commit()

class StudentListView(ListView):

    logger.log('список студентов')
    queryset = site.students
    template_name = 'student_list.html'


class AddStudentByCourseCreateView(CreateView):

    template_name = 'add_student.html'
    logger.log('add_student')

    def get_context_data(self):
        context = super().get_context_data()
        context['courses'] = site.courses
        context['students'] = site.students
        return context

    def create_object(self, data: dict):
        print(data)
        course_name = unquote(data['course_name'])
        course = site.get_course(course_name)
        student_name = unquote(data['student_name'])
        student = site.get_student(student_name)
        course.add_student(student)


def about_view(request):
    logger.log('Страничка о нас')
    return '200 OK', rendering('about.html')


def contact_view(request):
    logger.log('Страница обратной связи')
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
