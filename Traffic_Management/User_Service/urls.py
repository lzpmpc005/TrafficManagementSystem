from django.urls import path
from . import views

urlpatterns=[
	path('User_Service/register_driver/', views.register_driver),
    path('User_Service/register_vehicle/', views.register_vehicle),
]