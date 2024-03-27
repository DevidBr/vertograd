from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from blog.models import Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_articles_count',
                    'get_published_articles']
    prepopulated_fields = {'slug': ['name']}


class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget(),
                           label='Текст статьи')

    class Meta:
        model = Article
        fields = ['title', 'image', 'preview',
                  'body', 'author', 'category']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'get_created', 'get_updated',
                    'author', 'published']
    list_editable = ['published']
    list_display_links = ['id', 'title']
    list_per_page = 10
    list_filter = ['category', 'published']
    form = ArticleAdminForm

    def make_published(self, request, queryset):
        queryset.update(published=True)

    make_published.short_description = "Опубликовать выбранные статьи"

    def make_not_published(self, request, queryset):
        queryset.update(published=False)

    make_not_published.short_description = 'Снять с публикации выбранные статьи'

    actions = [make_published, make_not_published]
