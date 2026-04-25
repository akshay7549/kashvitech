from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 🔐 Admin Panel
    path('admin/', admin.site.urls),

    # 🌐 Main Website (Home, About, Landing pages)
    path('', include('apps.main.urls')),

    # 🛠 Services
    path('services/', include('apps.services.urls')),

    # 📩 Contact
    path('contact/', include('apps.contact.urls')),

]