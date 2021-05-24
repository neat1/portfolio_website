from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_portfolio/', views.my_portfolio, name='my_portfolio'),
    path('coin/', views.CoinListView.as_view(), name='coin'),
    path('register/', views.register, name='register'),
    path('trade/', views.add_trade, name='add_trade'),
    path('upload/', views.upload, name ='upload'),

]