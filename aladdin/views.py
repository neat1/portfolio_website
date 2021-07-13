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
	context = {}
	return render(request, 'aladdin/home2.html', context)

@login_required
def userpage(request):
	context = {}
	return render(request, 'aladdin/home.html', context)

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
def upload(request):
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		fs.save(uploaded_file.name, uploaded_file)
	return render(request, 'aladdin/upload.html')


@login_required
def my_portfolio(request):
	filtered_transaction_query_by_user = Transaction.objects.filter(portfolio__user=request.user)
	total_transactions_by_user =  filtered_transaction_query_by_user.values('coin__name').annotate( total = (Sum('trade_price' ) * Sum('number_of_coins'))).order_by('-total')
	portfolio_query = Portfolio.objects.filter(user=request.user)
	context = {'total_transactions':total_transactions_by_user,'portfolio': portfolio_query,}
	return render(request, 'aladdin/your_portfolio.html', context)


@login_required	
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
def add_trades_manually(request):
	results=Transaction
	return render(request, 'aladdin/add_trades_manually.html')


	
class CoinListView(generic.ListView):
    model = Coin
    queryset = Coin.objects.all() # Get 5 books containing the title war
    template_name = 'aladdin/coin_list.html'  # Specify your own template name/location

@login_required
def all_transactions_page(request): 
	filtered_transaction_query_by_user = Transaction.objects.filter(portfolio__user=request.user)
	paginator = Paginator(filtered_transaction_query_by_user, 8)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'transactions': filtered_transaction_query_by_user,}
	return render(request, 'aladdin/transaction_list.html', {'transactions': page_obj})