from rest_framework import permissions

#django way is too strict

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # for read only
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # for Write 
        return request.user == obj.purchaser 