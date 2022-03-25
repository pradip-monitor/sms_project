from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model =Student
        fields=['pic','first_name','last_name','email','password']
        widgets={'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'pic':forms.ClearableFileInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),}


