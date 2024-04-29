from .views import send_email
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import pre_delete,pre_save,post_delete,post_save
from .models  import Patient_data,Procedure_data

#signal will show msg when a patient data is going to add into the database
@receiver(pre_save,sender=Procedure_data)
def before_save(sender,instance,**kwargs):
    print("Patient will be Added in the DATABASE**********")
    
#signal will show msg when a patient data is added into the database
@receiver(post_save,sender=Procedure_data)
def after_save(sender,instance,**kwargs):
    id=instance.patient
    patient=Patient_data.objects.get(mobile_number=id)
    print(patient)
    mail=patient.email
    patient_name=patient.first_name+patient.last_name
    procedure_name=instance.procedure_name
    msg=f'''
    Hello {patient_name} ,
    Your Procedure {procedure_name} has been done.
    Please login into your application to view the report.
    
    Thankyou.
    
    Best Regards,
    NSVTech'''
    send_email(msg,mail)
    print(" Patient Added in the DATABASE **********")

#signal will show msg when a patient data is going to delete from the database   
@receiver(pre_delete,sender=Procedure_data)
def before_delete(sender,instance,**kwargs):
    print("pre_delete method **********")

#signal will show msg when a patient data is deleted from the database    
@receiver(post_delete,sender=Procedure_data)
def after_delete(sender,instance,**kwargs):
    print("post_delete method  **********")