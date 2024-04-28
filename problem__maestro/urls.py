from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("dashboard/", include("dashboard.urls")),
    path("users/", include("users.urls")),
    path("course/", include("course.urls")),
    path("admin/", admin.site.urls),
]
