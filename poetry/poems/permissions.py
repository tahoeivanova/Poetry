from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsAuthenticated_CUSTOM(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
