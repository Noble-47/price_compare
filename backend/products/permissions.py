from django.contrib.auth import get_user_model

from rest_framework.permissions import BasePermission

# this is redundant
# scrapper would have access to database directly
class AllowScrapper(BasePermission):
    "Allows access to only our Scrapper"

    def has_permission(self, request, view):
        # Scrapper = get_user_model().objects.get(email="scrapper@email.com")
        return True
        # return True if request.user == Scrapper else False
