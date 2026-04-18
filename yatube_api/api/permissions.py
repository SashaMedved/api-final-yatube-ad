from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Чтение — всем
        if request.method in SAFE_METHODS:
            return True

        # Запись — только автору
        return obj.author == request.user