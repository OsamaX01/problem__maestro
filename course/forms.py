from django import forms

from .models import Course
from problem.models import Problem 

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'students', 'problems']

    def __init__(self, instructor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['problems'].queryset = Problem.objects.filter(instructor=instructor)
