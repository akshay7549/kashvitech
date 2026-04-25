from .models import ServiceCategory

def services_data(request):
    categories = ServiceCategory.objects.prefetch_related('services').all()
    return {'service_categories': categories}