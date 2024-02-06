from django.urls import path
from . import views

urlpatterns=[
	path('register_driver/', views.register_driver),
    path('register_vehicle/', views.register_vehicle),
    path('process_junctions_log/<str:formatted_date>/', views.process_junctions_log),
    path('import_driver/', views.import_driver),
    path('import_plate/', views.import_plate),
    path('create_vehicles/', views.create_vehicles),
    path('process_violation_log/<str:formatted_date>/<str:violation_type>/', views.process_violation_log),
    path('generate_fine_log/<str:formatted_date>/<str:violation_type>/', views.generate_fine_log),
]