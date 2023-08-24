from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'

# modelform 은 model 에 항목을 추가했을 때 자동으로 html을 만들어줌.