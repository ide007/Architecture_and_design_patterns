import jsonpickle as jsonpickle

from wsgi.unit_of_work import DomainObject
from patterns.prototype import PrototypeMixin
from patterns.observer import Observer, Subject


class User:
    def __init__(self, name):
        self.name = name


class Teacher(User):
    pass


class Student(User, DomainObject):

    def __init__(self, name):
        self.courses = []
        super().__init__(name)


class UserFactory:

    types = {
        'студент': Student,
        'учитель': Teacher,
    }

    @classmethod
    def create(cls, type_, name):
        return cls.types[type_](name)


class Category:
    auto_id = 0

    def __getitem__(self, item):
        return self.courses[item]

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


class Course(PrototypeMixin, Subject):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)
        self.students = []
        super().__init__()

    def __getitem__(self, item):
        return self.students[item]

    def add_student(self, student: Student):
        self.students.append(student)
        student.courses.append(self)
        self.notify()


class OnlineCourse(Course):
    pass


class RecordCourse(Course):
    pass


class OffLineCourse(Course):
    pass


class CourseFactory:
    types = {
        'он-лайн': OnlineCourse,
        'офф-лайн': OffLineCourse,
        'записанный': RecordCourse,
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


class TrainingSite:

    def __init__(self):
        self.students = []
        self.teachers = []
        self.categories = []
        self.courses = []

    def create_user(self, type_, name):
        return UserFactory.create(type_, name)

    def create_category(self, name, category=None):
        return Category(name, category)

    def create_course(self, type_, name, category):
        return CourseFactory.create(type_, name, category)

    def find_category_by_id(self, id):
        for item in self.categories:
            print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'Нет категории с id = {id}.')

    def get_course(self, name) -> Course:
        for item in self.courses:
            print('курс : ', item)
            if item.name == name:
                return item

    def get_student(self, name) -> Student:
        for item in self.students:
            if item.name == name:
                return item


class SmsNotifier(Observer):

    def update(self, subject: Course):
        print('SMS -> ', subject.students[-1].name, ' присоединился к нам.')


class EmailNotifier(Observer):

    def update(self, subject: Course):
        print('SMS -> ', subject.students[-1].name, ' присоединился к нам.')


class BaseSerializer:

    def __init__(self, object):
        self.object = object

    def save(self):
        return jsonpickle.dumps(self.object)

    def load(self, data):
        return jsonpickle.loads(data)
