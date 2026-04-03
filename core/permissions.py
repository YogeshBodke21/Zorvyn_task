from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'
    

class RecordPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return request.user.role in ['admin', 'analyst', 'viewer']
        
        if request.method == 'POST':
            return request.user.role in ['admin', 'analyst',]
        
        return request.user.role == 'admin'
        

