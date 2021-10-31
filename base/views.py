from django.shortcuts import render

# Create your views here.
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

    b1labels=["Year 1","Year 2","Year 3"]
    bar1_d1=[30,20,50]
    bar1_d2=[10,20,40]

    context = {
        'p1labels': p1labels,
        'p1data': p1data,

        'p2labels': p2labels,
        'p2data': p2data,

        'p3labels': p3labels,
        'p3data': p3data,

        'p4labels': p4labels,
        'p4data': p4data,

        'b1labels': p4labels,
        'bar1_d1': bar1_d1,
        'bar1_d2': bar1_d2,

    }
    return render(request, 'dashboard.html', context=context)    