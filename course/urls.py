from django.urls import path

from . import views

app_name = 'course'
urlpatterns = [
    path("<int:course_id>", views.index, name='index'),
    path("create", views.create_course, name='create'),
    path("add_problem_to_course/<int:course_id>", views.add_problem_to_course, name='add_problem_to_course'),
    path("remove_problem_to_course/<int:course_id>", views.remove_problem_to_course, name='remove_problem_to_course'),
]