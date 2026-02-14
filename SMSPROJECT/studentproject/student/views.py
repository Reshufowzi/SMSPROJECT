from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    x = {
        'NAME': "ANU",
        'AGE': 32,
        'PLACE': 'CHENNAI'
    }
    return render(request,'home.html',x)
def about(request):
    numbers = {
        'number1': -10,
    }
    return render(request,'about.html',numbers)

def department(request):
    num = 11
    if num % 2 == 0:
        res = f"{num} is Even Number"
    else:
        res = f"{num} is Odd Number"
    return render(request,'department.html',{'output':res})

def contact(request):
    numbers = {
        'number1' : [1,2,3,4,5,6,7,8,9,10],
    }
    return render(request,'contact.html',numbers)