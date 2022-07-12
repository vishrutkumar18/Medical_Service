from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Contact, Certi


def home(request):
    if request.method == "POST":
        first = request.POST.get('name')
        last = request.POST.get('last')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        obj = Contact(first=first, last=last, email=email, feedback=feedback)
        obj.save()
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def reports(request):
    return render(request, 'reports.html')


def contact(request):
    if request.method == "POST":
        first = request.POST.get('name')
        last = request.POST.get('last')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        # print(first)
        obj = Contact(first=first, last=last, email=email, feedback=feedback)
        obj.save()
    return render(request, 'contact.html')


def service(request):
    return render(request, "services.html")


def kmedic(request):
    return render(request, 'kmedic.html')


def fmedic(request):
    return render(request, 'fmedic.html')


def petient(request):
    return render(request, 'petient.html')


def corporate(request):
    return render(request, 'corporate.html')


def certi(request):
    if request.method == "POST":
        fullname = request.POST.get('certi_name')
        Email = request.POST.get('certi_email')
        # Dob = request.POST.get('datepicker')
        # Gender = request.POST.get('name')
        Number_of_Passport = request.POST.get('number_of_passport')
        Contact_number = request.POST.get('certi_phone')
        # Number_of_Passport = request.POST.get('number_of_passport')
        Name_of_medical_examiner = request.POST.get('certi_examiner')
        Approvel_number = request.POST.get('certi_approval')
        Job_title = request.POST.get('certi_is')
        obj = Certi(fullname=fullname, Email=Email, Number_of_Passport=Number_of_Passport,
                    Contact_number=Contact_number,
                    Name_of_medical_examiner=Name_of_medical_examiner, Approvel_number=Approvel_number,
                    Job_title=Job_title,
                    # Approvel_number=Approvel_number
                    )
        obj.save()
    return render(request, 'certi.html')


def showdata(request):
    displaynames = User.objects.all()
    return render(request, 'showdata.html', {"Certi": displaynames})
