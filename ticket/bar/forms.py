from django import forms
from bar.models import Bar

class BarForm(forms.ModelForm):
    Creator = forms.IntegerField(required=False,widget=forms.HiddenInput())
    class Meta():
        model = Bar
        fields = ('Number','Summary','Creator')
