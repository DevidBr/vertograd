from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from service.tasks import service_order_processing
from service.models import ServiceCategory
from django.views.generic import ListView
from service.forms import OrderServiceForm


class ServiceList(ListView):
    template_name = 'service/service_list.html'
    context_object_name = 'services'
    model = ServiceCategory

    def get_queryset(self):
        return ServiceCategory.objects.annotate(total_services=
                                                Count('services',
                                                      filter=
                                                      Q(services__published=
                                                        True))).\
                                                filter(total_services__gt=0)


def service_category_detail(request, service_category_slug):
    service_category = get_object_or_404(ServiceCategory,
                                         slug=service_category_slug)
    services = service_category.services.filter(published=True)
    order_form = OrderServiceForm(
        initial={'service_name': service_category.name})
    return render(request, 'service/service_detail.html', {
        'service_category': service_category,
        'services': services,
        'order_form': order_form
    })


class OrderServiceView(View):
    def post(self, request):
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            service_order_processing.delay(cd)
            return JsonResponse(
                data=
                {'success': 'Спасибо! Мы свяжемся с Вами в ближайшее время.'},
                status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse(data={'error': errors}, status=400)
