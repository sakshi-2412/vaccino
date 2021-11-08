from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('notif/', views.notif, name='notif'),
   path('profile/', views.profile, name='profile'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('register/', views.register, name='register'),
   path('login/', views.login_, name='login'),
   path('profile_form/', views.profile_form, name='profile_form'),
]