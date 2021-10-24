from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def notif(request):
    return render(request, 'notif.html')