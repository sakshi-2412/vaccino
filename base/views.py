from django.shortcuts import render
from .forms import *
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully created!')
            return redirect('settings:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    context = { 
        'user_form': user_form,
        'profile_form': profile_form, 
    }

    return render(request, 'register.html', context=context)


def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def notif(request):
    return render(request, 'notif.html')

def profile(request):
    return render(request, 'profile.html') 

def dashboard(request):
    p1labels=["Yes","No"]
    p1data=[100,20]

    p2labels=["Yes","No"]
    p2data=[70,50]

    p3labels=["Yes","No"]
    p3data=[50,70]

    p4labels=["Covishield","Covaxin","Sputnik"]
    p4data=[50,40,10]

    b1labels=["Year 1","Year 2","Year 3","Year 4","Year 5","M.Tech","PhD"]
    bar1_d1=[5,10,20,5,20,30,20]
    bar1_d2=[2,3,10,5,20,20,10]

    context = {
        'p1labels': p1labels,
        'p1data': p1data,

        'p2labels': p2labels,
        'p2data': p2data,

        'p3labels': p3labels,
        'p3data': p3data,

        'p4labels': p4labels,
        'p4data': p4data,

        'b1labels': b1labels,
        'bar1_d1': bar1_d1,
        'bar1_d2': bar1_d2,

    }
    return render(request, 'dashboard.html', context=context)    