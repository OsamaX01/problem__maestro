from django.shortcuts import render

from .models import Course

# Create your views here.
def index(request, course_id):
    return render(request, "course/index.html", {
        "course" : Course.objects.get(pk = course_id)
    })