from django.db import models


class Student_registration(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    father_name = models.TextField()
    mother_name = models.TextField()
    department = models.TextField()
    phone_number = models.CharField(max_length=15)


class Student_application(models.Model):
    name = models.TextField()
    email = models.TextField()
    ssc_marks = models.IntegerField()
    bie_marks = models.IntegerField()
