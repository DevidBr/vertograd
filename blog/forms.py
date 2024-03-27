from django import forms


class GetConsultationForm(forms.Form):
    name = forms.CharField(label='Имя*', widget=forms.TextInput(
        attrs={'class': 'form-control mb-3',
               'placeholder': 'Имя'}))
    phone = forms.CharField(label='Телефон*', widget=forms.TextInput(
        attrs={'class': 'phone form-control mb-3',
               'type': 'tel',
               'placeholder': '+7 (999) 999-99-99'}))
    email = forms.EmailField(label='email', required=False,
                             widget=forms.EmailInput(
                              attrs={'class': 'form-control mb-3',
                                     'placeholder': 'Ваш email'}))
    question = forms.CharField(label='Сообщение*', widget=forms.Textarea(
        attrs={'class': 'form-control',
               'rows': 8,
               'placeholder': 'Введите текст сообщения'}))

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) != 18:
            raise forms.ValidationError('Некорректный номер телефона.')
        return phone