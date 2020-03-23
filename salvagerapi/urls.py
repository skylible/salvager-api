from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings

urlpatterns = [
    re_path('api/(?P<version>(v1|v2))/', include('salvager.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
