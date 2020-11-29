from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('student_create/', views.student_create, name='student_create'),
    path('student_join/', views.student_join, name='student_join'),
    path('student_list/', views.student_list, name='student_list'),
]
