from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns=[

    path('PatientAPI/',views.PatientAPI.as_view(),name="patient"),
    path('LoginAPI/',views.LoginAPI.as_view(),name="login"),
    path('LogoutAPI/',views.LogoutAPI.as_view(),name="logout"),
    path('ProcedureAPI/',views.ProcedureAPI.as_view(),name="procedure"),
    path('PatientView/',views.PatientView.as_view(),name="Patientview"),
    path('PatientView_Queryobject/',views.PatientView_Queryobject.as_view(),name="PatientView_Queryobject"),
    path('gettoken/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('refreshtoken/',TokenRefreshView.as_view(),name="token_refresh"),
    path('verifytoken/',TokenVerifyView.as_view(),name="token_verify"),
    
]