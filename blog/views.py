from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from blog.models import Article, Category
from django.http import JsonResponse
from blog.forms import GetConsultationForm
from blog.tasks import get_consultation_processing


def index_page(request):
    articles = Article.objects.filter(published=True).prefetch_related(
        'category')[:3]
    return render(request, 'blog/index.html', {'articles': articles})


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/articles_list.html'
    paginate_by = 6

    def get_queryset(self):
        if self.kwargs.get('category_slug'):
            category = get_object_or_404(Category,
                                         slug=self.kwargs['category_slug'])
            return Article.is_published.filter(category=category)
        else:
            return Article.is_published.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('category_slug'):
            category = get_object_or_404(Category,
                                         slug=self.kwargs['category_slug'])
            context['category'] = category
            context['title'] = f"Статьи на тему: {category.name}"
        else:
            context['title'] = "Все статьи"
        return context


def article_detail(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    category = article.category
    similar_articles = \
        Article.objects.filter(category=category).exclude(pk=article.pk)[:3]
    return render(request,
                  'blog/article_detail.html',
                  {
                      'article': article,
                      'similar_articles': similar_articles
                  })


@require_POST
def get_consultation_view(request):
    form = GetConsultationForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        get_consultation_processing.delay(cd=cd)
        return JsonResponse(
            data=
            {'success': 'Спасибо! Мы свяжемся с Вами в ближайшее время.'},
            status=200)
    else:
        errors = form.errors.as_json()
        return JsonResponse(data={'error': errors}, status=400)


def about_us_page(request):
    return render(request, 'blog/about_us.html')


def contacts_page_view(request):
    return render(request, 'blog/contacts.html')


def policy_page_view(request):
    return render(request, 'blog/politica.html')


def oferta_page_view(request):
    return render(request, 'blog/oferta.html')
