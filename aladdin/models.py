from django.db import models
from django.db.models import Avg, Count, Sum
from django.contrib.auth.models import User

# Create your models here.
class Coin(models.Model):
    """Model representing an individial security"""
    cutip = models.IntegerField(primary_key=True, unique=True, editable=False)
    ticker = models.CharField(max_length=200, unique=True, help_text='Look up the ticker manually now')
    name = models.CharField(max_length=200, help_text='Enter a cryptocurrency name (e.g. Bitcoin)')

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Portfolio(models.Model):
    """Model representing an individial portfolio."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    portfolio_id = models.IntegerField(primary_key=True, unique=True,auto_created=True,editable=False,)
    name = models.CharField(max_length=200, help_text='Enter a portfolio name (e.g. Andras portfolio')

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    """maybe useful later"""
    @property
    def average_trade_price(self):
        return Transaction.objects.all()
        """is the same as self.transaction_set.all()"""

        """here below is the average trade price method"""
        """.aggregate(Avg('trade_price'))"""
    
    """maybe useful later"""
    @property
    def number_of_distinct_cutips(self):
        return Trade.objects.all().aggregate(Count('cutip',distinct=True))

    @property
    def just_cusips(self):
        return [transaction.cutip for transaction in self.transaction_set.all()]
        """return self.transaction_set.all().filter(cutip = 3)"""

    @property
    def just_doge_coin(self):
        return sum([transaction.total_trade_value for transaction in self.transaction_set.all().filter(cutip = 3)])
        """return self.transaction_set.all().filter(cutip = 3)"""

    @property
    def total_porfolio_value(self):
        return sum([transaction.total_trade_value for transaction in self.transaction_set.all()])

    @property
    def total_coin_value(self):
        return ([transaction.total_trade_value for transaction in self.transaction_set.all().filter(portfolio_id=1)])
        
    @property
    def number_bought(Self):
        return Transaction.objects.all().aggregate(Count('number_of_coins',distinct=True))

class Transaction(models.Model):
    """Model representing a Cryptocurrency."""
    trade_id = models.IntegerField(primary_key=True, unique=True,auto_created=True,editable=False,)
    portfolio_id = models.ForeignKey('Portfolio',on_delete=models.CASCADE)
    cutip = models.ForeignKey(Coin,on_delete=models.CASCADE)
    number_of_coins = models.DecimalField(max_digits=10, decimal_places=0)
    trade_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return str(self.trade_id)   

    @property
    def total_trade_value(self):
        return self.trade_price * self.number_of_coins

    @property
    def show_ticker(self):
        return Coin.cutip
    """def show_ticker(self):
        return [valami.ticker for valami in Coin.objects.all()]"""
        


    
   
