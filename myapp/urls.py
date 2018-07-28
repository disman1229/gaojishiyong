from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.index,name='index'),
    path('upfile/',views.upfile),
    path('savefile/',views.savefile),
    path('studentpage/<int:pageid>/',views.studentpage),
    path('ajaxstudents/',views.ajaxstudents),
    path('studentsinfo/',views.studentsinfo),
    path('edit/',views.edit),
    path('celery/',views.celery),
]