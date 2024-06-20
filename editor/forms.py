from django import forms

class CodeSnippetForm(forms.Form):
    code = forms.CharField()
    problem_id = forms.IntegerField()