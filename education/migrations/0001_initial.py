# Generated by Django 4.1 on 2024-03-19 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Название курса')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('image', models.ImageField(upload_to='education/images/', verbose_name='Картинка для карточки')),
                ('short_description', models.TextField(verbose_name='Краткое описание курса (для карточки)')),
                ('description', models.TextField(verbose_name='Подробное описание курса')),
                ('start_date', models.CharField(max_length=30, verbose_name='Начало обучения')),
                ('duration', models.CharField(max_length=30, verbose_name='Длительность курса')),
                ('form_of_education', models.CharField(max_length=30, verbose_name='Форма обучения')),
                ('document', models.CharField(max_length=50, verbose_name='Документ об окончании')),
                ('column_1_title', models.CharField(max_length=250, verbose_name='Заголовок левой колонки')),
                ('description_column_1', models.TextField(verbose_name='Текст левой колонки')),
                ('column_2_title', models.CharField(max_length=250, verbose_name='Заголовок правой колонки')),
                ('description_column_2', models.TextField(verbose_name='Текст правой колонки')),
                ('separator_text', models.CharField(max_length=200, verbose_name='Разделительная строка над блоками')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('rate', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('meta_description', models.CharField(default='вписать meta description', max_length=200, verbose_name='meta description')),
                ('title', models.CharField(max_length=200, verbose_name='title для страницы')),
            ],
            options={
                'verbose_name': 'Курс обучения',
                'verbose_name_plural': 'Курсы обучения',
                'ordering': ['-rate', '-pk'],
            },
        ),
        migrations.CreateModel(
            name='TrainingBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заголовок блока')),
                ('block', models.TextField(verbose_name='блок')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block_set', to='education.training')),
            ],
        ),
    ]
