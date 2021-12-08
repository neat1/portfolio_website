from django.urls import path
from . import views
#haha
urlpatterns = [
    path('', views.index, name='index'),
    path('my_portfolio/', views.my_portfolio, name='my_portfolio'),
    path('register/', views.register, name='register'),
    path('table_total_portfolio_value/', views.table_total_portfolio_value, name ='table_total_portfolio_value'),
    path('table_previous_transactions/', views.table_previous_transactions, name ='table_previous_transactions'),
    path('test/', views.test, name ='test'),
    path('get_data/', views.get_data, name ='get_data'),
]