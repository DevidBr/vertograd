"""vertograd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
# from django.views.static import serve as mediaserve
from blog.sitemaps import ArticleSitemap, CategorySitemap, \
    ServiceCategorySitemap, TrainingSitemap, StaticViewSitemap

sitemaps = {
    'posts': ArticleSitemap,
    'category': CategorySitemap,
    'uslugi': ServiceCategorySitemap,
    'obuchenie': TrainingSitemap,
    'static': StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('obuchenie/', include('education.urls', namespace='education')),
    path('my_orders/', include('order.urls', namespace='order')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('uslugi/', include('service.urls', namespace='service')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
