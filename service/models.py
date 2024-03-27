from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class ServiceCategory(models.Model):
    name = models.CharField(max_length=250, verbose_name='Категория услуг',
                            unique=True)
    short_description = models.CharField(max_length=250,
                                         verbose_name=
                                         'Краткое описание для карточки',
                                         blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='services/images/',
                              verbose_name='Изображение', blank=True,
                              null=True)
    column_1_title = models.CharField(max_length=250,
                                      verbose_name='Заголовок левой колонки')
    description_column_1 = models.TextField(
        verbose_name='Описание категории услуг - левая колонка')
    column_2_title = models.CharField(max_length=250,
                                      verbose_name='Заголовок правой колонки')
    description_column_2 = models.TextField(
        verbose_name='Описание категории услуг - правая колонка')

    meta_description = models.CharField(max_length=200,
                                        verbose_name='meta description',
                                        default='вписать meta description')
    title = models.CharField(max_length=200, verbose_name='title для страницы')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service:service_category_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуг'


class ServicePublishedManger(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(
            published=True
        )


class Service(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название услуги')
    slug = models.SlugField(max_length=250)
    description = models.TextField(verbose_name='Подробное описание услуги')
    image = models.ImageField(upload_to='service/images/%Y/%m/%d/',
                              verbose_name="Изображение для услуги")
    category = models.ForeignKey(to=ServiceCategory, on_delete=models.CASCADE,
                                 verbose_name='Категория услуги',
                                 related_name='services',
                                 null=True, blank=True)
    published = models.BooleanField(default=False, verbose_name='Опубликовано')
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True,
                                null=True, verbose_name='Стоимость')

    objects = models.Manager()
    is_published = ServicePublishedManger()

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service:service_detail', args=[self.slug])


class OrderForService(models.Model):
    service_name = models.CharField(max_length=50,
                                    verbose_name='Категория услуги')
    name = models.CharField(verbose_name='Имя заказчика', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=18)
    question = models.TextField(verbose_name='Комментарий заказчика',
                                blank=True)
    comment = models.TextField(verbose_name='Мои комментарии')
    status = models.BooleanField(default=False, verbose_name='Обработано')

    class Meta:
        verbose_name = 'Заказ услуги'
        verbose_name_plural = 'Заказы услуг'

    def __str__(self):
        return f'Заказ №{self.id}. Категория услуги: {self.service_name}'
