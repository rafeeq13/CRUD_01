from django.shortcuts import render,HttpResponseRedirect
from .forms import User
from .models import Student
# Create your views here.
def detail(request):
    if request.method=="POST":
        fm=User(request.POST)
        if fm.is_valid():
           nm=fm.cleaned_data['name']
           em=fm.cleaned_data['email']
           pwd=fm.cleaned_data['password']
           reg=Student(name=nm,email=em,password=pwd)
           reg.save()
           fm=User()

    else:
        fm=User()
    stu=Student.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'st':stu})

def delete_data(request,id):
    if request.method=="POST":
        st=Student.objects.get(pk=id)
        st.delete()
    return HttpResponseRedirect('/')


def updatedata(request,id):
    if request.method=="POST":
        st=Student.objects.get(pk=id)
        fm=User(request.POST,instance=st)
        if fm.is_valid():
            fm.save()
    else:
        st=Student.objects.get(pk=id)
        fm=User(request.POST,instance=st)        
    return render(request,'enroll/update.html',{'id':fm})