from django.urls import path
from . import views

urlpatterns=[
	path('dash_board/', views.dash_board),
    path('register_driver/', views.register_driver),
]