from django.core.mail import send_mail


def send(name, phone, question, email, training_name):
    send_mail(f"Заказ обучения {training_name}",
              f'Поступила заявка с сайта на обучение:\n'
              f'\nНазвание курса: {training_name}\n'
              f'\nИмя: {name}\n'
              f'Телефон: {phone}\n'
              f'Email: {email}\n'
              f'\nКомментарии заказчика: {question}',
              'sitever-g@yandex.ru',
              ['sitever-g@yandex.ru'],
              fail_silently=False)