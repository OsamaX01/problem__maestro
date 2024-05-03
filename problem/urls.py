from django.urls import path

from . import views

app_name = 'problem'
urlpatterns = [
    path("<int:problem_id>", views.index, name='index'),
]