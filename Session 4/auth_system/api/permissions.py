from rest_framework.permissions import BasePermission

class IsPremiumUser(BasePermission):
    """
    Allows access only to authenticated users who have is_premium=True.
    """
    message = "Access Denied: Only premium users can access ticket booking."

    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        
        return hasattr(request.user, 'profile') and request.user.profile.is_premium