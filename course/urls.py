from django.urls import path

from . import views

app_name = 'course'
urlpatterns = [
    path("<int:course_id>", views.index, name='index'),
    path("create", views.create_course, name='create'),
]