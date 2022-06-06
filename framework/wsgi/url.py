from dataclasses import dataclass

from typing import Type

from framework.wsgi.views import View


@dataclass
class Url:
    url: str
    view: Type[View]
