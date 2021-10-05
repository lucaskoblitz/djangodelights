from django.urls import path
from . import views
from django.views.generic import ListView

urlpatterns = [
	path('', views.home, name="home"),
	path('inventory/list', views.Inventory.as_view(), name='inventory')
]