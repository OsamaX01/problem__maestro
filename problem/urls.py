from django.urls import path

from . import views

app_name = 'problem'
urlpatterns = [
    path("<int:problem_id>", views.index, name='index'),
    path("create", views.create_problem, name='create'),
    path("create_test_case/<int:problem_id>", views.create_test_case, name='create_test_case'),
]