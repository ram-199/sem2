from django.shortcuts import render
from django.http.response import HttpResponse
from openpyxl import Workbook,load_workbook
import os

# Create your views here.
def result(branch):
    wb=load_workbook(os.path.dirname(__file__)+"/E1S2.xlsx")
    return { "rows":wb[branch].rows }

def home(request):
    return HttpResponse("<h1>add / + branch to url </h1>")

def cse(request):
    return render(request,"index.html",result("CSE"))

def ece(request):
    return render(request,"index.html",result("ECE"))

def mech(request):
    return render(request,"index.html",result("MECH"))

def civil(request):
    return render(request,"index.html",result("CIVIL"))

def mme(request):
    return render(request,"index.html",result("MME"))

def chem(request):
    return render(request,"index.html",result("CHEM"))

