from django.core.mail import send_mail


def send(name, phone, question, email):
    send_mail(f"Заявка с сайта от {name}",
              f'Поступила заявка с сайта на бесплатную консультацию:\n'
              f'\nИмя: {name}\n'
              f'Телефон: {phone}\n'
              f'email: {email}\n'
              f'\nТекст вопроса: {question}',
              'sitever-g@yandex.ru',
              ['sitever-g@yandex.ru'],
              fail_silently=False)