from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("accounts/", include("django_registration.backends.activation.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("api/auth/", include("accounts.urls")),
    path("api/product/", include("products.urls")),
]
