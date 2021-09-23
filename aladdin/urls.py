from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_portfolio/', views.my_portfolio, name='my_portfolio'),
    path('register/', views.register, name='register'),
    path('trade/', views.add_trade, name='add_trade'),
    path('transactions/', views.all_transactions_page, name ='transactions'),
    path('add_trade_manually/', views.add_trades_manually, name ='add_trade_manually'),
    path('table_total_portfolio_value/', views.table_total_portfolio_value, name ='table_total_portfolio_value'),
    path('table_previous_transactions/', views.table_previous_transactions, name ='table_previous_transactions'),
    path('test/', views.test, name ='test'),
]