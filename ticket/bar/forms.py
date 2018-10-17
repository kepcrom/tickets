from django import forms
from bar.models import Bar

class BarForm(forms.ModelForm):
    class Meta():
        model = Bar
        fields = ('Number','Summary')
        #fields = ('Number','Summary','Creator')
