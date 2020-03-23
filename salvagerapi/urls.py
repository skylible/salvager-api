from django.contrib import admin
from django.urls import path, re_path, include
urlpatterns = [
    re_path('api/(?P<version>(v1|v2))/', include('salvager.urls')),
    path('admin/', admin.site.urls),
]
