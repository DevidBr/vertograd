from blog.forms import GetConsultationForm


def get_context_data(request):
    context = {
        'get_consultation_form': GetConsultationForm()
    }
    return context