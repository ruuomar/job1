from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Applicant

# Create your views here.
def form(request):
    if request.method =="POST":
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        Address = request.POST['address']
        Gender = request.POST['gender']
        Meritalstatus = request.POST['meritalstatus']
        Phone = request.POST['phonenumber']

        new_applicant = Applicant(fname=Fname, lname=Lname, address=Address, gender=Gender, meritalstatus=Meritalstatus, phonenumber=Phone)
        new_applicant.save()
    return render(request, 'form.html')

def applicants(request):
    appls = Applicant.objects.all()
    return render(request, 'applicant.html', {'appls':appls})

