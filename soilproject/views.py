from django.shortcuts import redirect, render
from .models import Soils
from .forms import SoildForm
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    context = { 'soils' : Soils.objects.all() }
    return render(request,'index.html',context)

def add(request):
     if request.method == 'POST':
        form = SoildForm(request.POST, request.FILES)
        if form.is_valid():    
            fs = FileSystemStorage()
            uploadedfile = request.FILES['Image']
            file = fs.save(uploadedfile.name, uploadedfile)

            soid = Soils()
            soid.Id = Soils.objects.last().Id + 1
            soid.Sample = form.cleaned_data['Sample']
            soid.Sand = form.cleaned_data['Sand']
            soid.Silt = form.cleaned_data['Silt']
            soid.Clay = form.cleaned_data['Clay']
            soid.Type = form.cleaned_data['Type']
            soid.ImagePath = fs.url(file)
            soid.save()
            
            return redirect("/")

     else:
        form = SoildForm()
        return render(request,'form.html', {'form': form})

def contact(request):
     return render(request,'contact.html')