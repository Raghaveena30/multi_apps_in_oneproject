from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return render(request,'msd.html')
def ajay(request):
    return HttpResponse('<h1> allrounder </h1>')
