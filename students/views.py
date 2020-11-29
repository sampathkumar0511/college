from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Student_registration, Student_application


def first_page(request):
    return render(request, 'students/base.html')


def student_create(request):
    if request.method == 'POST':
        Student_registration.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            father_name=request.POST["father_name"],
            mother_name=request.POST["mother_name"],
            department=request.POST["department"],
            phone_number=request.POST["phone_number"]
        )
    return render(request, 'students/student_reg.html')


def student_join(request):
    if request.method == 'POST':
        Student_application.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            ssc_marks=request.POST["ssc_marks"],
            bie_marks=request.POST["bie_marks"]
        )
    return render(request, 'students/student_app.html')


def student_list(request):
    all_students = Student_application.objects.all()
    context = {
        'all_students': all_students
    }
    return render(request, 'students/student_list.html', context)
