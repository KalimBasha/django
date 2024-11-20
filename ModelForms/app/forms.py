from django import forms 
from app.models import * 
from django.core.validators import *

class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = "__all__"

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url','topic_name']
        exclude=['url']
        help_texts={'name':'Only Alphabets'}
        labels={'topic_name':'TN'}
        widgets={'name':forms.PasswordInput}

    mobile=forms.CharField(max_length=10,min_length=10,validators=[RegexValidator('[6-9]/d{9}')])      #mobile no must be charfield with validators and like this we can add extra input field
    remail=forms.EmailField(widget=forms.HiddenInput)
    Botcatcher=forms.IntegerField(max_value=10,widget=forms.HiddenInput,required=False)

    def clean(self):
        se=self.cleaned_data['email']
        re=self.cleaned_data['remail']
        if se != re:
            raise forms.ValidationError('Emails Not Matching!!!')
        
    def clean_Botcatcher(self):
        bot=self.cleaned_data['Botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('Hacker Alert!!!')