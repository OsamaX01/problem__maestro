from django import forms

from problem.models import Problem, TestCase

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['name', 'statement', 'input_section', 'output_section', 'correct_answer']


class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['number', 'data', 'is_visable']