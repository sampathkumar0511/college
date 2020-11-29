from django.contrib import admin
from .models import Student_registration, Student_application

# Register your models here.

admin.site.register(Student_application)
admin.site.register(Student_registration)
