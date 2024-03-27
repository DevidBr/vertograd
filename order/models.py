from django.db import models
from django.urls import reverse


class Order(models.Model):
    type_of_application = models.CharField(max_length=200,
                                           verbose_name='Вид заявки')
    exactly_name_application = models.CharField(max_length=200,
                                                verbose_name='Конкретно на '
                                                             'что заявка')
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.ImageField(verbose_name='email')
    question = models.TextField(verbose_name="Комментарии посетителя")
    date = models.DateTimeField(auto_now=True, verbose_name="Когда получено")
    status = models.BooleanField(default=False, verbose_name='Обработано')
    relevant = models.BooleanField(default=True, verbose_name='Актуально')
    comment = models.TextField(default='Мои комментарии',
                               verbose_name='Мои комментарии')

    class Meta:
        verbose_name = 'Заявка от клиента'
        verbose_name_plural = 'Заявки от клиентов'

        ordering = ['-pk']

    def __str__(self):
        return f'{self.type_of_application} от {self.name}'

    def get_absolute_url(self):
        return reverse('order:order_detail', args=[self.pk])

