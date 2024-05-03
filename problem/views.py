from django.shortcuts import render

from .models import Problem

# Create your views here.
def index(request, problem_id):
    problem = Problem.objects.get(pk = problem_id)
    samples = problem.testcases.filter(is_visable=True)

    return render(request, "problem/index.html", {
        "problem" : problem,
        "samples" : samples, 
    })
