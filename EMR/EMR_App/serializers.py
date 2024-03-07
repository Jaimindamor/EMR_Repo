from rest_framework import serializers
from .models import Patient,Procedure
from django.core.validators import FileExtensionValidator
class PatientSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Patient
        fields='__all__'
    
    # object-level Validation
    def validate(self,data):
        mobile_number=data.get('mobile_number')
        emergency_contact_mobile_number=data.get('emergency_contact_mobile_number')
        gender=data.get('gender')
        pincode=data.get('pincode')
        gen=['male','female','others']
        if len(mobile_number)!=10:
            raise serializers.ValidationError("Invalid mobile_number Length should be 10 #####")
        if len(emergency_contact_mobile_number)!=10:
            raise serializers.ValidationError("Invalid emergency_contact_mobile_number Length should be 10 #####")
        if gender not in gen:
            raise serializers.ValidationError(f"Invalid status choose from this :{ gen } ####")
        if len(pincode)!=6:
            raise serializers.ValidationError("Invalid pincode Length should be 6 ###")
        return data

class ProcedureSerializer(serializers.ModelSerializer):
    report=serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    class Meta:
        model=Procedure
        fields='__all__'
        
    # object-level Validation
    def validate(self,data):
        status=data.get('status')
        sta=['preparation ', 'in-progress ' ,'not-done' , 'on-hold','stopped', 'completed ', 'entered-in-error', 'unknown']    
        if status not in sta:
            raise serializers.ValidationError(f"Invalid status choose from this :{ sta } ###")
        return data
        
    
        
        
        
    
            
        
            
        
        
        
    