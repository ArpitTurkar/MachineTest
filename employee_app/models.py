from django.db import models

# Create your models here.

class Employee(models.Model):
    GENDER_CHOICES = (
        ('Select', 'Select'),
        ('M','MALE'), 
        ('F','FEMALE'), 
        ('O','OTHER')
        )

    emp_fname = models.CharField(max_length=30)
    emp_lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, default=None)
    designation = models.CharField(max_length=225)
    mobile = models.PositiveBigIntegerField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    