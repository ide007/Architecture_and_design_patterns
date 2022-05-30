from models import TrainingSite
from wsgi.wsgi import Framework
from wsgi.response import rendering
from user_urls import user_url as urls


def controller(request):
    request['secret'] = 'secret'


front_controller = [controller]

app = Framework(urls, front_controller)
site = TrainingSite()


@app.add_route('/copy_course/')
def copy_course(request):
    request_params = request['request_params']
    print(request_params)
    name = request_params['name']
    old_course = site.get_course(name)
    if old_course:
        new_course_name = f'copy_{name}'
        new_course = old_course.clone()
        new_course.name = new_course_name

        site.courses.append(new_course)

    return '200 OK', rendering('index.html', objects_list=site.courses)


@app.add_route('/category_list')
def category_list(request):
    return '200 OK', rendering('category_list.html',
                               objects_list=site.categories)
