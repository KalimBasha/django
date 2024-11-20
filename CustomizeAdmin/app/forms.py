from django import forms 
from app.models import * 

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