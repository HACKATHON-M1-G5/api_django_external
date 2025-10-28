from django import forms
from app.option.models import Option

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['name', 'value']
