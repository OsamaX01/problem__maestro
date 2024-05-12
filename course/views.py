from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Course
from .forms import CourseForm
from problem.models import Problem

# Create your views here.
def index(request, course_id):
    course = Course.objects.get(pk = course_id)
    unused_problems = Problem.objects.exclude(courses=course_id).filter(instructor_id=request.user.id)

    return render(request, "course/index.html", {
        "course" : course, 
        "unused_problems" : unused_problems,
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

def add_problem_to_course(request, course_id):
    if request.method == 'POST':
        problem_id = request.POST.get('problem_id')
        problem = Problem.objects.get(id = problem_id)
        course = Course.objects.get(id = course_id)
        course.problems.add(problem)
        course.save()
        return redirect('course:index', course_id=course_id)

def remove_problem_to_course(request, course_id):
    if request.method == 'POST':
        problem_id = request.POST.get('problem_id')
        problem = Problem.objects.get(id = problem_id)
        course = Course.objects.get(id = course_id)
        course.problems.remove(problem)
        course.save()
        return redirect('course:index', course_id=course_id)