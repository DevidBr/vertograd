from order.models import Order


def order_create(type_of_application, exactly_name_application,
                 name, phone, question, email):
    Order.objects.create(
        type_of_application=type_of_application,
        exactly_name_application=exactly_name_application,
        name=name,
        phone=phone,
        question=question,
        email=email
    )
