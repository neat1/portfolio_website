from django.shortcuts import render
from .models import Transaction, Portfolio

# Create your views here.

def index(request):

	filtered = Transaction.objects.filter(portfolio_id = 2)

	'''all_transactions = Transaction.objects.all()'''
	one_transaction = Transaction.objects.get(pk=1)

	context = {'transactions': filtered,
	'one': one_transaction ,}
	return render(request, 'aladdin/home.html', context)
	