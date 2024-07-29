# app/urls.py

from django import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('signup/employee/', views.employee_signup, name='employee_signup'),
    path('signup/employer/', views.employer_signup, name='employer_signup'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/employee/<int:user_id>/', views.employee_profile, name='employee_profile'),
    path('profile/employer/<int:user_id>/', views.employer_profile, name='employer_profile'),
    path('post_job/', views.post_job, name='post_job'),
    path('job_page/', views.job_page, name='job_page'),
]