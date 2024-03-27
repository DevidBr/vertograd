from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('', views.MyOrdersView.as_view(), name='my_orders'),
    path('<int:order_id>/', views.order_detail_view, name='order_detail'),
    path('order_change/', views.order_change_view, name='order_change_save'),
    path('order_delete_confirm/<int:order_pk>/', views.order_delete_confirm,
         name='order_delete_confirm'),
    path('order_final_delete/<int:order_pk>', views.order_delete_view,
         name='order_final_delete'),
    path('create_order/', views.order_create_page_view,
         name='order_create_page'),
    path('staff_logout/', views.staff_logout, name='staff_logout')
]
