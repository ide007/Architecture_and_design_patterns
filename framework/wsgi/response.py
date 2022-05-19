import os.path

from jinja2 import Template


def rendering(url: str, folder='templates', **kwargs):
    """
    :param url: url
    :param folder: папка с шаблонами, в моем случаи ../templates
    :param kwargs: дополнительные параметры
    :return: рендеринг страницы
    """
    file_path = os.path.join(folder, url)
    with open(file_path, encoding='utf-8') as file:
        template = Template(file.read())

    return template.render(**kwargs)


if __name__ == '__main__':
    page = rendering('index.html', books={
        'title': 'Руслан и Людмила',
        'author': 'А.С.Пушкин',
        'genre': 'Поэма'
    })
    # print(page)
