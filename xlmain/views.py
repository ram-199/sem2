from django.shortcuts import render
from django.http.response import HttpResponse
from .models import CSE,ECE,CHEM,CIVIL,MECH,MME


def result(name,b):
    return {
    "headings" :name.keys(),
    "rows" : [item.values() for item in name.objects.all()],
    "branch":b
    }
# Create your views here.
def home(request):
    items =  CIVIL.objects.all()
    print(dir(items[0]))
    return render(request,"home.html")
def cse(request):
    return render(request,"results.html",result(CSE,"cse"))
def ece(request):
    return render(request,"results.html",result(ECE,"ece"))

def mech(request):
    return render(request,"results.html",result(MECH,'mech'))

def civil(request):
    return render(request,"results.html",result(CIVIL,'civil'))

def mme(request):
    return render(request,"results.html",result(MME,'mme'))

def chem(request):
    return render(request,"results.html",result(CHEM,'chem'))

