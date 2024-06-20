from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Problem
from .forms import ProblemForm, TestCaseForm
from .functions import compute_test_answer

from editor.forms import CodeSnippetForm
from editor.functions import validate_solution

# Create your views here.
def index(request, problem_id):
    problem = Problem.objects.get(pk = problem_id)
    samples = problem.testcases.filter(is_visable=True)
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            problem_id = form.cleaned_data['problem_id']
            problem = Problem.objects.get(id = problem_id)
            validation = validate_solution(problem, code)  
            return  render(request, "problem/index.html", {
                "problem" : problem,
                "samples" : samples,
                "result" : validation[0],
                "description" : validation[1]
            })
        else:
            print(form.errors)
        

    return render(request, "problem/index.html", {
        "problem" : problem,
        "samples" : samples,
    })

@login_required
def create_problem(request):
    if request.method == 'POST':
        problem_form = ProblemForm(request.POST)
        if problem_form.is_valid():
            problem = problem_form.save(commit=False)
            problem.instructor = request.user
            problem.save()
            return redirect('problem:create_test_case', problem_id=problem.id)
    else:
        problem_form = ProblemForm()
        editor_from = CodeSnippetForm()

    return render(request, 'problem/create_problem.html', {
        'problem_form': problem_form,
        'editor_form': editor_from,
    })

@login_required
def create_test_case(request, problem_id):
    problem = Problem.objects.get(pk=problem_id)
    if request.method == 'POST':
        test_case_form = TestCaseForm(request.POST)
        if test_case_form.is_valid():
            test_case = test_case_form.save(commit=False)
            test_case.problem = problem
            test_case.answer = compute_test_answer(test_case)
            test_case.save()
            
            if 'finish' in request.POST:
                return redirect('problem:my_problems')
            else:
                return redirect('problem:create_test_case', problem_id=problem_id)
    else:
        test_case_form = TestCaseForm()

    return render(request, 'problem/create_test_case.html', {
        'test_case_form': test_case_form
    })

def my_problems(request):
    if request.user.role == 'student':
        return redirect('dashboard:index')

    problems = Problem.objects.filter(instructor = request.user.id)
    return render(request, 'problem/my_problems.html', {
        'problems': problems
    })