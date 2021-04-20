from django.contrib import admin
from .models import Trade, Portfolio, Security
# Register your models here.

class SecurityAdmin(admin.ModelAdmin):
    list_display = ('cutip','ticker','name',)

admin.site.register(Security, SecurityAdmin)

class TradeAdmin(admin.ModelAdmin):
    list_display = ('trade_id','cutip','number_of_coins','trade_price','total_trade_value', 'date', 'portfolio_id')

admin.site.register(Trade, TradeAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('portfolio_id','name','total_porfolio_value','total_coin_value')

admin.site.register(Portfolio, PortfolioAdmin)



