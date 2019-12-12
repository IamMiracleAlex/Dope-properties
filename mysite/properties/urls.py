from django.urls import path

from . import views

urlpatterns = [
    path('', views.properties, name='properties'),
    path('<int:property_id>/', views.property_, name='property'),
    path('search/', views.search, name='search')
]
