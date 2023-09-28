from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        """Anyone can see article details"""
        return True

    def has_object_permission(self, request, view, obj):
        """Only the author of the article can manipulate it"""
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
