from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(VaccDetails)
admin.site.register(CovidHistory)
admin.site.register(Notifications)