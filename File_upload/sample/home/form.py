from django import forms

from .models import employee


class form2(forms.ModelForm):
    class Meta:
        model = employee
        fields = "__all__"
