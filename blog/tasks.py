from vertograd.celery import app
from blog.send_email_service import send
# from order.save_order_service import order_create


@app.task
def get_consultation_processing(cd):
    name = cd.get('name')
    phone = cd.get('phone')
    question = cd.get('question')
    email = cd.get('email')
    type_of_application = 'Бесплатная консультация'
    exactly_name_application = 'Бесплатная консультация'

    order_create(type_of_application=type_of_application,
                 exactly_name_application=exactly_name_application,
                 name=name, phone=phone, question=question, email=email)
    # send(name=name, phone=phone, question=question, email=email)