from django.urls import path
from . import views

app_name = 'editor'
urlpatterns = [
    path('', views.create_snippet, name='create_snippet'),
]
