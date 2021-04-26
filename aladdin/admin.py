from django.contrib import admin
from .models import Portfolio, Coin, Transaction, PortfolioView
# Register your models here.




class CoinAdmin(admin.ModelAdmin):
    list_display = ('id','ticker','name')

admin.site.register(Coin, CoinAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'name','total_portfolio_value',)
   
admin.site.register(Portfolio, PortfolioAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id','coin','number_of_coins','trade_price','total_trade_value','date','portfolio','transaction_ticker',)

admin.site.register(Transaction, TransactionAdmin)

class PortfolioViewAdmin(admin.ModelAdmin):
    list_display = ('coin','portfolio','distinct_coin')
   
admin.site.register(PortfolioView, PortfolioViewAdmin)


