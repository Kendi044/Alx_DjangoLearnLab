
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit/delete it.
    Read permissions are allowed to any authenticated user.
    """
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS requests (read access) for anyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions (PUT, POST, DELETE) are only allowed to the author
        return obj.author == request.user