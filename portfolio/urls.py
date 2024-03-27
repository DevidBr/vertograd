from django.urls import path
from portfolio.views import PortfolioListView, portfolio_detail_view


app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioListView.as_view(), name='portfolio_list'),
    path('<slug:project_slug>/', portfolio_detail_view,
         name='portfolio_detail')
]
