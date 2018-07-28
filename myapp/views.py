from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def index(request):
    return render(request,'myapp/index.html')

def upfile(request):
    return render(request,'myapp/upfile.html')

def savefile(request):
    if request.method == 'POST':
        f = request.FILES['file']
        filePath = os.path.join(settings.MDEIA_ROOT,f.name)
        with open(filePath,'wb') as fp:
            for info in f.chunks():
                fp.write(info)
        return HttpResponse('上传成功')

    else:
        return HttpResponse('上传失败')

#分页方法
from .models import Students
from django.core.paginator import Paginator
def studentpage(request,pageid):
    #所有学生列表
    alllist = Students.objects.all()
    pageinator = Paginator(alllist,6)
    page = pageinator.page(pageid)

    return render(request,'myapp/studentpage.html',{'students':page})


def ajaxstudents(request):
    return render(request,'myapp/ajaxstudents.html')

from django.http import JsonResponse
def studentsinfo(request):
    stus = Students.objects.all()
    list = []
    for stu in stus:
        list.append([stu.sname,stu.sage])
    return JsonResponse({'data':list})

def edit(request):
    return render(request,'myapp/edit.html')

import time
def celery(request):

    return render(request,'myapp/celery.html')