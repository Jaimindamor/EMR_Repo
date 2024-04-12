from rest_framework import serializers
from .models import Patient,Procedure
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User,Group

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # (write_only=True) only be used for input data  and it should not be included when serializing the object for output
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True, required=False) # (PrimaryKeyRelatedField)serializer field used for representing relationships to other models via their primary keys.,(queryset=Group.objects.all())retrieves all the Group objects from the database.

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'groups')
    
    def create(self, validated_data):
        groups_data = validated_data.pop('groups', None)  #This line essentially extracts the groups_id  (if any) from the validated data
        user = User.objects.create_user(**validated_data)
        if groups_data:
            user.groups.set(groups_data) #assignsthe specified groups  tpo user
        return user
        
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
            raise serializers.ValidationError(f"Invalid gender choose from this :{ gen } ####")
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
        

    
        
        
        
    
            
        
            
        
        
        
    