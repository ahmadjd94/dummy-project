from django.contrib import admin

# Register your models here.
from .models import CovidActivity, Employee, CovidActivityHistory

admin.site.register(Employee)
admin.site.register(CovidActivity)
admin.site.register(CovidActivityHistory)
