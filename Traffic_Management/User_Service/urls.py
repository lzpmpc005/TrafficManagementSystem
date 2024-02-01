from django.urls import path
from . import views

urlpatterns=[
	path('register_driver/', views.register_driver),
    path('register_vehicle/', views.register_vehicle),
    path('process_junctions_log/<str:formatted_date>/', views.process_junctions_log),
]