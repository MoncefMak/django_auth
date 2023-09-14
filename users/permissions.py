from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission

from users.models import User


class SuperAdminPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == User.Role.SUPERADMIN:
            return True
        raise AuthenticationFailed(detail='You are not authorized to access this resource', code='unauthorized')

