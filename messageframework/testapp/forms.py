from django import forms
from testapp.models import User

class StudentRegistation(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email', 'password']

