from django.shortcuts import render, redirect
from .models import Transaction, Portfolio, Coin
from .forms import RegistrationForm, AddTransactionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
import json,requests
# Create your views here. portfolio\aladdin\static\js\demo\chart-area-demo.js

def index(request):
	# Main page here.
	context = {}
	return render(request, 'aladdin/index.html', context)

@login_required
def test(request):
	# Grab Crypto Price Data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
	price = json.loads(price_request.content)
	portfolio_query = Portfolio.objects.filter(user=request.user) # for total portfolio value
	filtered_transaction_query_by_user = Transaction.objects.filter(portfolio__user=request.user) # for each transactions

	
	return render(request, 'aladdin/test.html', {'price': price, 'portfolio': portfolio_query,})

@login_required	
def get_data(request):
	filtered_transaction_query_by_user = Transaction.objects.filter(portfolio__user=request.user)
	total_transactions_by_user =  filtered_transaction_query_by_user.values('coin__name').annotate( total = (Sum('trade_price') * Sum('number_of_coins'))).order_by('-total')
	data = list(total_transactions_by_user)
	return JsonResponse(data,safe=False)




@login_required
def table_total_portfolio_value(request):
	# Table Total Portoflio Value.
	filtered_transaction_query_by_user = Transaction.objects.filter(portfolio__user=request.user)
	total_transactions_by_user =  filtered_transaction_query_by_user.values('coin__name').annotate( total = (Sum('trade_price' ) * Sum('number_of_coins'))).order_by('-total')
	portfolio_query = Portfolio.objects.filter(user=request.user)
	context = {'total_transactions':total_transactions_by_user,'portfolio': portfolio_query,}
	return render(request, 'aladdin/table_total_portfolio_value.html', context)

@login_required
def table_previous_transactions(request):
	# Table Total Portoflio Value.
	filtered_transaction_query_by_user = Transaction.objects.filter(portfolio__user=request.user)
	context = {'transactions': filtered_transaction_query_by_user,}
	return render(request, 'aladdin/table_previous_transactions.html', context)

def register(request):
    if request.method == 'POST':
        f = RegistrationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('index')

    else:
        f = RegistrationForm()

    return render(request, 'registration/register.html', {'form': f})


@login_required
def my_portfolio(request):
	filtered_transaction_query_by_user = Transaction.objects.filter(portfolio__user=request.user)
	total_transactions_by_user =  filtered_transaction_query_by_user.values('coin__name').annotate( total = (Sum('trade_price' ) * Sum('number_of_coins') ) ).order_by('-total')
	portfolio_query = Portfolio.objects.filter(user=request.user)

	context = {'total_transactions':total_transactions_by_user,'portfolio': portfolio_query,}
	return render(request, 'aladdin/dashboard.html', context)


@login_required	
# Old depreciated, might be useful in future.
def add_trade(request):
	if request.method == 'POST':
		f = AddTransactionForm(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request, 'Trade created successfully')
			return redirect('index')

	else:
		f = AddTransactionForm()

	return render(request, 'aladdin/add_trade.html', {'form': f})

