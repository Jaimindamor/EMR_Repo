from rest_framework.permissions import BasePermission

class nursepermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Nurse's").exists():
            return True

class doctorpermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Doctor's").exists():
            return True
        


class frontdeskpermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Front_Desk").exists():
            return True

class patientpermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Patient").exists():
            return True