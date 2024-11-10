from rest_framework import permissions


class IsLoggedInUserOrAdmin(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['admin']

    def has_object_permission(self, request, view, obj):
        if self.required_groups is None:
            return False
        return obj == request.user


class IsAdminUser(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['admin']

    def has_permission(self, request, view):
        return request.user

    def has_object_permission(self, request, view, obj):
        return request.user


class IsAdminOrAnonymousUser(permissions.BasePermission):
    required_groups = ['admin', 'anonymous']

    def has_permission(self, request, view):
        return request.user
