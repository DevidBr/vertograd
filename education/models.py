from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Training(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название курса',
                            unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='education/images/',
                              verbose_name='Картинка для карточки')
    short_description = models.TextField(
        verbose_name='Краткое описание курса (для карточки)')
    description = models.TextField(verbose_name='Подробное описание курса')
    start_date = models.CharField(max_length=30,
                                  verbose_name='Начало обучения')
    duration = models.CharField(max_length=30,
                                verbose_name='Длительность курса')
    form_of_education = models.CharField(max_length=30,
                                         verbose_name='Форма обучения')
    document = models.CharField(max_length=50,
                                verbose_name='Документ об окончании')
    column_1_title = models.CharField(max_length=250,
                                      verbose_name='Заголовок левой колонки')
    description_column_1 = models.TextField(
        verbose_name='Текст левой колонки')
    column_2_title = models.CharField(max_length=250,
                                      verbose_name='Заголовок правой колонки')
    description_column_2 = models.TextField(
        verbose_name='Текст правой колонки')
    separator_text = models.CharField(max_length=200,
                                      verbose_name=
                                      'Разделительная строка над блоками')
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                verbose_name='Стоимость')
    published = models.BooleanField(default=False, verbose_name='Опубликовано')
    rate = models.IntegerField(default=0, verbose_name='Рейтинг')
    meta_description = models.CharField(max_length=200,
                                        verbose_name='meta description',
                                        default='вписать meta description')
    title = models.CharField(max_length=200, verbose_name='title для страницы')

    class Meta:
        verbose_name = 'Курс обучения'
        verbose_name_plural = 'Курсы обучения'
        ordering = ['-rate', '-pk']

    def get_absolute_url(self):
        return reverse('education:training_detail', args=(self.slug,))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class TrainingBlock(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок блока')
    block = models.TextField(verbose_name='блок')
    training = models.ForeignKey(Training, on_delete=models.CASCADE,
                                 related_name='block_set')

    def __str__(self):
        return f'Блок курса {self.training}'
