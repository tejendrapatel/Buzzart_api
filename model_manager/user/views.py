from django.shortcuts import render
from user.models import *

def HOME(request):
    use = users.detail.all()
    d = {"use":use}
    return render (request,'home.html',d)

def USERRAN(request):
    g = Detail.objects.all()
    ag = Detail.deta.get_Detail_age_range(1,20)
    d = {"ag":ag,"g":g}
    return render (request,'home2.html',d)
