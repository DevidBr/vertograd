from django.core.mail import send_mail


def send(name, phone, question, email, service_name):
    send_mail(f"Заказ услуги {service_name}",
              f'Поступила заявка с сайта на услугу:\n'
              f'\nКатегория услуги: {service_name}\n'
              f'\nИмя: {name}\n'
              f'Телефон: {phone}\n'
              f'email: {email}\n'
              f'\nТекст вопроса: {question}',
              'sitever-g@yandex.ru',
              ['sitever-g@yandex.ru'],
              fail_silently=False)

