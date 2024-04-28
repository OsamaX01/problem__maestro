from django.shortcuts import render
from django.db.models import Q

from course.models import Course

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "dashboard/guest.html")
    
    student_courses = Course.objects.filter(students=request.user)
    instructor_courses = Course.objects.filter(instructor_id=request.user)
    return render(request, "dashboard/user_dashboard.html", {
        "courses" : (student_courses | instructor_courses).distinct()
    })