from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Course
from .forms import CourseForm

# Create your views here.
def index(request, course_id):
    return render(request, "course/index.html", {
        "course" : Course.objects.get(pk = course_id)
    })

@login_required
def create_course(request):
    if request.user.role != 'instructor':
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = CourseForm(instructor=request.user, data=request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user 
            course.save()
            form.save_m2m()
            return redirect('course:index', course_id=course.id)
    else:
        form = CourseForm(instructor=request.user)

    return render(request, 'course/create_course.html', {
        'form': form,
    })