from django import forms

from order.models import Order


class OrderChangeForm(forms.Form):
    status_choices = [
        (False, 'Не обработано'),
        (True, 'Обработано')
    ]
    relevant_choices = [
        (False, 'Неактуально'),
        (True, 'Актуально')
    ]

    order_pk = forms.IntegerField(widget=forms.HiddenInput())
    comment = forms.CharField(label='Мои заметки',
                              widget=forms.Textarea
                              (attrs={'class': 'form-control'}))
    status = forms.ChoiceField(label='Статус заявки',
                               choices=status_choices, widget=forms.Select(
            attrs={'class': 'form-control'}))

    relevant = forms.ChoiceField(label='Актуальность заявки',
                                 choices=relevant_choices, widget=forms.Select(
            attrs={'class': 'form-control',
                   'style': "width: 40%"}))


class OrderCreateForm(forms.ModelForm):
    type_of_application_choices = [
        ('Услуга', 'Услуга'),
        ('Обучение', 'Обучение')
    ]

    type_of_application = forms.ChoiceField(
        choices=type_of_application_choices,
        label='Вид заявки',
        widget=forms.Select(attrs={'class': 'form-control'}))
    exactly_name_application = forms.CharField(
        label='Продукт',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'на что конкретно заявка'})

    )
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'имя заказчика'}))

    phone = forms.CharField(
        label='Телефон', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'телефон заказчика'}))

    email = forms.EmailField(
        label='email', required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'email заказчика'})
    )

    comment = forms.CharField(
        label='Мои заметки',
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Комментарии'}))

    class Meta:
        model = Order
        fields = ['type_of_application', 'exactly_name_application', 'name',
                  'phone', 'email', 'comment']


class OrderRelevantFilterForm(forms.Form):
    status_filter_choices = [
        (False, 'Неактуально'),
        (True, 'Актуально')
    ]
    filter_relevant_arg = forms.ChoiceField(
        choices=status_filter_choices,
        widget=forms.Select(
         attrs={'class': 'form-control'}))


class OrderStatusFilterForm(forms.Form):
    status_filter_choices = [
        (False, 'Свежие заявки'),
        (True, 'Обработанные заявки')
    ]
    filter_status_arg = forms.ChoiceField(
        choices=status_filter_choices,
        widget=forms.Select(
         attrs={'class': 'form-control'}))


class SearchOrderByPkForm(forms.Form):
    search_pk = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control',
                   'placeholder': 'номер заявки'}
        )
    )
