from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Article, Category
from service.models import Service, ServiceCategory
from education.models import Training
from portfolio.models import Project


class ArticleSitemap(Sitemap):
    def items(self):
        return Article.objects.filter(published=True)


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()


class ServiceCategorySitemap(Sitemap):
    def items(self):
        return ServiceCategory.objects.all()


class TrainingSitemap(Sitemap):
    def items(self):
        return Training.objects.all()


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['blog:about_us', 'blog:contacts', 'blog:policy',
                'education:education_main', 'portfolio:portfolio_list', ]

    def location(self, item):
        return reverse(item)
