from rest_framework import permissions


class VendedorOuAdminPermissions(permissions.Permission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_employee or request.user.is_superuser