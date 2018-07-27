from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.index,name='index'),
    path('upfile/',views.upfile),
    path('savefile/',views.savefile),
]