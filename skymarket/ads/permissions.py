# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework import permissions

#
# class IsOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.author == request.user


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.role == 'admin'
