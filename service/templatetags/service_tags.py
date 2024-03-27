from django import template
from service.models import Service, ServiceCategory
from django.db.models import Count, Q


register = template.Library()


@register.simple_tag()
def get_services():
    return Service.objects.filter(published=True)


@register.simple_tag()
def get_services_categories():
    return ServiceCategory.objects.annotate(
        total_services=Count('services', filter=Q(services__published=True)))\
        .filter(total_services__gt=0)