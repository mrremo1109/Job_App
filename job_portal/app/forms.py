# app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from wtforms import ValidationError
from .models import Job, User, Employee, Employer

class EmployeeSignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    dob = forms.DateField()
    email = forms.EmailField()
    location = forms.CharField(max_length=100)
    postcode = forms.CharField(max_length=20)
    university = forms.CharField(max_length=100)
    education_details = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'dob', 'email', 'location', 'postcode', 'university', 'education_details', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employee = True
        if commit:
            user.save()
            Employee.objects.create(user=user, 
                                    full_name=self.cleaned_data.get('full_name'),
                                    dob=self.cleaned_data.get('dob'),
                                    location=self.cleaned_data.get('location'),
                                    postcode=self.cleaned_data.get('postcode'),
                                    university=self.cleaned_data.get('university'),
                                    education_details=self.cleaned_data.get('education_details'))
        return user

class EmployerSignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    dob = forms.DateField()
    shop_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)
    postcode = forms.CharField(max_length=10)
    number_of_employees = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'full_name', 'dob', 'shop_name', 'email', 'phone_number', 'address', 'postcode', 'number_of_employees', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employer = True
        if commit:
            user.save()
            Employer.objects.create(user=user,
                                    name=self.cleaned_data.get('name'),
                                    dob=self.cleaned_data.get('dob'),
                                    shop_name=self.cleaned_data.get('shop_name'),
                                    phone_number=self.cleaned_data.get('phone_number'),
                                    address=self.cleaned_data.get('address'),
                                    postcode=self.cleaned_data.get('postcode'),
                                    num_employees=self.cleaned_data.get('num_employees'))
        return user

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'responsibilities', 'vacancies', 'pay_per_hour', 'location', 'postcode', 'eligible_candidates', 'gender']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))