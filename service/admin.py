from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from service.models import Service, ServiceCategory


class ServiceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(),
                                  label='Подробное описание услуги')

    class Meta:
        model = Service
        fields = ['name', 'description', 'image',
                  'category', 'price', 'published']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ['id', 'name', 'category', 'price', 'published']
    list_display_links = ['id', 'name']
    list_editable = ['published', ]
    list_filter = ['category']


class ServiceCategoryAdminForm(forms.ModelForm):
    description_column_1 = forms.CharField(widget=CKEditorUploadingWidget(),
                                           label=
                                           'Описание категории услуг '
                                           '- левая колонка')
    description_column_2 = forms.CharField(widget=CKEditorUploadingWidget(),
                                           label=
                                           'Описание категории услуг '
                                           '- правая колонка')
    meta_description = forms.CharField(label='meta description',
                                       widget=forms.Textarea(attrs={
                                           'placeholder': 'Должен содержать '
                                                          'понятное описание '
                                                          'того, что мы '
                                                          'предлагаем этой '
                                                          'услугой конкретно! '
                                                          'Очень важно для '
                                                          'поисковиков!',
                                           'style': 'border: 1px solid red;'}))
    title = forms.CharField(label='title для поисковиков',
                            widget=forms.Textarea(attrs={
                                'placeholder': 'Должен быть похож на '
                                               'человеческий запрос, '
                                               'например: '
                                               '"Озеленить офис в москве".'
                                               'Очень важен для поисковиков '
                                               'и выступает заголовком в '
                                               'выдаче запросов яндекс и '
                                               'прочих.',
                                'style': 'border: 1px solid red;'}))

    class Meta:
        model = ServiceCategory
        fields = ['name', 'short_description', 'meta_description',
                  'title', 'image',
                  'column_1_title',
                  'description_column_1',
                  'column_2_title',
                  'description_column_2']


@admin.register(ServiceCategory)
class AdminServiceCategory(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name']
    form = ServiceCategoryAdminForm
