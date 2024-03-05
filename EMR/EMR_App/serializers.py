from rest_framework import serializers
from .models import Patient,Procedure

def check_mobile_number(value):
    if len(value)!=10:
            raise  serializers.ValidationError('Invalid mobile_number Length should be 10')
    

class PatientSerializer(serializers.ModelSerializer):
    mobile_number=serializers.CharField(validators=[check_mobile_number])

    class Meta:
        model=Patient
        fields='__all__'
        
    def create(self,validate_data):
        
        
        gen=['male','female','others']    
        if len(validate_data['mobile_number'])!=10:
            raise  serializers.ValidationError('Invalid mobile_number Length should be 10 ')
        
        if validate_data['gender'] not in gen :
            raise  serializers.ValidationError(f'Invalid gender choose from this :{ gen } ')
        
        if len(validate_data['emergency_contant_mobile_number'])!=10:
            raise  serializers.ValidationError('Invalid emergency_contant_mobile_number Length should be 10 ')
        
        if len(validate_data['pincode'])!=6:
            raise  serializers.ValidationError('Invalid pincode Length should be 6 ')
        
        return Patient.objects.create(**validate_data)

class ProcedureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Procedure
        fields='__all__'
    
    
    def create(self,validate_data):
        
        sta=['preparation ', 'in-progress ' ,'not-done' , 'on-hold','stopped', 'completed ', 'entered-in-error', 'unknown']    
     
        if validate_data['status'] not in sta :
            raise  serializers.ValidationError(f'Invalid status choose from this :{ sta } ')
        
        return Procedure.objects.create(**validate_data)