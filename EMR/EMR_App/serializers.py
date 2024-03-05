from rest_framework import serializers
from .models import Patient,Procedure

# Custom validation 
def check_mobile_number(value):
    if len(value)!=10:
        raise serializers.ValidationError("Invalid mobile_number Length should be 10 8********")
   
    
def check_pincode(value):
    if len(value)!=6:
        raise serializers.ValidationError("Invalid pincode Length should be 6 *******")

def check_gender(value):
    gen= ['male','female','others']
    if value not in gen :
        raise serializers.ValidationError(f"Invalid gender choose from this :{ gen } *******")


def check_status(value):
    sta=['preparation ', 'in-progress ' ,'not-done' , 'on-hold','stopped', 'completed ', 'entered-in-error', 'unknown']    
    if value not in sta:
        raise serializers.ValidationError(f"Invalid status choose from this :{ sta } ********")

        
class PatientSerializer(serializers.ModelSerializer):
    
    gender=serializers.CharField(validators=[check_gender])
    mobile_number=serializers.CharField(validators=[check_mobile_number])
    pincode=serializers.CharField(validators=[check_pincode])
    emergency_contact_mobile_number=serializers.CharField(validators=[check_mobile_number])
    
    class Meta:
        model=Patient
        fields='__all__'
    
    # # field level Validation
    # def validate_mobile_number(self,value):
    #     if len(value)!=10:
    #         raise serializers.ValidationError("Invalid mobile_number Length should be 10 !!!!!!!")
    #     return value
    
    # def validate_gender(self,value):
    #     gen=['male','female','others']   
    #     if value not in gen:
    #         raise serializers.ValidationError(f"Invalid gender choose from this :{ gen } !!!!!!")
    #     return value
    
    # def validate_emergency_contant_mobile_number(self,value):
    #     if len(value)!=10:
    #         raise serializers.ValidationError("Invalid emergency_contact_mobile_number Length should be 10 !!!!!!!")
    #     return value
    
    # def validate_pincode(self,value):
    #     if len(value)!=6:
    #         raise serializers.ValidationError("Invalid pincode Length should be 6 !!!!!!!")
    #     return value
    
    # # object-level Validation
    # def validate(self,data):
    #     mobile_number=data.get('mobile_number')
    #     emergency_contact_mobile_number=data.get('emergency_contact_mobile_number')
    #     gender=data.get('gender')
    #     pincode=data.get('pincode')
    #     gen=['male','female','others']
    #     if len(mobile_number)!=10:
    #         raise serializers.ValidationError("Invalid mobile_number Length should be 10 #####")
    #     if len(emergency_contact_mobile_number)!=10:
    #         raise serializers.ValidationError("Invalid mobile_number Length should be 10 #####")
    #     if gender not in gen:
    #         raise serializers.ValidationError(f"Invalid status choose from this :{ gen } ####")
    #     if len(pincode)!=6:
    #         raise serializers.ValidationError("Invalid pincode Length should be 6 ###")
    #     return data
    
    
class ProcedureSerializer(serializers.ModelSerializer):
    status=serializers.CharField(validators=[check_status])
    class Meta:
        model=Procedure
        fields='__all__'
    # # field level Validation
    # def validate_status(self,value):
    #     sta=['preparation ', 'in-progress ' ,'not-done' , 'on-hold','stopped', 'completed ', 'entered-in-error', 'unknown']    
    #     if value not in sta:
    #         raise serializers.ValidationError(f"Invalid status choose from this :{ sta } !!!!!!!!!")
    #     return value
    
    
    # # object-level Validation
    # def validate(self,data):
    #     status=data.get('status')
    #     sta=['preparation ', 'in-progress ' ,'not-done' , 'on-hold','stopped', 'completed ', 'entered-in-error', 'unknown']    
    #     if status not in sta:
    #         raise serializers.ValidationError(f"Invalid status choose from this :{ sta } ###")
    #     return data
        
        
        
        
    
            
        
            
        
        
        
    