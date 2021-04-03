from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Subscribermail(models.Model):
    email = models.EmailField(('email address'), unique=True, error_messages={'unique':"An account exists with this email."})

class ContactUsForm(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(('email address'), unique=False)
    phone_number = PhoneNumberField(null=False, blank=False, unique=False)
    domain = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

class JoinUsForm(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(('email address'), unique=False)
    phone_number = PhoneNumberField(null=False, blank=False, unique=False)
    domain = models.CharField(max_length=50, blank=True, null=True)
    experience = models.CharField(max_length=30, blank=False, null=False)
    message = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


