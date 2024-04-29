from django.contrib import admin

from .models import Patient_data,Procedure_data

# Register your models here.
@admin.register(Patient_data)
class PatientAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','mobile_number','address','gender','birthdate','email','country_code','city',
                  'state','pincode','emergency_contact_name','emergency_contact_mobile_number','language']
    
    
@admin.register(Procedure_data)
class ProcedureAdmin(admin.ModelAdmin):
    list_display=['id','patient','status','procedure_date','procedure_time','statusReason','category','procedure_name','clinic_address','notes','report']

    
    