from copy import deepcopy


class PrototypeMixin:
    """
    Клонирует зарегистрированный объект, для быстрого создания с небольшими
    правками атрибутов.
    """
    # прототип
    def clone(self):
        return deepcopy(self)
