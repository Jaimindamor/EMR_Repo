from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import pre_init,pre_delete,pre_save,post_init,post_delete,post_save
def login_success(sender,request,user,**kwargs):
    print("login successfully 2@@@@@@@@@@@@@@@@@@@@@@@@@")
user_logged_in.connect(login_success,sender=User)
    
def logout_success(sender,request,user,**kwargs):
    print("logout successfulyy @@@@@@@")
user_logged_out.connect(logout_success,sender=User)

def login_failed(sender,request,user,**kwargs):
    print("login failed **********")
user_login_failed.connect(login_failed,sender=User)



@receiver(pre_save,sender=User)
def before_save(sender,instance,**kwargs):
    print("pre_save method **********")
    
@receiver(pre_delete,sender=User)
def before_delete(sender,instance,**kwargs):
    print("pre_delete method **********")

@receiver(post_init,sender=User)
def at_end(sender,instance,**kwargs):
    print("post_init method **********")

@receiver(post_save,sender=User)
def after_save(sender,instance,**kwargs):
    print("post_save method  **********")
    
@receiver(post_delete,sender=User)
def after_delete(sender,instance,**kwargs):
    print("post_delete method  **********")


@receiver(post_save,sender=User)
def after_creating(sender,instance, created,**kwargs):
    if created:
        subject="Checking emial sending !!!!!!!"
        message = 'A new user has registered on the EMR__App.'
        recipient_list = ['jaimin.damor@nsvtech.com']  
        send_mail(subject, message,'none43208@gmail.com', recipient_list,fail_silently=False)
    
