from copy import deepcopy


class PrototypeMixin:
    # прототип
    def clone(self):
        return deepcopy(self)
