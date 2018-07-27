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