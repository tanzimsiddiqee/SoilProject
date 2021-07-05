from django.shortcuts import render, redirect
from .models import Students

# Create your views here.

def index(request):
    context = { 'students' : Students.objects.all() }
    return render(request,'index.html',context)

def about(request):
   return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')