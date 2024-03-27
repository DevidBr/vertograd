from vertograd.celery import app
# from order.save_order_service import order_create
from education.education_send_email_service import send


@app.task
def training_order_processing(cd):
    name = cd.get('name')
    phone = cd.get('phone')
    email = cd.get('email')
    question = cd.get('question')
    training_name = cd.get('training_name')
    order_create(type_of_application='Обучение',
                 exactly_name_application=training_name,
                 phone=phone, name=name, email=email,
                 question=question)
    # send(name, phone, question, email, training_name)