from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label ='Title', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    content = forms.CharField(required = False, widget = forms.Textarea(attrs  = {"placeholder": "Your description"}))
    active = forms.BooleanField()

    
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
            ]
