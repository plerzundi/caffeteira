from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [

    # path core
    path('', include('core.urls')),
    # url admin
    path('admin/', admin.site.urls),
]

"""
Cargar archivos media modo debug
"""

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
