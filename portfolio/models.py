from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название проекта',
                            unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=500,
                                   verbose_name='Текст')
    image = models.ImageField(upload_to=f'portfolio/main_photos/',
                              verbose_name='Фото для карточки')
    bottom_photo = models.ImageField(upload_to=
                                     f'portfolio/bottom_photos/',
                                     verbose_name='Нижнее фото')
    published = models.BooleanField(default=False, verbose_name='Опубликовано')

    meta_description = models.CharField(max_length=200,
                                        verbose_name='meta description',
                                        default='вписать meta description')

    class Meta:
        verbose_name = 'Пример выполненной работы'
        verbose_name_plural = 'Примеры выполненных работ'

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_detail', args=[self.slug, ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                verbose_name='Фотография для галереи',
                                related_name='photo_set')
    photo = models.ImageField(upload_to=
                              f'portfolio/gallery_photos/')
