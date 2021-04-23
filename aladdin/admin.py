from django.contrib import admin
from .models import Portfolio, Coin, Transaction
# Register your models here.




class CoinAdmin(admin.ModelAdmin):
    list_display = ('cutip','ticker','name')

admin.site.register(Coin, CoinAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user','portfolio_id', 'name')

admin.site.register(Portfolio, PortfolioAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('trade_id','portfolio_id','cutip','number_of_coins','trade_price','date')

admin.site.register(Transaction, TransactionAdmin)





