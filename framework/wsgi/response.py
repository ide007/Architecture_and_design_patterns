from jinja2 import Environment, FileSystemLoader


def rendering(template_name: str, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка с шаблонами, в моем случаи ../templates
    :param kwargs: дополнительные параметры
    :return: рендеринг страницы
    """
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)


if __name__ == '__main__':
    page = rendering('index.html', books={
        'title': 'Руслан и Людмила',
        'author': 'А.С.Пушкин',
        'genre': 'Поэма'
    })
