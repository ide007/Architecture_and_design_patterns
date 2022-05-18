from framework.wsgi import Framework
from user_urls import user_url


app = Framework(user_url)
