from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
def register(request):
    if request.user.is_authenticated:
	    return redirect('index')
    else:    
        user_form = UserForm()

        if request.method == 'POST':
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                user = user_form.save()
                if(user):
                    login(request, user)

                Notifications.objects.create(student2=request.user,
                                        message="Your account was registered",
                                        option="success",
                                        date_notif=datetime.datetime.now())
                Notifications.objects.create(student2=request.user,
                                        message="Complete your profile and vaccination details from the profile page",
                                        option="info",
                                        date_notif=datetime.datetime.now())

                return redirect('notif')
            else:
                messages.error(request, 'Please correct the errors.')

        return render(request, 'register.html', { 'user_form': user_form })

def login_(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username/password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logout_(request):
	logout(request)
	return redirect('login')

def index(request):
    return render(request, 'index.html')

def notif(request):
    context = {
        'user_notifs': None,
    }
    user_notifs = Notifications.objects.all()
    context['user_notifs'] = user_notifs
    return render(request, 'notif.html',context = context)

@login_required(login_url='login')
def profile(request):
    context = {
        'user_vacc': None,
        'user_covid': None,
    }
    user_vacc = VaccDetails.objects.filter(student=request.user)[0]
    user_covid = CovidHistory.objects.filter(student1=request.user)[0]
    context['user_vacc'] = user_vacc
    context['user_covid'] = user_covid
    
    return render(request, 'profile.html', context = context) 

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

def profile_form(request):
    profile_form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()

            Notifications.objects.create(student2=request.user,
                                        message="Profile details updated",
                                        option="success",
                                        date_notif=datetime.datetime.now())
            Notifications.objects.create(student2=request.user,
                                        message=
                                        "Complete your vaccination details (if you have not) from the profile page",
                                        option="info",
                                        date_notif=datetime.datetime.now())

            return redirect('notif')
        else:
            messages.error(request, 'Please correct the errors.')

    return render(request, 'profile_form.html', { 'profile_form': profile_form })
    
@login_required(login_url='login')
def vacc_form(request):
    existing_form = VaccDetails.objects.filter(student=request.user)[0]
    vacc_form = VaccForm(instance=existing_form)

    if request.method == 'POST':
        vacc_form = VaccForm(request.POST, request.FILES, instance=existing_form)
        if vacc_form.is_valid():
            vacc_form.save()

            Notifications.objects.create(student2=request.user,
                                        message="Vaccination details updated",
                                        option="success",
                                        date_notif=datetime.datetime.now())
            Notifications.objects.create(student2=request.user,
                                        message=
                                        "Wait for the authority to verify your vaccination certificate",
                                        option="info",
                                        date_notif=datetime.datetime.now())
            Notifications.objects.create(student2=request.user,
                                        message=
                                        "Complete your covid history details (if you have not yet) from the profile page",
                                        option="info",
                                        date_notif=datetime.datetime.now())

            return redirect('notif')
        else:
            messages.error(request, 'Please correct the errors.')

    return render(request, 'vacc_form.html', { 'vacc_form': vacc_form })

@login_required(login_url='login')
def history_form(request):
    existing_form = CovidHistory.objects.filter(student1=request.user)[0]
    history_form = HistoryForm(instance=existing_form)

    if request.method == 'POST':
        history_form = HistoryForm(request.POST, instance=existing_form)
        if history_form.is_valid():
            history_form.save()

            Notifications.objects.create(student2=request.user,
                                        message="Covid History form updated",
                                        option="success",
                                        date_notif=datetime.datetime.now())
                                        
            return redirect('notif')
        else:
            messages.error(request, 'Please correct the errors.')

    return render(request, 'history_form.html', { 'history_form': history_form })