import os.path

from jinja2 import Template


class Response:

    def __init__(self, path):
        self.path = path

    def __call__(self, folder='templates', **kwargs):
        """
        :param path: имя шаблона
        :param folder: папка с шаблонами, в моем случаи ../templates
        :param kwargs: дополнительные параметры
        :return: рендеринг страницы
        """
        file_path = os.path.join(folder, self.path)
        with open(file_path, encoding='utf-8') as file:
            template = Template(file.read())

        return '200 OK', template.render(**kwargs)


if __name__ == '__main__':
    page = Response('index.html')
