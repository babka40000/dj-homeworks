from rest_framework import permissions


class IsOwnerDelete(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True

        return obj.creator == request.user
