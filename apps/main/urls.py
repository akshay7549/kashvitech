from django.urls import path, include
from . import views

app_name = "main"  # ✅ optional but recommended

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # ✅ Include other apps
    path('contact/', include('apps.contact.urls')),
    path('services/', include('apps.services.urls')),
]