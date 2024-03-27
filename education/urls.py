from django.urls import path
from education import views

app_name = 'education'

urlpatterns = [
    path('', views.education_main_page, name='education_main'),
    path('<slug:training_slug>/', views.training_detail, name='training_detail'),
    path('training_order', views.TrainingOrderView.as_view(),
         name='training_order')
]