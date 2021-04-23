from django.shortcuts import render
from .models import Transaction

# Create your views here.

def index(request):
	
	all_transactions = Transaction.objects.all().filter(portfolio_id=1)
	one_transaction = Transaction.objects.get(pk=1)
	name = Transaction.objects.name
	context = {'transactions': all_transactions,
	'one': one_transaction }
	return render(request, 'aladdin/home.html', context)
	