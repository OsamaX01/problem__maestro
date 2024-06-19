from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CodeSnippetForm

def create_snippet(request):
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            return render(request, "editor/result.html", {
                'code': code   
            })
        else:
            print(form.errors)
