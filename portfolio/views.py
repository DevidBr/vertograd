from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from portfolio.models import Project


class PortfolioListView(ListView):
    template_name = 'portfolio/portfolio_list.html'
    model = Project
    queryset = Project.objects.filter(published=True)
    paginate_by = 6
    context_object_name = 'projects'


def portfolio_detail_view(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render(request, 'portfolio/portfolio_detail.html',
                  {'project': project})

