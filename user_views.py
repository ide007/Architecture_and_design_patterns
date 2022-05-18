from jinja2 import Template
from framework.views import View


class Pages(View):

    def get(self, request):
        return 'GET SUCCESS'

    def post(self, request):
        return 'POST SUCCESS'
