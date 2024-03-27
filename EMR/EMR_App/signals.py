from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from .views import send_email,msg
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import pre_init,pre_delete,pre_save,post_init,post_delete,post_save
from .models  import Patient

def login_success(sender,request,user,**kwargs):
    print("login successfully 2@@@@@@@@@@@@@@@@@@@@@@@@@")
user_logged_in.connect(login_success,sender=Patient)
    
def logout_success(sender,request,user,**kwargs):
    print("logout successfulyy @@@@@@@")
user_logged_out.connect(logout_success,sender=Patient)

def login_failed(sender,request,user,**kwargs):
    print("login failed **********")
user_login_failed.connect(login_failed,sender=Patient)

@receiver(pre_save,sender=Patient)
def before_save(sender,instance,**kwargs):
    print("Patient will be Added in the DATABASE**********")
    
@receiver(pre_delete,sender=Patient)
def before_delete(sender,instance,**kwargs):
    print("pre_delete method **********")

@receiver(post_init,sender=Patient)
def at_end(sender,instance,**kwargs):
    print("post_init method **********")

@receiver(post_save,sender=Patient)
def after_save(sender,instance,**kwargs):
    msg()
    send_email()
    print(" Patient Added in the DATABASE **********")
    
@receiver(post_delete,sender=Patient)
def after_delete(sender,instance,**kwargs):
    print("post_delete method  **********")