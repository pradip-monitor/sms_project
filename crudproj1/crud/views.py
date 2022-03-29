from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForm
from .models import Student
# Create your views here.

def index(request):
    return render(request,"crud/base.html")

def addandshow(request):
    if request.method=="POST":
        fm=StudentForm(request.POST,request.FILES)
        if fm.is_valid():
            pic=fm.cleaned_data["pic"]
            fname=fm.cleaned_data["first_name"]
            lname=fm.cleaned_data["last_name"]
            em=fm.cleaned_data["email"]
            pw=fm.cleaned_data["password"]
            stud=Student(pic=pic,first_name=fname,last_name=lname,email=em,password=pw)
            stud.save()
            fm=StudentForm()
    else:
        fm=StudentForm()
    stud=Student.objects.all()

    return render(request,"crud/addandshow.html",{'form':fm,'stud':stud})



def update_student(request,id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            fm=StudentForm()
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentForm(instance=pi)

    return render(request,"crud/update_student.html",{'form':fm})


def delete_student(request,id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")
