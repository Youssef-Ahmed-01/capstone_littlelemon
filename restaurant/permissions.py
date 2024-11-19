from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff)

class IsAdminOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.groups.filter(name='Manager').exists())

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Manager').exists()

class IsUer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='User').exists()
