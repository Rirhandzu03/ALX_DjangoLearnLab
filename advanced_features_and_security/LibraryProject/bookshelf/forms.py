from django import forms

class ExampleForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search for books')