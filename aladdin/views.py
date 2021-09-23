from datetime import date
from django.shortcuts import render, redirect
from .models import Transaction, Portfolio, Coin
from django.views import generic
from .forms import RegistrationForm, AddTransactionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum
from django.core.paginator import Paginator


# Create your views here.

def index(request):
	# Main page here.
	context = {}
	return render(request, 'aladdin/index.html', context)

def test(request):
	# test querys.
	labels = []
	data = []

	filtered_transaction_query_by_user = Transaction.objects.filter(portfolio__user=request.user)
	total_transactions_by_user =  filtered_transaction_query_by_user.values('coin__name').annotate( total = (Sum('trade_price') * Sum('number_of_coins'))).order_by('-total')

	for each in total_transactions_by_user:
		labels.append(each["coin__name"])
		data.append(each["total"])

	portfolio_query = Portfolio.objects.filter(user=request.user)
		
	context = {'total_transactions':total_transactions_by_user, 'labels': labels, 'data': data,}
	return render(request, 'aladdin/pie_chart.html', context)


def table_total_portfolio_value(request):
	# Table Total Portoflio Value.
	filtered_transaction_query_by_user = Transaction.objects.filter(portfolio__user=request.user)
	total_transactions_by_user =  filtered_transaction_query_by_user.values('coin__name').annotate( total = (Sum('trade_price' ) * Sum('number_of_coins'))).order_by('-total')
	portfolio_query = Portfolio.objects.filter(user=request.user)
	context = {'total_transactions':total_transactions_by_user,'portfolio': portfolio_query,}
	return render(request, 'aladdin/table_total_portfolio_value.html', context)


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
	# Main Dashboard.
	labels = []
	data = []

	filtered_transaction_query_by_user = Transaction.objects.filter(portfolio__user=request.user)
	total_transactions_by_user =  filtered_transaction_query_by_user.values('coin__name').annotate( total = (Sum('trade_price' ) * Sum('number_of_coins'))).order_by('-total')	
	portfolio_query = Portfolio.objects.filter(user=request.user)
	for each in total_transactions_by_user:
		labels.append(each["coin__name"])
		data.append(each["total"])
	context = {'total_transactions':total_transactions_by_user,'portfolio': portfolio_query, 'labels': labels, 'data': data,}
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

@login_required
# Old depreciated, might be useful in future.
def add_trades_manually(request):
	results=Transaction
	return render(request, 'aladdin/add_trades_manually.html')


@login_required
def all_transactions_page(request): 
	# Old depreciated, might be useful in future.
	filtered_transaction_query_by_user = Transaction.objects.filter(portfolio__user=request.user)
	paginator = Paginator(filtered_transaction_query_by_user, 8)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'transactions': filtered_transaction_query_by_user,}
	return render(request, 'aladdin/transaction_list.html', {'transactions': page_obj})