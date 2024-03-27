from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from education.models import Training, TrainingBlock


class TrainingBlockInlineForm(forms.ModelForm):
    block = forms.CharField(widget=CKEditorUploadingWidget(), label='Блок')

    class Meta:
        fields = ['title', 'block']


class TrainingBlockInline(admin.StackedInline):
    model = TrainingBlock
    form = TrainingBlockInlineForm
    verbose_name = 'Блок обучения'
    verbose_name_plural = 'Блоки обучения'
    extra = 1


class TrainingAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(),
                                  label='Подробное описание курса')
    description_column_1 = forms.CharField(widget=CKEditorUploadingWidget(),
                                           label='Текст левой колонки')
    description_column_2 = forms.CharField(widget=CKEditorUploadingWidget(),
                                           label='Текст правой колонки')
    rate = forms.IntegerField(label='Рейтинг (по-умолчанию равен 0).'
                                    'Чем выше рейтинг, тем ближе к'
                                    'началу списка карточка с этим'
                                    'курсом.')

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
                                'style': 'border: 1px '
                                         'solid red;'}))

    class Meta:
        model = Training
        fields = ['name', 'image', 'short_description', 'meta_description', 'title',
                  'description', 'start_date', 'duration',
                  'form_of_education', 'document',
                  'column_1_title', 'description_column_1',
                  'column_2_title', 'description_column_2',
                  'separator_text', 'price', 'published']


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['name', 'form_of_education',
                    'price', 'start_date', 'rate', 'published']
    list_display_links = ['name', 'form_of_education']
    list_editable = ['published']
    inlines = [TrainingBlockInline]
    form = TrainingAdminForm

    fieldsets = (
        (None, {
            'fields': ('name', 'image', 'meta_description',
                       'title', 'short_description', 'description',
                       ('published', 'rate'))
        }),
        ('Дата начала, продолжительность, форма обучения, '
         'выдаваемый документ, стоимость',
         {
             'fields': ('start_date', 'duration',
                        'form_of_education', 'document', 'price')
         }),
        ('Колонки',
         {
             'fields': ('column_1_title', 'description_column_1',
                        'column_2_title', 'description_column_2')
         }),
        ('Разделительный текст между колонками и блоками',
         {
             'fields': ('separator_text',)
         })
    )

