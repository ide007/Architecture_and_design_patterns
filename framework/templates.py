import os.path

from test_data import *
from jinja2 import Template


def render_template(template_name, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка с шаблонами, в моем случаи ../templates
    :param kwargs: дополнительные параметры
    :return: рендеринг страницы
    """
    file_path = os.path.join(folder, template_name)

    with open(file_path, encoding='utf-8') as file:
        template = Template(file.read())

    return template.render(**kwargs)


if __name__ == '__main__':
    test = render_template('index.html', page={'position': 'Base',
     'first_stage': 'first_basic_stage',
     'secondary_stage': 'second_basic_stage'
     })
    print(test)
