from django.db import models

# Create your models here.

# 클래스의 이름은 항상 대문자로 시작 

class Article(models.Model):
     # C, T, D 저것들 다 클래스 
    title = models.CharField(max_length = 50)
    content = models.uTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

