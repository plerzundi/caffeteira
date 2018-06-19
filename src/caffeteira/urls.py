from django.contrib import admin
from django.urls import path, include



urlpatterns = [

    #path core
    path('', include('core.urls')),
    #url admin
    path('admin/', admin.site.urls),
]
