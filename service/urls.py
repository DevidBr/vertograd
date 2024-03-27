from django.urls import path
from service import views

app_name = 'service'

urlpatterns = [
    path('', views.ServiceList.as_view(), name='service_list'),
    path('<slug:service_category_slug>/', views.service_category_detail,
         name='service_category_detail'),
    path('order_service', views.OrderServiceView.as_view(),
         name='order_service')
]
