from django.contrib import admin
from .models import Portfolio, Coin, Transaction
# Register your models here.




class CoinAdmin(admin.ModelAdmin):
    list_display = ('name','portfolio','number_bought')

admin.site.register(Coin, CoinAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('stock','number_of_coins','trade_price','date','total_trade_value',)

admin.site.register(Transaction, TransactionAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'nos')

admin.site.register(Portfolio, PortfolioAdmin)



