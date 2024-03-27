from django import forms


class TrainingOrderForm(forms.Form):
    training_name = forms.CharField(widget=forms.HiddenInput())
    name = forms.CharField(label='Имя*', widget=forms.TextInput(
        attrs={'class': 'form-control mb-3',
               'placeholder': 'Имя'}))
    phone = forms.CharField(label='Телефон*', widget=forms.TextInput(
        attrs={'class': 'phone form-control mb-3',
               'type': 'tel',
               'placeholder': '+7 (999) 999-99-99'}))
    email = forms.EmailField(label='email*', widget=forms.EmailInput(
        attrs={'class': 'form-control mb-3',
               'placeholder': 'ваш email'}))
    question = forms.CharField(label='Комментарии',
                               required=False,
                               widget=forms.Textarea(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Комментарии',
                                       'rows': 8}))

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) != 18:
            raise forms.ValidationError('Некорректный номер телефона.')
        return phone
