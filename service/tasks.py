from vertograd.celery import app
from order.save_order_service import order_create
from service.service_send_email_service import send


@app.task
def service_order_processing(cd):
    name = cd.get('name')
    phone = cd.get('phone')
    email = cd.get('email')
    question = cd.get('question')
    service_name = cd.get('service_name')
    order_create(type_of_application='Услуга',
                 exactly_name_application=service_name,
                 name=name, phone=phone, question=question, email=email)
    # send(name, phone, question, email, service_name)
