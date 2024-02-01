from django import forms
from myapp.models import Book


class bookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields= "__all__"