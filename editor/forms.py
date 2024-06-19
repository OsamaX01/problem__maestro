from django import forms

class CodeSnippetForm(forms.Form):
    code = forms.CharField()