from django.urls import path

from . import views

app_name = 'problem'
urlpatterns = [
    path("<int:problem_id>", views.index, name='index'),
    path("create", views.create_problem, name='create'),
    path("create/ai", views.create_problem_using_ai, name='create_suing_ai'),
    path("create_test_case/<int:problem_id>", views.create_test_case, name='create_test_case'),
    path("my_problems", views.my_problems, name='my_problems'),
    path("approve_ai_testcases/<int:problem_id>", views.approve_ai_testcases, name='approve_ai_testcases'),
]