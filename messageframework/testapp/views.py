from django.shortcuts import render
from .forms import StudentRegistation
from django.contrib import messages

# Create your views here.


def regi(request):
    if request.method == 'POST':
        fm = StudentRegistation(request.POST)
        if fm.is_valid():
            fm.save()

            messages.add_message(request,messages.SUCCESS,'Your Account Has Been Created !!!')
            messages.info(request,'Now You Can Login')
    else:
        fm = StudentRegistation()
    return render(request,'testapp/index.html',{'form':fm})
