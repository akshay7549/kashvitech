from django.urls import path
from .views import contact_view

app_name = "contact"

urlpatterns = [
    # 📩 Contact Page
    path('', contact_view, name='contact'),

    # 🔮 Future-ready routes (optional but recommended)
    #path('success/', contact_success, name='success'),
]