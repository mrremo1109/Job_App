
# Create your models here.
# app/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='app_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='app_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    location = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    university = models.CharField(max_length=200)
    education_details = models.TextField()

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    shop_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=20)
    number_employees = models.IntegerField()

class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    responsibilities = models.TextField()
    vacancies = models.IntegerField()
    pay_per_hour = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=200)
    postcode = models.CharField(max_length=20)
    eligible_candidates = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.role
