from django.contrib import admin
from .models import Portfolio, Coin, Transaction
# Register your models here.




class CoinAdmin(admin.ModelAdmin):
    list_display = ('cutip','ticker','name')

admin.site.register(Coin, CoinAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('portfolio_id','total_porfolio_value','user', 'name','average_trade_price','just_doge_coin','number_bought')
   
admin.site.register(Portfolio, PortfolioAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('trade_id','portfolio_id','cutip','number_of_coins','trade_price','date')

admin.site.register(Transaction, TransactionAdmin)




