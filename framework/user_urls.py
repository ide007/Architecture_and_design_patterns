from user_views import *

user_url = {
    '/': course_list,
    '/home': course_list,
    '/course_list': course_list,
    '/create_course': create_course,
    '/about': about_view,
    '/category_list': CategoryListView(),
    '/create_category': CategoryCreateView(),
    '/student_list': StudentListView(),
    '/create_student': StudentCreateView(),
    '/add_student': AddStudentByCourseCreateView(),
    '/contacts': contact_view,
}
