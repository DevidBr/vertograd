from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from portfolio.models import Project, ProjectPhoto
from django import forms


class ProjectPhotoInline(admin.StackedInline):
    model = ProjectPhoto
    verbose_name = 'Фотография для галереи'
    verbose_name_plural = 'Фотографии для галереи'
    extra = 1


class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(),
                                  label='Текст')

    class Meta:
        model = Project
        fields = ['name', 'description', 'meta_description',
                  'image', 'bottom_photo', 'published']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ['name', 'published']
    list_display_links = ['name']
    list_editable = ['published']
    inlines = [ProjectPhotoInline]



