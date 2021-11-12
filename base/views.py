from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return render(request, 'index.html')

def notif(request):
    context = {
        'user_notifs': None,
    }
    user_notifs = Notifications.objects.all().order_by('-date_notif')
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

    date1yes = VaccDetails.objects.filter(date1__isnull = False ).count()
    date1no = VaccDetails.objects.filter(date1__isnull = True ).count()
    p1labels=["Yes","No"]
    p1data=[date1yes,date1no]

    date2yes = VaccDetails.objects.filter(date2__isnull = False ).count()
    date2no = VaccDetails.objects.filter(date2__isnull = True ).count()
    p2labels=["Yes","No"]
    p2data=[date2yes,date2no]

    infectedyes = CovidHistory.objects.filter(date__isnull = False ).count()
    infectedno = CovidHistory.objects.filter(date__isnull = True ).count()
    p3labels=["Yes","No"]
    p3data=[infectedyes,infectedno]

    covishield = VaccDetails.objects.filter(vaccine_name = 'COVISHIELD' ).count()
    covaxin = VaccDetails.objects.filter(vaccine_name = 'COVAXIN' ).count()
    sputnik = VaccDetails.objects.filter(vaccine_name = 'SPUTNIK' ).count()
    p4labels=["Covishield","Covaxin","Sputnik"]
    p4data=[ covishield, covaxin, sputnik ]

    year11 = VaccDetails.objects.filter(student__profile__year = 1, date1__isnull = False ).count()
    year21 = VaccDetails.objects.filter(student__profile__year = 2, date1__isnull = False ).count()
    year31 = VaccDetails.objects.filter(student__profile__year = 3, date1__isnull = False ).count()
    year41 = VaccDetails.objects.filter(student__profile__year = 4, date1__isnull = False ).count()
    year51 = VaccDetails.objects.filter(student__profile__year = 5, date1__isnull = False ).count()
    mtech1 = VaccDetails.objects.filter(student__profile__program = 'M.TECH', date1__isnull = False ).count()
    phd1 = VaccDetails.objects.filter(student__profile__program = 'PhD', date1__isnull = False ).count()

    year12 = VaccDetails.objects.filter(student__profile__year = 1, date2__isnull = False).count()
    year22 = VaccDetails.objects.filter(student__profile__year = 2, date2__isnull = False ).count()
    year32 = VaccDetails.objects.filter(student__profile__year = 3, date2__isnull = False ).count()
    year42 = VaccDetails.objects.filter(student__profile__year = 4, date2__isnull = False ).count()
    year52 = VaccDetails.objects.filter(student__profile__year = 5, date2__isnull = False ).count()
    mtech2 = VaccDetails.objects.filter(student__profile__program = 'M.TECH', date2__isnull = False ).count()
    phd2 = VaccDetails.objects.filter(student__profile__program = 'PhD', date2__isnull = False ).count()
    b1labels=["Year 1","Year 2","Year 3","Year 4","Year 5","M.Tech","PhD"]
    bar1_d1=[year11,year21,year31,year41,year51,mtech1,phd1]
    bar1_d2=[year12,year22,year32,year42,year52,mtech2,phd2]

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

@login_required(login_url='login')
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