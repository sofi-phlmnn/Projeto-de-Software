from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # CORE
    path("", include(("core.urls", "core"), namespace="core")),

    # AUTENTICAÇÃO
    path("accounts/", include(("usuario.urls", "usuario"), namespace="usuario")),
]

