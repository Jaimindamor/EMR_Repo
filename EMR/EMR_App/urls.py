from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns=[
    path('Register_user/',views.Register_user.as_view(),name="Register_user"),
    path('PatientAPI/',views.PatientAPI.as_view(),name="patient"),
    path('Json_Format/',views.Json_Format.as_view(),name="Json_Format"),
    path('Json_Format_procedure/',views.Json_Format_procedure.as_view(),name="Json_Format_procedure"),
    path('LoginAPI/',views.LoginAPI.as_view(),name="login"),
    path('data_transfer/',views.Data_Transfer.as_view(),name="Data_Transfer"),
    path('LogoutAPI/',views.LogoutAPI.as_view(),name="logout"),
    path('ProcedureAPI/',views.ProcedureAPI.as_view(),name="procedure"),
    path('PatientView/',views.PatientView.as_view(),name="Patientview"),
    path('PatientView_Queryobject/',views.PatientView_Queryobject.as_view(),name="PatientView_Queryobject"),
    path('gettoken/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('refreshtoken/',TokenRefreshView.as_view(),name="token_refresh"),
    path('verifytoken/',TokenVerifyView.as_view(),name="token_verify"),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('record/', views.record, name='record'),
    path('add_record/', views.add_record, name='add_record'),
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('update_record/', views.update_record, name='update_record'),
    path('navbar/', views.navbar, name='navbar'),
    path('manage/', views.manage, name='manage'),
    path('managepatient/', views.managepatient, name='managepatient'),
    path('manageprocedure/', views.manageprocedure, name='manageprocedure'),
    path('addpatient/', views.addpatient, name='addpatient'),
    path('addpatientdata/', views.addpatientdata, name='addpatientdata'),
    path('deletepatient/', views.deletepatient, name='deletepatient'),
    path('deletepatientdata/', views.deletepatientdata, name='deletepatientdata'),
    path('updatepatient/', views.updatepatient, name='updatepatient'),
    path('updatepatientdata/', views.updatepatientdata, name='updatepatientdata'),
    path('updateprocedure/', views.updateprocedure, name='updateprocedure'),
    path('updateproceduredata/', views.updateproceduredata, name='updateproceduredata'),
    path('addprocedure/', views.addprocedure, name='addprocedure'),
    path('addproceduredata/', views.addproceduredata, name='addproceduredata'),
    path('deleteprocedure/', views.deleteprocedure, name='deleteprocedure'),
    path('deleteproceduredata/', views.deleteproceduredata, name='deleteproceduredata'),
    path('patientresource/', views.patientresource, name='patientresource'),
    path('procedureresource/', views.procedureresource, name='procedureresource'),
    

]