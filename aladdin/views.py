from django.shortcuts import render
from .models import Transaction, Portfolio, Coin

# Create your views here.

def index(request):

	filtered = Transaction.objects.filter(portfolio = 1)

	'''all_transactions = Transaction.objects.all()'''
	one_transaction = Transaction.objects.get(pk=1)

	all_coins = Coin.objects.first()
	for coin in all_coins:
		print(coin)
	teszt = b.transaction_set.all()
	


	context = {'transactions': filtered,
	'one': teszt ,}
	return render(request, 'aladdin/home.html', context)
	