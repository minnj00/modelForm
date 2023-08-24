from django.shortcuts import render
from .models import Article

# Create your views here.

# 인덱스가 하는 일은 게시물들을 보여주는 것
def index(request):
    articles = Article.objects.all()

    context ={
        'articles': articles
    }
    return render(request, 'index.html', context )

def detail(request, id):
    article = Article.objects.get(id=id)
    context ={
        'article': article,

    }
    return render(request, 'detail.html', context)