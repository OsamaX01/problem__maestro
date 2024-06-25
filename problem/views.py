from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import json

from urllib.parse import urlencode

from .models import Problem, TestCase
from .forms import ProblemForm, TestCaseForm
from .functions import compute_test_answer

from editor.forms import CodeSnippetForm
from editor.functions import validate_solution

from openai_api.forms import PromptForm
from openai_api.api import request_problem

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
def create_problem_using_ai(request):
    if request.method == 'POST':
        problem_prompt_form = PromptForm(request.POST)
        if problem_prompt_form.is_valid():
            problem_prompt = problem_prompt_form.cleaned_data['prompt']
            problem = request_problem(problem_prompt)
            if problem['success'] == True:
                query_string = urlencode(problem)
                return redirect(f'/problem/create?{query_string}')
            else:
                return render(request, 'problem/create_problem_using_ai.html', {
                    'prompt_form': problem_prompt_form,
                    'message' : 'Please try again with a better prompt and make sure it is related to problem writing',
                })
    else:
        problem_prompt_form = PromptForm()

    return render(request, 'problem/create_problem_using_ai.html', {
        'prompt_form': problem_prompt_form,
    })

@login_required
def create_problem(request):
    initial_data = {
        'name': request.GET.get('title', ''),
        'statement': request.GET.get('statement', ''),
        'input_section': request.GET.get('input', ''),
        'output_section': request.GET.get('output', ''),
    }

    testcases = request.GET.getlist('testcases', [])
    
    if request.method == 'POST':
        problem_form = ProblemForm(request.POST)
        if problem_form.is_valid():
            problem = problem_form.save(commit=False)
            problem.instructor = request.user
            problem.save()
            if testcases == []:
                return redirect('problem:create_test_case', problem_id=problem.id)
            else:
                request.session['testcases'] = testcases
                return redirect('problem:approve_ai_testcases', problem_id=problem.id)
    else:
        problem_form = ProblemForm(initial=initial_data)
        editor_from = CodeSnippetForm()

    return render(request, 'problem/create_problem.html', {
        'problem_form': problem_form,
        'editor_form': editor_from,
    })

@login_required
def approve_ai_testcases(request, problem_id):
    problem = Problem.objects.get(pk=problem_id)
    testcases = request.session.get('testcases', [])
    testcases = eval(testcases[0])

    if request.method == 'POST':
        for i in range(len(testcases)):
            input_data = request.POST.get(f'input_{i}')
            is_visible = request.POST.get(f'is_visible_{i}') == 'on'
            if input_data != None: 
                test_case = TestCase()
                print(input_data)
                test_case.data = input_data
                test_case.problem = problem
                test_case.is_visable = is_visible
                test_case.answer = compute_test_answer(test_case)
                test_case.save()

        if 'finish' in request.POST:
            return redirect('problem:my_problems')
        else:
            return redirect('problem:create_test_case', problem_id=problem_id)

    return render(request, 'problem/approve_ai_testcases.html', {
        'problem': problem,
        'testcases': testcases
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