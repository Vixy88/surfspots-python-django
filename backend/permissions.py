from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
  """
    A base class from which all permission classes should inherit.
  """

  def has_permission(self, request, view):
      # Authenticated users only can see list view
      if request.user.is_authenticated:
        return True
      return False