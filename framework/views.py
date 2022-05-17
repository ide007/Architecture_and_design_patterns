from templates import render_template
from test_data import pages


def home_page(request):
    print(request)
    return '200 OK', render_template('index.html', pages=pages)


def first_page(request):
    print(request)
    return '200 OK', render_template('index.html', pages=pages[0])


def next_page(request):
    print(request)
    return '200 OK', render_template('next_page.html', pages=pages[1])


def special_page(request):
    print(request)
    return '200 OK', render_template('next_page.html', pages=pages[2])


def about(request):
    return '200 OK', "About_us"
