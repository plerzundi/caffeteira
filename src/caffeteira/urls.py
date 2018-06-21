from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [

    # path core
    path('', include('core.urls')),
    # path services
    path('services/', include('services.urls')),
    # path blog
    path('blog/', include('blog.urls')),
    # path pages
    path('page/', include('pages.urls')),
    # url admin
    path('admin/', admin.site.urls),
]

"""
Cargar archivos media modo debug
"""

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
