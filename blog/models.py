from django.db import models
from django.urls import reverse
from django.utils import timezone
from pytils.translit import slugify


tz = timezone.get_default_timezone()


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название",
                            unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Категория статей'
        verbose_name_plural = 'Категории статей'

    def get_articles_count(self):
        return self.articles.all().count()

    get_articles_count.short_description = 'Всего статей'

    def get_published_articles(self):
        return self.articles.filter(published=True).count()

    get_published_articles.short_description = 'Опубликованных'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:articles_list_by_category',
                       args=[self.slug, ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            published=True)


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок",
                             unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                              verbose_name="Изображение для карточки")
    preview = models.TextField(verbose_name='Описание статьи')
    body = models.TextField(verbose_name="Текст")
    author = models.CharField(max_length=150, verbose_name="Автор")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE,
                                 related_name='articles',
                                 verbose_name="Категория")
    published = models.BooleanField(default=False, verbose_name="Опубликовано")

    objects = models.Manager()
    is_published = PublishedManager()

    def get_created(self):
        return self.created.astimezone(tz).strftime('%d.%m.%Y %H:%M')

    get_created.short_description = 'Создано'

    def get_updated(self):
        return self.created.astimezone(tz).strftime('%d.%m.%Y %H:%M')

    get_updated.short_description = 'Обновлено'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-updated']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.slug, ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
