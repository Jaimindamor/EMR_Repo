from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions  import IsAuthenticated
from .custompermission import doctorpermission,nursepermission,frontdeskpermission,patientpermission
from django.shortcuts import render
from rest_framework.status import HTTP_202_ACCEPTED,HTTP_204_NO_CONTENT,HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_401_UNAUTHORIZED
from .models import Patient_data,Procedure_data
from .serializers import PatientSerializer,ProcedureSerializer,UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
import base64
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
import win32com.client
import pythoncom
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
from fhir.resources.patient import Patient
from fhir.resources.identifier import Identifier
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint

from fhir.resources.address import Address
from fhir.resources.extension import Extension

from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.procedure import Procedure
from fhir.resources.coding import Coding
from fhir.resources.reference import Reference
# from fhir.resources import Procedure, Identifier
from datetime import datetime
from fhir.resources.resource import Resource
from fhir.resources.identifier import Identifier
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.reference import Reference


 
# Create your views here.
def updateproceduredata(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        patient=request.POST.get('patient')
        status=request.POST.get('status')
        statusReason=request.POST.get('statusReason')
        procedure_date=request.POST.get('procedure_date')
        procedure_time=request.POST.get('procedure_time')
        category=request.POST.get('category')
        procedure_name=request.POST.get('procedure_name')
        clinic_address=request.POST.get('clinic_address')
        notes=request.POST.get('notes')
        report=request.POST.get('report')
        
        # Create a dictionary to hold the fields to update
        fields_to_update = {}
        if patient:
            fields_to_update['patient'] = patient
        if status:
            fields_to_update['status'] = status
        if statusReason:
            fields_to_update['mobile_number'] = statusReason
        if procedure_date:
            fields_to_update['procedure_date'] = procedure_date
        if procedure_time:
            fields_to_update['procedure_time'] = procedure_time
        if category:
            fields_to_update['category'] = category
        if procedure_name:
            fields_to_update['procedure_name'] = procedure_name
        if clinic_address:
            fields_to_update['clinic_address'] = clinic_address
        
        if notes:
            fields_to_update['notes'] = notes
        if report:
            fields_to_update['report'] = report
        
        try:
            # Update the objects that match the condition
            Procedure.objects.filter(id=id).update(**fields_to_update)
            return render(request, 'updateprocedure.html',{'data_saved': True})
        except Patient.DoesNotExist:
            return HttpResponse("Object with ID {} does not exist.".format(id))
def deleteprocedure(request):
    return render(request, 'deleteprocedure.html')

def deleteproceduredata(request):
    if request.method == 'POST': 
        id=request.POST.get('id')
        procedure=Procedure.objects.get(id=id)
        procedure.delete()
        return render(request, 'deleteprocedure.html',{'data_saved': True})
    
def addprocedure(request):
    patients = Patient_data.objects.all()
    print(patients)
    return render(request, 'addprocedure.html' , {'patients': patients} )
def addproceduredata(request):
    if request.method == 'POST':     
        patient=request.POST.get('patient_id')
        status=request.POST.get('status')
        statusReason=request.POST.get('statusReason')
        procedure_date=request.POST.get('procedure_date')
        procedure_time=request.POST.get('procedure_time')
        category=request.POST.get('category')
        procedure_name=request.POST.get('procedure_name')
        clinic_address=request.POST.get('clinic_address')
        notes=request.POST.get('notes')
        report=request.POST.get('report')
        patientObj = Patient.objects.get(id=int(patient))
        print(patientObj)

        # Create a new procedure entry in the database using the Procedure model
        procedure = Procedure(patient=patientObj, status=status,statusReason=statusReason, 
                          procedure_date=procedure_date,procedure_time=procedure_time, category=category,
                          procedure_name=procedure_name,report=report, 
                          notes=notes,clinic_address=clinic_address)
        procedure.save()
        return render(request, 'addprocedure.html',{'data_saved': True})
    else:
        return HttpResponse("Invalid request method.")
    
def updatepatientdata(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        mobile_number=request.POST.get('mobile_number')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        birthdate=request.POST.get('birthdate')
        email=request.POST.get('email')
        country_code=request.POST.get('country_code')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        emergency_contact_name=request.POST.get('emergency_contact_name')
        emergency_contact_mobile_number=request.POST.get('emergency_contact_mobile_number')
        language=request.POST.get('language')
        
        # Create a dictionary to hold the fields to update
        fields_to_update = {}
        if first_name:
            fields_to_update['first_name'] = first_name
        if last_name:
            fields_to_update['last_name'] = last_name
        if mobile_number:
            fields_to_update['mobile_number'] = mobile_number
        if address:
            fields_to_update['address'] = address
        if gender:
            fields_to_update['gender'] = gender
        if birthdate:
            fields_to_update['birthdate'] = birthdate
        if email:
            fields_to_update['email'] = email
        if country_code:
            fields_to_update['country_code'] = country_code
        
        if city:
            fields_to_update['city'] = city
        if state:
            fields_to_update['state'] = state
            
        if pincode:
            fields_to_update['pincode'] = pincode
        if emergency_contact_name:
            fields_to_update['emergency_contact_name'] = emergency_contact_name    
        
        if emergency_contact_mobile_number:
            fields_to_update['emergency_contact_mobile_number'] = emergency_contact_mobile_number
        if language:
            fields_to_update['language'] = language    
        try:
            # Update the objects that match the condition
            Patient.objects.filter(id=int(id)).update(**fields_to_update)
            return render(request, 'updatepatient.html',{'data_saved': True})
        except Patient.DoesNotExist:
            return HttpResponse("Object with ID {} does not exist.".format(id))

def deletepatientdata(request):
    if request.method == 'POST': 
        id=request.POST.get('id')
        patient=Patient.objects.get(id=id)
        print(patient)
        patient.delete()
        return render(request, 'deletepatient.html',{'data_saved': True})
    

def addpatientdata(request):
    if request.method == 'POST':     
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        mobile_number=request.POST.get('mobile_number')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        birthdate=request.POST.get('birthdate')
        email=request.POST.get('email')
        country_code=request.POST.get('country_code')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        emergency_contact_name=request.POST.get('emergency_contact_name')
        emergency_contact_mobile_number=request.POST.get('emergency_contact_mobile_number')
        language=request.POST.get('language')

        
        # Create a new patient entry in the database using the Patient model
        patient = Patient(first_name=first_name, last_name=last_name,mobile_number=mobile_number, 
                          address=address,gender=gender, birthdate=birthdate,
                          email=email, country_code=country_code,city=city, 
                          state=state,pincode=pincode, emergency_contact_name=emergency_contact_name
                          ,emergency_contact_mobile_number=emergency_contact_mobile_number,
                          language=language)
        patient.save()
        return render(request, 'addpatient.html',{'data_saved': True})
    else:
        return HttpResponse("Invalid request method.")
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# Function to get procedure data acc to FHIR    
def create_procedure_resource(procedure_instance):
    # Create a procedure resource
    # Add subject (patient) reference
    subject_reference = Reference()
    subject_reference.reference = f"Patient/{procedure_instance.patient}"
    temp = {"status": procedure_instance.status, "subject": subject_reference}
    procedure_resource = Procedure(**temp)

    # Add procedure identifier
    identifier = Identifier()
    identifier.system = "http://example.org/procedure"
    identifier.value = str(procedure_instance.id)
    procedure_resource.identifier = [identifier]


    # Add procedure code
    code = CodeableConcept()
    code.text = procedure_instance.procedure_name
    procedure_resource.code = code


    # Add procedure performed date and time
    if procedure_instance.procedure_date:
        performed_date = datetime.combine(procedure_instance.procedure_date, procedure_instance.procedure_time)
        procedure_resource.occurrenceDateTime = performed_date.strftime("%Y-%m-%dT%H:%M:%S")

    # Add clinic address as part of notes
    notes = f"Clinic Address: {procedure_instance.clinic_address}. {procedure_instance.notes}"
    procedure_resource.note = [{"text": notes}]

    return procedure_resource

# Function to get patient data acc to FHIR 
def create_patient_resource(patient_model_instance):
    # Create a patient resource
    patient_resource = Patient()

    # Add patient identifier
    identifier = Identifier()
    identifier.system = "http://example.org/patient"
    identifier.value = str(patient_model_instance.id)
    patient_resource.identifier = [identifier]

    # Add patient name
    name = HumanName()
    name.family = patient_model_instance.last_name
    name.given = [patient_model_instance.first_name]
    patient_resource.name = [name]

    # Add patient gender
    patient_resource.gender = patient_model_instance.gender

    # Add patient birth date
    patient_resource.birthDate = patient_model_instance.birthdate.strftime("%Y-%m-%d")

    # Add patient address
    address = Address()
    address.use = "home"
    address.type = "both"
    address.text = patient_model_instance.address
    address.city = patient_model_instance.city
    address.state = patient_model_instance.state
    address.postalCode = patient_model_instance.pincode
    patient_resource.address = [address]

    # Add patient telecom
    telecom = ContactPoint()
    telecom.system = "phone"
    telecom.value = patient_model_instance.mobile_number
    patient_resource.telecom = [telecom]

    # Add patient language as extension
    if patient_model_instance.language:
        language_extension = Extension()
        language_extension.url = "http://hl7.org/fhir/StructureDefinition/patient-primary-language"
        language_extension.valueString = patient_model_instance.language
        patient_resource.extension = [language_extension]

    return patient_resource    
    
    
    
    
    
    
def updatepatient(request):
    return render(request, 'updatepatient.html')

def patientresource(request):
    return render(request, 'patientresource.html')
def procedureresource(request):
    return render(request, 'procedureresource.html')
def updateprocedure(request):
    return render(request, 'updateprocedure.html')    
def deletepatient(request):
    return render(request, 'deletepatient.html')
        
def managepatient(request):
    patients = Patient_data.objects.all()
    return render(request, 'managepatient.html',{'patients': patients})

def addpatient(request):
    return render(request, 'addpatient.html')    
def manageprocedure(request):
    procedure=Procedure_data .objects.all()
    return render(request, 'manageprocedure.html',{'procedures' : procedure})
def manage(request):
    return render(request, 'manage.html')
def home(request):
    return render(request, 'home.html')
def navbar(request):
    return render(request, 'navbar.html')
def update_record(request):
    return render(request, 'update_record.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def record(request):
    return render(request, 'record.html')
def add_record(request):
    return render(request, 'add_record.html')
def base(request):
    return render(request, 'base.html')
def updatepatient(request):
    return render(request, 'updatepatient.html')
# Email Sending After Procedure Added 
def send_email(msg,mail):
    recipient=mail
    pythoncom.CoInitialize()
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)  # 0 represents mail item
    mail.To =recipient 
    mail.Subject = 'Greetings'
    mail.Body = msg
    mail.Send()
    
class PatientAPI(APIView):

    def get(self,request,format=None):
        try:
            patient=Patient_data.objects.all()
            serializer=PatientSerializer(data=patient,many=True)

            return render(request, 'managepatient.html',{'patients': patient})
            return Response(serializer.data,status=HTTP_200_OK)
        except:  
            return Response("Patient Not found !!!!!",status=HTTP_404_NOT_FOUND)
        else:
            return Response("Id Not provided!!!!",status=HTTP_204_NO_CONTENT)

    def put(self,request,format=None):
        pythondata=request.data
        print(pythondata)
        id=request.data.get('id')
        if id is not None:
            patient=Patient_data.objects.get(id=id)
            serializer=PatientSerializer(patient,data=pythondata,partial=True)
            if serializer.is_valid():
                serializer.save()
                print("hello")
                return Response(serializer.data,status=HTTP_200_OK)
                return render(request, 'updatepatient.html')
            print(serializer.errors)
            return Response(serializer.errors)
        
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
                return render(request, 'addpatient.html',{'data_saved': True})
                return Response(res,status=HTTP_200_OK)
            return Response(serializer.errors,status=HTTP_401_UNAUTHORIZED)
        else:
            return Response("No Content!!!!",status=HTTP_204_NO_CONTENT)
        
    def delete(self,request,format=None):
        id=request.data.get('id')
        if id is not None:
            try:
                patient=Patient_data.objects.get(id=id)
                patient.delete()
                return render(request, 'deletepatient.html',{'data_saved': True})
                return Response("Data deleted !!!!!!!!",status=HTTP_202_ACCEPTED)
            except:
                return Response("Patient data not found !!!!!",status=HTTP_404_NOT_FOUND)
        else:
            return Response("Id not Mentioned !!!!",status=HTTP_204_NO_CONTENT)
        
# class PatientAPI(APIView):
#     # authentication_classes=[JWTAuthentication]
#     # permission_classes=[nursepermission|frontdeskpermission]
#     def get(self,request,format=None):
#         id=request.GET.get('id')
#         if id is not None:
#             try:
#                 patient=Patient.objects.get(id=id)   
#                 serializer=PatientSerializer(patient)
#                 return render(request, 'managepatient.html',{'patients': patient})
#                 return Response(serializer.data,status=HTTP_200_OK)
#             except:  
#                 return Response("Patient Not found !!!!!",status=HTTP_404_NOT_FOUND)
#         else:
#             return Response("Id Not provided!!!!",status=HTTP_204_NO_CONTENT)

#     def put(self,request,format=None):
#         pythondata=request.data
#         id=request.data.get('id')
#         if id is not None:
#             try:
#                 patient=Patient.objects.get(id=id)
#                 serializer=PatientSerializer(patient,data=pythondata,partial=True)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data,status=HTTP_200_OK)
#             except:
#                 return Response("Patient data not found !!!!!",status=HTTP_404_NOT_FOUND)
#         elif id is None and request.data:
#             return Response("Id  missing !!!!",status=HTTP_204_NO_CONTENT)
#         else:
#             return Response("No Content!!!!",status=HTTP_204_NO_CONTENT)
            
#     def post(self,request,format=None): 
#         python_data=request.data
#         if python_data:
#             serializer=PatientSerializer(data=python_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 res={'msg':' data saved !!!!!!!!!!!'}
#                 return Response(res,status=HTTP_200_OK)
#             return Response(serializer.errors,status=HTTP_401_UNAUTHORIZED)
#         else:
#             return Response("No Content!!!!",status=HTTP_204_NO_CONTENT)
        
#     def delete(self,request,format=None):
#         id=request.data.get('id')
#         if id is not None:
#             try:
#                 patient=Patient.objects.get(id=id)
#                 patient.delete()
#                 return Response("Data deleted !!!!!!!!",status=HTTP_202_ACCEPTED)
#             except:
#                 return Response("Patient data not found !!!!!",status=HTTP_404_NOT_FOUND)
#         else:
#             return Response("Id not Mentioned !!!!",status=HTTP_204_NO_CONTENT)


class ProcedureAPI(APIView):
    

    def get(self,request,format=None):
        try:
            procedure=Procedure_data.objects.all()
            serializer=ProcedureSerializer(procedure,many=True)
            return render(request, 'manageprocedure.html',{'procedures': serializer.data})
        except:
            return Response("Procedure Data Not Found !!!!",status=HTTP_404_NOT_FOUND)             

    def put(self,request,format=None):
        pythondata=request.data
        print(pythondata)
        if request.FILES:
            pythondata['report']=request.FILES.get('report')
            print(pythondata['report'])
        id=request.data.get('id')
        if id is not None:
            procedure=Procedure_data.objects.get(id=id)
            serializer=ProcedureSerializer(procedure,data=pythondata,partial=True)
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=HTTP_200_OK)
            print(serializer.errors)
            return Response(serializer.errors)
        elif id is None and pythondata:
            return Response("Id  missing !!!!",status=HTTP_404_NOT_FOUND)
        else:
            return Response("No Content !!!!!!!",status=HTTP_204_NO_CONTENT)

    def post(self,request,format=None): 
        python_data=request.data
        id=request.data.get("patient")
        if request.FILES:
            python_data['report']=request.FILES['report']
        if python_data:
            #python_data['user']=request.user.id
            serializer=ProcedureSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                res={'msg':' data saved !!!!!!!!!!!'}
                return render(request, 'addprocedure.html',{'data_saved': True})
                return Response(res,status=HTTP_200_OK)
            return Response(serializer.errors,status=HTTP_401_UNAUTHORIZED)
        else:
            return Response("No Content !!!!!!!",status=HTTP_204_NO_CONTENT)
    
    def delete(self,request,format=None):
        id=request.data.get('id')
        if id is not None:
            try:
                patient=Procedure_data.objects.get(id=id)
                print(patient)
                patient.delete()
                return render(request, 'deleteprocedure.html',{'data_saved': True})
                return HttpResponseRedirect('/deleteprocedure/')
                return render(request, 'manageprocedure.html',{'data': True})
                return Response({"Data deleted !!!!!!!!"},status=HTTP_202_ACCEPTED)
            except:
                return Response({"Procedure Data Not found !!!!!!!"},status=HTTP_404_NOT_FOUND)
        else:
            return Response({"Id is not Mentioned !!!!!!!"},status=HTTP_204_NO_CONTENT)
# class ProcedureAPI(APIView):
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[doctorpermission|nursepermission]
#     def get(self,request,format=None):
#         id=request.data.get('id')
#         if id is not None:
#             try:
#                 procedure=Procedure.objects.get(id=id)
#                 serializer=ProcedureSerializer(procedure)
#                 x=serializer['report'].value
#                 if x:
#                     x=x.encode('utf-8')
#                     x=base64.b64encode(x)
#                     new_serializer =serializer.data
#                     new_serializer['new_report']=x.decode() 
#                     return Response(new_serializer,status=HTTP_200_OK)
#                 else:
#                     return Response(serializer.data,status=HTTP_200_OK)
#             except:
#                 return Response("Procedure Data Not Found !!!!",status=HTTP_404_NOT_FOUND)             
#         else:
#             return Response("ID  is not given !!!!",status=HTTP_204_NO_CONTENT)
            
#     def put(self,request,format=None):
#         pythondata=request.data
#         if request.FILES:
#             pythondata['report']=request.FILES['report']
#         id=request.data.get('id')
#         if id is not None:
#             try:
#                 procedure=Procedure.objects.get(id=id)
#                 serializer=ProcedureSerializer(procedure,data=pythondata,partial=True)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data,status=HTTP_200_OK)
#                 return Response(serializer.errors,status=HTTP_401_UNAUTHORIZED)
#             except:
#                 return Response("Procedure Data Not Found !!!!",status=HTTP_404_NOT_FOUND)  
#         elif id is None and pythondata:
#             return Response("Id  missing !!!!",status=HTTP_404_NOT_FOUND)
#         else:
#             return Response("No Content !!!!!!!",status=HTTP_204_NO_CONTENT)

#     def post(self,request,format=None): 
#         python_data=request.data
#         if request.FILES:
#             python_data['report']=request.FILES['report']
#         if python_data:
#             python_data['user']=request.user.id
#             serializer=ProcedureSerializer(data=python_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 res={'msg':' data saved !!!!!!!!!!!'}
#                 return Response(res,status=HTTP_200_OK)
#             return Response(serializer.errors,status=HTTP_401_UNAUTHORIZED)
#         else:
#             return Response("No Content !!!!!!!",status=HTTP_204_NO_CONTENT)
    
#     def delete(self,request,format=None):
#         id=request.data.get('id')
#         if id is not None:
#             try:
#                 patient=Procedure.objects.get(id=id)
#                 patient.delete()
#                 return Response({"Data deleted !!!!!!!!"},status=HTTP_202_ACCEPTED)
#             except:
#                 return Response({"Procedure Data Not found !!!!!!!"},status=HTTP_404_NOT_FOUND)
#         else:
#             return Response({"Id is not Mentioned !!!!!!!"},status=HTTP_204_NO_CONTENT)
            
class LoginAPI(APIView):
    
    def post(self,request):
        try:
            print(request.data)
            decoded_data= base64.b64decode(request.data.get("info")).decode('UTF-8')
            print(decoded_data  )
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
        patient=Patient_data.objects.get(email=request.user.email)
        if patient:
            patient_serializer=PatientSerializer(patient)
            patient_data=dict(patient_serializer.data)
            procedure=Procedure_data.objects.filter(patient=patient.id)
            if procedure:
                procedure_serializer=ProcedureSerializer(procedure,many=True)
                procedure_data=list(procedure_serializer.data)
                patient_data['Procedure_list']=procedure_data
                return Response(patient_data,status=HTTP_200_OK)
            patient_data['Procedure_list']="No procedure Conducted"
            return Response(patient_data,status=HTTP_200_OK)
        return Response("No Patient Found with this mail ID !!!!!!!!!!",status=HTTP_204_NO_CONTENT)    

class PatientView_Queryobject(APIView):
    permission_classes=[patientpermission]
    def get(self,request,format=None): 
        patient=Patient_data.objects.filter(email=request.user.email).values().first()
        patient_data=dict(patient)
        if patient:      
            procedures=Procedure_data.objects.filter(patient=patient['id']).values()
            procedure_data=[procedure for procedure in procedures]
            if procedures:
                patient_data["Procedure List "]=procedure_data
                return Response(patient_data,status=HTTP_200_OK)
            patient_data["Procedure List "]="No procedure Conducted"
            return Response(patient_data,status=HTTP_200_OK)
        
        return Response("No Patient Found with this mail ID !!!!!!!!!!",status=HTTP_204_NO_CONTENT)
    
class Register_user(APIView):
    
    def post(self, request):
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return render(request, 'login.html')
            return Response(serializer.errors, status=HTTP_204_NO_CONTENT)
        
class Json_Format(APIView):
    def post(self,request,format=None):
        
        patient=Patient_data.objects.get(id=request.data.get('id'))
        serializer=PatientSerializer(patient)      
        # Assuming you have a patient_model_instance already created
        fhir_patient_resource = create_patient_resource(patient)

        x=fhir_patient_resource.json()
        # x=json.dumps(x)
        vari=json.loads(x)
        print(vari)
        # return render(request, 'patientresource.html',{'datas': vari})
        # return render(request,'patientresource.html',{'data': vari })
        return Response(data=vari, status=HTTP_200_OK)
        return HttpResponseRedirect('/patientresource/',{'datas':vari})
    
class Json_Format_procedure(APIView):
    def post(self,request,format=None):
        
        procedure=Procedure_data.objects.get(id=request.data.get('id'))
        # Assuming you have a patient_model_instance already created
        fhir_patient_resource = create_procedure_resource(procedure)
        x=fhir_patient_resource.json()
        vari=json.loads(x)
        print(vari)
        return Response(data=vari, status=HTTP_200_OK)
        # return Response({"data": json.loads(x)}, status=HTTP_200_OK)

class Data_Transfer(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[doctorpermission|nursepermission]
    def post(self,request,format=None):
        data=request.data
        print(f"{data} Done Sended !!!!!!!")
        return Response("Data Snd Successfully !!!!!!!!")