from django.shortcuts import redirect, render
from .models import Students
from .forms import StudentForm
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    context = { 'students' : Students.objects.all() }
    return render(request,'index.html',context)

def student(request):
     if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():    
            fs = FileSystemStorage()
            uploadedfile = request.FILES['Image']
            file = fs.save(uploadedfile.name, uploadedfile)

            std = Students()
            std.ID = Students.objects.last().ID + 1
            std.Name = form.cleaned_data['Name']
            std.ImagePath = fs.url(file)
            std.save()
            
            return redirect("/")

     else:
        form = StudentForm()
        return render(request,'form.html', {'form': form})

def contact(request):
     return render(request,'contact.html')