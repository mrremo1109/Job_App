from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EmployeeSignUpForm, EmployerSignUpForm, JobPostForm, CustomLoginForm
from .models import Employee, Employer, Job
from django.contrib.auth import views as auth_views

def welcome_page(request):
    return render(request, 'app/welcome_page.html')

def employee_signup(request):
    if request.method == 'POST':
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have signed up successfully. Please log in.')
            return redirect('employee_profile', user_id=user.id)
    else:
        form = EmployeeSignUpForm()
    return render(request, 'app/employee_signup.html', {'form': form})

def employer_signup(request):
    if request.method == 'POST':
        form = EmployerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have signed up successfully. Please log in.')
            return redirect('employer_profile', user_id=user.id)
    else:
        form = EmployerSignUpForm()
    return render(request, 'app/employer_signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if hasattr(user, 'employee'):
                    return redirect('employee_profile', user_id=user.id)
                elif hasattr(user, 'employer'):
                    return redirect('employer_profile', user_id=user.id)
    else:
        form = CustomLoginForm()
    
    return render(request, 'app/login.html', {'form': form})

@login_required
def employee_profile(request, user_id):
    employee = get_object_or_404(Employee, pk=user_id)
    return render(request, 'app/employee_profile.html', {'employee': employee})

@login_required
def employer_profile(request, user_id):
    employer = get_object_or_404(Employer, pk=user_id)
    return render(request, 'app/employer_profile.html', {'employer': employer})

@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user.employer
            job.save()
            return redirect('employer_profile', user_id=request.user.employer.id)
    else:
        form = JobPostForm()
    return render(request, 'app/post_job.html', {'form': form})

@login_required
def job_page(request):
    jobs = Job.objects.all()
    return render(request, 'app/job_page.html', {'jobs': jobs})

def login_view(request):
    return auth_views.LoginView.as_view(template_name='app/login.html')(request)

def logout_view(request):
    logout(request)
    return redirect('login')
