# import 잊지말기
from django.urls import path
from . import views 
 
# 가끔 서버 킨 상태에서 새로 만들면 반영이 안될 수도 있으니 
# module 에러가 나면 다시 서버 껏다 켜보기도 하기


app_name = 'articles'

urlpatterns=[
    path('',views.index, name='index'),
    path('<int:id>/',views.detail, name='detail'),

    path('create/', views.create, name='create'),
]
