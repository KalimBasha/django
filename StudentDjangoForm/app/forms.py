from django import forms
from app.models import *
from django.core.validators import *

class SchoolForm(forms.Form):
    SchoolID=forms.CharField()
    SchoolName=forms.CharField()


def validate_for_char(data):     # this is a way to validate it will validate only one input at a time.
    if not data[0].isalpha():
        raise forms.ValidationError('Error')

def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('error')
    
class StudentForm(forms.Form):
    SchoolId=forms.CharField(min_length=3,validators=[MinLengthValidator(3)])
    Stuid=forms.CharField()
    Stuname=forms.CharField(validators=[validate_for_char,validate_for_len,MaxLengthValidator(2)])
    # location=forms.CharField()
    # Mobile_No=forms.IntegerField()
    Email=forms.EmailField(validators=[validate_for_char,EmailValidator])
    remail=forms.EmailField()
    BotCatcher=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean(self):
        s=self.cleaned_data['Email']
        r=self.cleaned_data['remail']
        if s!=r:
            raise forms.ValidationError('Error')

    def clean_BotCatcher(self):
        bc=self.cleaned_data['BotCatcher']
        if len(bc)>0:
            raise forms.ValidationError('Not Given By Human')