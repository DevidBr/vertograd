from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_page, name='home'),
    path('blog/post/<slug:article_slug>/',
         views.article_detail, name='article_detail'),
    path('blog/category/<slug:category_slug>/',
         views.ArticleListView.as_view(), name='articles_list_by_category'),
    path('blog/', views.ArticleListView.as_view(), name='articles_list'),
    path('about_us/', views.about_us_page, name='about_us'),
    path('get_consultation/', views.get_consultation_view,
         name='get_consultation'),
    path('contacts/', views.contacts_page_view, name='contacts'),
    path('politica/', views.policy_page_view, name='policy'),
    path('oferta/', views.oferta_page_view, name='oferta'),
]