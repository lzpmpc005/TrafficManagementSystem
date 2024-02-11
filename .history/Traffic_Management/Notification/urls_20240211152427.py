from django.urls import path
from . import views

urlpatterns=[
    path('send_email/', views.send_email),
    path('send_congestion_warning/<str:formatted_date>/', views.send_congestion_warning),
]