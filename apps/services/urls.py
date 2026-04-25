from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    # 🔹 Services List Page
    path('', views.services_view, name='services'),

    # 🔹 Service Detail Page (IMPORTANT)
    path('<slug:slug>/', views.service_detail, name='service_detail'),
]