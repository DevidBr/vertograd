from django import template
from blog.models import Category
from django.db.models import Count, Q

register = template.Library()


@register.simple_tag()
def get_categories():
    categories = Category.objects.annotate(total_articles=Count(
        'articles', filter=Q(articles__published=True)))\
        .filter(total_articles__gt=0)
    return categories