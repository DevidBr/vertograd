from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from education.models import Training
from education.forms import TrainingOrderForm
from education.tasks import training_order_processing


def education_main_page(request):
    trainings = Training.objects.filter(published=True)
    return render(request, 'education/education-main.html',
                  {'trainings': trainings})


def training_detail(request, training_slug):
    training = get_object_or_404(Training, slug=training_slug)
    training_order_form = TrainingOrderForm(
        initial={'training_name': training.name}
    )
    return render(request, 'education/training_detail.html',
                  {'training': training,
                   'training_order_form': training_order_form})


class TrainingOrderView(View):
    def post(self, request):
        form = TrainingOrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            training_order_processing.delay(cd)
            return JsonResponse(
                data=
                {'success': 'Спасибо! Мы свяжемся с Вами в ближайшее время.'},
                status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse(data={'error': errors}, status=400)
