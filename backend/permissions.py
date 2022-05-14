from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    A base class from which all permission classes should inherit.
    """

    def has_permission(self, request, view):
       # Authenticated users only can see list view
        if request.user and request.user.is_authenticated:
            return True
        return False

    # Authorization
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """

        # POST
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user


class IsSafeMethod(permissions.BasePermission):
    message = 'Only save http methods allowed'

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class IsPremiumUser(permissions.BasePermission):
    message = 'You have to be a premium user for this action'

    def has_object_permission(self, request, view, obj):
        return request.user.is_premium


class IsPutOrGetMethod(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method == 'PUT' or request.method == 'GET'


class IsCreator(permissions.BasePermission):
    message = 'You have to be the creator in order to amend this surfspot'

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class IsSelf(permissions.BasePermission):
    message = 'You are not allowed to see this profile.'

    def has_object_permission(self, request, view, obj):
        return obj == request.user