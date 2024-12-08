from django import forms

class TagWidget(forms.TextInput):
    """
    Custom widget for handling tag input.
    """
    def __init__(self, attrs=None):
        default_attrs = {'placeholder': 'Enter comma-separated tags', 'class': 'tag-input'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)
        
    def format_value(self, value):
        # You can add custom formatting logic for the value if needed
        return super().format_value(value)
