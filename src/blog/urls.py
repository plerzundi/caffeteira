from django.urls import path
from . import views

urlpatterns = [

    path('', views.blog, name="blog"),
    path('category/<int:categoy_id>/', views.category, name="category"),
]
