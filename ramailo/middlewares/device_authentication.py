from rest_framework.permissions import IsAuthenticated

from ramailo.helpers.user_helper import get_current_user
from ramailo.helpers.view_helper import get_auth_token


class IsDeviceAuthenticated(IsAuthenticated):

    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        if is_authenticated:
            user = get_current_user(request)
            token = get_auth_token(request)

            return True

        return False
