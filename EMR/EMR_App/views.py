from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions  import IsAuthenticated
from .custompermission import doctorpermission,nursepermission,frontdeskpermission,patientpermission
from rest_framework.status import HTTP_202_ACCEPTED,HTTP_204_NO_CONTENT,HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_401_UNAUTHORIZED
from .models import Patient,Procedure
from .serializers import PatientSerializer,ProcedureSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
import base64
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
import win32com.client
import pythoncom

# Create your views here.

def send_email(msg,mail):
    recipient =mail
    pythoncom.CoInitialize()
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)  # 0 represents mail item
    mail.To =recipient 
    mail.Subject = 'Greetings'
    mail.Body = msg
    mail.Send()
    
class PatientAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[nursepermission|frontdeskpermission]
    def get(self,request,format=None):
        id=request.data.get('id')
        if id is not None:
            try:
                patient=Patient.objects.get(id=id)
                serializer=PatientSerializer(patient)
                return Response(serializer.data,status=HTTP_200_OK)
            except:    
                return Response("Patient Not found !!!!!",status=HTTP_404_NOT_FOUND)
        else:
            return Response("Id Not provided!!!!",status=HTTP_204_NO_CONTENT)
   
    def put(self,request,format=None):
        pythondata=request.data
        id=request.data.get('id')
        if id is not None:
            try:
                patient=Patient.objects.get(id=id)
                serializer=PatientSerializer(patient,data=pythondata,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=HTTP_200_OK)
            except:
                return Response("Patient data not found !!!!!",status=HTTP_404_NOT_FOUND)
        elif id is None and request.data:
            return Response("Id  missing !!!!",status=HTTP_204_NO_CONTENT)
        else:
            return Response("No Content!!!!",status=HTTP_204_NO_CONTENT)
            
    def post(self,request,format=None): 
        python_data=request.data
        if python_data:
            serializer=PatientSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                res={'msg':' data saved !!!!!!!!!!!'}
                return Response(res,status=HTTP_200_OK)
            return Response(serializer.errors,status=HTTP_401_UNAUTHORIZED)
        else:
            return Response("No Content!!!!",status=HTTP_204_NO_CONTENT)
        
    def delete(self,request,format=None):
        id=request.data.get('id')
        if id is not None:
            try:
                patient=Patient.objects.get(id=id)
                patient.delete()
                return Response("Data deleted !!!!!!!!",status=HTTP_202_ACCEPTED)
            except:
                return Response("Patient data not found !!!!!",status=HTTP_404_NOT_FOUND)
        else:
            return Response("Id not Mentioned !!!!",status=HTTP_204_NO_CONTENT)

class ProcedureAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[doctorpermission|nursepermission]
    def get(self,request,format=None):
        id=request.data.get('id')
        if id is not None:
            try:
                procedure=Procedure.objects.get(id=id)
                serializer=ProcedureSerializer(procedure)
                x=serializer['report'].value
                if x:
                    x=x.encode('utf-8')
                    x=base64.b64encode(x)
                    new_serializer =serializer.data
                    new_serializer['new_report']=x.decode() 
                    return Response(new_serializer,status=HTTP_200_OK)
                else:
                    return Response(serializer.data,status=HTTP_200_OK)
            except:
                return Response("Procedure Data Not Found !!!!",status=HTTP_404_NOT_FOUND)             
        else:
            return Response("ID  is not given !!!!",status=HTTP_204_NO_CONTENT)
            
    def put(self,request,format=None):
        pythondata=request.data
        if request.FILES:
            pythondata['report']=request.FILES['report']
        id=request.data.get('id')
        if id is not None:
            try:
                procedure=Procedure.objects.get(id=id)
                serializer=ProcedureSerializer(procedure,data=pythondata,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=HTTP_200_OK)
                return Response(serializer.errors,status=HTTP_401_UNAUTHORIZED)
            except:
                return Response("Procedure Data Not Found !!!!",status=HTTP_404_NOT_FOUND)  
        elif id is None and pythondata:
            return Response("Id  missing !!!!",status=HTTP_404_NOT_FOUND)
        else:
            return Response("No Content !!!!!!!",status=HTTP_204_NO_CONTENT)

    def post(self,request,format=None): 
        python_data=request.data
        if request.FILES:
            python_data['report']=request.FILES['report']
        if python_data:
            python_data['user']=request.user.id
            serializer=ProcedureSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                res={'msg':' data saved !!!!!!!!!!!'}
                return Response(res,status=HTTP_200_OK)
            return Response(serializer.errors,status=HTTP_401_UNAUTHORIZED)
        else:
            return Response("No Content !!!!!!!",status=HTTP_204_NO_CONTENT)
    
    def delete(self,request,format=None):
        id=request.data.get('id')
        if id is not None:
            try:
                patient=Procedure.objects.get(id=id)
                patient.delete()
                return Response({"Data deleted !!!!!!!!"},status=HTTP_202_ACCEPTED)
            except:
                return Response({"Procedure Data Not found !!!!!!!"},status=HTTP_404_NOT_FOUND)
        else:
            return Response({"Id is not Mentioned !!!!!!!"},status=HTTP_204_NO_CONTENT)
            
class LoginAPI(APIView):
    
    def post(self,request):
        try:
            decoded_data= base64.b64decode(request.data.get("info")).decode('UTF-8')
            username,password=str(decoded_data).split(":")
            user=authenticate(username=username,password=password)
            if user :
                refresh = RefreshToken.for_user(user)
                return Response({'token': str(refresh),
                                'acces_token': str(refresh.access_token)})
            else:
                return Response({'msg': 'User/Password  is invalid  !!!!!'})
        except:
            return Response({'msg': 'Value is not correctly base64 encoded  is invalid  !!!!!'})

class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"Token added to blacklist !!!!!!!!"},status=HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)})

class PatientView(APIView):
    permission_classes=[patientpermission]
    def get(self,request,format=None): 
        patient=Patient.objects.get(email=request.user.email)
        serializer=PatientSerializer(patient)
        procedure=Procedure.objects.filter(patient=patient.id)
        serializer1=ProcedureSerializer(procedure,many=True)
        response_data = {
            'patient_data': serializer.data,
            'procedure_data': serializer1.data
        }
        return Response(response_data)
    

class PatientView_Queryobject(APIView):
    permission_classes=[patientpermission]
    def get(self,request,format=None): 
        patient=Patient.objects.get(email=request.user.email)      
        procedures=Procedure.objects.filter(patient=patient.id)
        patient_data={
            "id": 53,
        "first_name": patient.first_name,
        "last_name": patient.last_name,
        "mobile_number": patient.mobile_number,
        "address": patient.address,
        "gender": patient.gender,
        "birthdate": patient.birthdate,
        "email": patient.email,
        "country_code": patient.country_code,
        "city": patient.city,
        "state": patient.state,
        "pincode": patient.pincode,
        "emergency_contact_name": patient.emergency_contact_name ,
        "emergency_contact_mobile_number": patient.emergency_contact_mobile_number,
        "language": patient.language,
        "create_date":patient.create_date,
        "update_date": patient.update_date
        }
        procedure_data=[]
        for procedure in procedures:
            # procedure_report=str(procedure.report).split("\\")
            # print(procedure_report)
            print(procedure.report)
            print(procedure.user)
            print(procedure.patient)
            procedure_data.append({ 
                "id": procedure.id,
              "report" : str(procedure.report),
            "status": procedure.status,
            "statusReason":procedure.statusReason,
            "procedure_date": procedure.procedure_date,
            "procedure_time":procedure.procedure_time,
            "category": procedure.category,
            "procedure_name": procedure.procedure_name,
            "clinic_address": procedure.clinic_address,
            "notes": procedure.notes,
            "create_date":procedure.create_date,
            "update_date":procedure.update_date,
            "user":procedure.user.id,
            "patient":procedure.patient.id,
                
            })
        response_Data={    "patient_data": patient_data,
                       "procedure data": procedure_data}
        return Response(response_Data)
        