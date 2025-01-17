from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        # fields='__all__'
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=profile
        # fields='__all__'
        fields=['Address','profile_pic']