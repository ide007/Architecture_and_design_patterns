import sqlite3
from models import Student, Category, Course

connection = sqlite3.connect('patterns.sqlite')


class RecordNotFound(Exception):

    def __init__(self, message):
        super().__init__(f'Record not found: {message}')


class DataCommitException(Exception):

    def __init__(self, message):
        super().__init__(f'Database commit failed: {message}')


class DataUpdateException(Exception):

    def __init__(self, message):
        super().__init__(f'Database update data failed: {message}')


class DataDeleteException(Exception):

    def __init__(self, message):
        super().__init__(f'Database delete data failed: {message}')


class StudentMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.tablename = 'student'

    def all_students(self):
        statement = f'SELECT * FROM {self.tablename}'
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            id, name = item
            student = Student(name)
            student.id = id
            result.append(student)
        return result

    def find_by_id(self, id):
        statement = f'SELECT id, name FROM {self.tablename} WHERE id=?'
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()
        if result:
            return Student(*result)
        else:
            raise RecordNotFound(f'record with id = {id} not found')

    def insert(self, object):
        statement = f'INSERT INTO {self.tablename} (name) VALUES (?)'
        self.cursor.execute(statement, (object.name,))
        try:
            self.connection.commit()
        except Exception as err:
            raise DataCommitException(err.args)

    def update(self, object):
        statement = f'UPDATE {self.tablename} SET name=? WHERE id=?'
        self.cursor.execute(statement, (object.name, object.id))
        try:
            self.connection.commit()
        except Exception as err:
            raise DataUpdateException(err.args)

    def delete(self, object):
        statement = f'DELETE FROM {self.tablename} WHERE id=?'
        self.cursor.execute(statement, (object.id,))
        try:
            self.connection.commit()
        except Exception as err:
            raise DataDeleteException(err.args)


class CategoryMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor
        self.tablename = 'category'

    def all(self):
        statement = f'SELECT * FROM {self.tablename}'
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            id, name, category = item
            category_ = Category(name, category)
            category_.id = id
            result.append(category_)
        return result

    def find_category_by_id(self, id):
        statement = f'SELECT id, name FROM {self.tablename} WHERE id=?'
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()
        if result:
            return Category(*result)
        else:
            raise RecordNotFound(f'Record with id = {id}, not found.')

    def insert(self, object):
        statement = f'INSERT INTO {self.tablename} (name) VALUES (?)'
        self.cursor.execute(statement, (object.name,))
        try:
            self.connection.commit()
        except Exception as err:
            raise DataCommitException(err.args)

    def update(self, object):
        statement = f'UPDATE {self.tablename} SET name=? WHERE id=?'
        self.cursor.execute(statement, (object.name, object.id,))
        try:
            self.connection.commit()
        except Exception as err:
            raise DataUpdateException(err.args)

    def delete(self, object):
        statement = f'DELETE FROM {self.tablename} WHERE id=?'
        self.cursor.execute(statement, (object.id,))
        try:
            self.connection.commit()
        except Exception as err:
            raise DataDeleteException(err.args)


class CourseMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.tablename = 'course'

    def all(self):
        statement = f'SELECT * from {self.tablename}'
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            id, name, category = item
            course = Course(name, category)
            course.id = id
            result.append(course)
        return result

    def find_by_name(self, id):
        statement = f"SELECT id, name FROM {self.tablename} WHERE id=?"
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()
        if result:
            return Course(*result)
        else:
            raise RecordNotFound(f'Record with id={id} not found')

    def insert(self, object):
        statement = f"INSERT INTO {self.tablename} (name) VALUES (?)"
        self.cursor.execute(statement, (object.name,))
        try:
            self.connection.commit()
        except Exception as err:
            raise DataCommitException(err.args)

    def update(self, object):
        statement = f"UPDATE {self.tablename} SET name=? WHERE id=?"
        self.cursor.execute(statement, (object.name, object.id))
        try:
            self.connection.commit()
        except Exception as err:
            raise DataUpdateException(err.args)

    def delete(self, object):
        statement = f"DELETE FROM {self.tablename} WHERE id=?"
        self.cursor.execute(statement, (object.id,))
        try:
            self.connection.commit()
        except Exception as err:
            raise DataDeleteException(err.args)


class MapperRegistry:

    mappers = {
        'student': StudentMapper,
        'category': CategoryMapper,
        'course': CourseMapper,
    }

    @staticmethod
    def get_mapper(object):
        if isinstance(object, Student):
            return StudentMapper(connection)
        if isinstance(object, Category):
            return CategoryMapper(connection)
        if isinstance(object, Course):
            return CourseMapper(connection)

    @staticmethod
    def get_current_mapper(name):
        return MapperRegistry.mappers[name](connection)
