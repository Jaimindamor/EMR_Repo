from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
import re

#Custom Validation 
def check_mobile_number(value):
    reg=r'[1-9]{1}[0-9]{9}'         # r is a convention that indicates a raw string literal to understand regular expression patterns
    if re.findall(reg,value):
        return True
    else:
        raise ValidationError('Not satisfing the condition of (integer value) or (len of number should be 10)')

def check_gender(value):
    reg=r'male|female|others|Not determined'          
    
    if re.search(reg,value):           # search function used to search for a pattern anywhere in the string for the first occurences. 
        return True                    # But findall function used to find all occurence of a pattern in the string .
    else:
        raise ValidationError('Gender not metioned properly : (male|female|others|Not determined) ')

def check_pincode(value):
    reg=r'^[1-9]{1}[0-9]{5}'      # '^'Symbol check the begin of the string
    if re.search(reg,value):
        return True
    else:
        raise ValidationError('Pincode is not correct !!!!!!!!')

def check_emial(value):
    reg=r'[\w]*@[\w]*\.com$'       # '$' Symbol check pattern at the end of the string ,
    if re.search(reg,value):       # '\w'It matches any alphanumeric character [a-zA-Z0-9_] and underscores
        return True
    else:
        raise ValidationError('not a validate emial_id !!!!!!!!')

gender_choice=(
    ("male","male"),
    ("female","female"),
    ("others","others")
    
)
status_choice=(
    ('preparation','preparation'),
    ("in-progress","in-progress"),
    ("not-done","not-done"),
    ("entered-in-error","entered-in-error"),
    ("completed","completed"),
    ("stopped","stopped"),
    ("unknown","unknown"),
    ("on-hold","on-hold"),
)

# Create your models here.

class Patient(models.Model):
    first_name=models.CharField(blank=True,max_length=30)
    last_name=models.CharField(blank=True,max_length=30)
    mobile_number=models.CharField(max_length=10,validators=[check_mobile_number])
    address=models.CharField(max_length=255,blank=True,null=True)
    gender=models.CharField(max_length=15,choices=gender_choice)
    birthdate=models.DateField(blank=True)
    email=models.EmailField(blank=True)
    country_code=models.CharField(blank=True,max_length=3,null=True)
    city=models.CharField(blank=True,max_length=12,null=True)
    state=models.CharField(blank=True,max_length=14,null=True)
    pincode=models.CharField(blank=True,max_length=6,null=True,validators=[MinLengthValidator(6)])
    emergency_contact_name=models.CharField(blank=True,max_length=12,null=True)
    emergency_contact_mobile_number=models.CharField(blank=True,max_length=10,null=True,validators=[MinLengthValidator(10)])
    language=models.CharField(blank=True,max_length=8,null=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True,blank=True, null=True)
     
    def save(self, *args, **kwargs): 
        self.update_date = timezone.now()
        super(Patient, self).save(*args, **kwargs)      # method of the class (Patient) using super() function  .
    def __str__(self):                                  # It ensures that the default save behavior of the parent class is executed.
        return str(self.mobile_number)
    
class Procedure(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    patient=models.ForeignKey(Patient, on_delete=models.SET_NULL,null=True)
    status=models.CharField(max_length=50,choices=status_choice)
    statusReason=models.CharField(blank=True,max_length=50)
    procedure_date=models.DateField(blank=True, null=True)
    procedure_time=models.TimeField(blank=True, null=True)
    category=models.CharField(blank=True,max_length=50)            
    type=models.CharField(max_length=50)             
    clinic_address=models.CharField(blank=True,max_length=50)  
    notes=models.CharField(blank=True,max_length=50)  
    report=models.FileField(null=True,blank=True)

    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True,blank=True, null=True)

    def save(self, *args, **kwargs):    
        self.update_date = timezone.now()
        super(Procedure, self).save(*args, **kwargs)
