from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactUs
from .models import Careers
from django.core.files.storage import FileSystemStorage

# Create your views here.


def index(request):
    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def test(request):

    pass

    #Queries= Careers.objects.all()

    #return render(request,'test.html', {'Queries':Queries})

def careers(request):
    if request.method == "POST":
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        file_upload = request.FILES['resumeUpload']
        fs = FileSystemStorage()
        fs.save(file_upload.name, file_upload)
        print(file_upload.name)
        
        

        c= Careers(firstname=firstname, lastname=lastname,email=email,phone=phone,street=street,city=city,state=state,zip=zip)
        c.save() 

        return render(request,'careers.html')
    else:
        return render(request,'careers.html')


    

def industry(request):
    return render(request,'industry.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        c = ContactUs(name=name,email=email,subject=subject,message=message)
        c.save()

    else:

        return render(request, 'contact.html')


        
    return render(request,'contact.html')

def privacy(request):
    return render(request,'privacy.html')

def services(request):
    return render(request,'services.html')