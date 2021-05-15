from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 

# Create your views here.
def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service.html')

def faculty(request):
    return render(request,'faculty.html')

def college(request):
    return render(request,'college.html')

def admission(request):
    return render(request, 'admission.html')

def home(request):
    return render(request, 'index.html')
