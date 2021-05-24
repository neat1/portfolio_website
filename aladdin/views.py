from django.db.models.lookups import Transform
from django.shortcuts import render, redirect
from .models import Transaction, Portfolio, Coin
from django.views import generic
from .forms import RegistrationForm, AddTransactionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum, Avg, Count

# Create your views here.

def index(request):
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
	portfolio_query = Portfolio.objects.filter(user=request.user)
	justbitcoinzero = filtered_transaction_query_by_user.filter(coin__ticker='BTC').first()
	justbitcoin = filtered_transaction_query_by_user.filter(coin__ticker='BTC').aggregate(Sum('number_of_coins'))
	test = filtered_transaction_query_by_user.values('coin__name').annotate(total = Sum('number_of_coins')).order_by('-total')

	order_list = Transaction.objects.all().extra(select={'result': 'trade_price * number_of_coins'})
		
	context = {'transactions': filtered_transaction_query_by_user, 'portfolio': portfolio_query,'test':order_list}
	return render(request, 'aladdin/page_for_user.html', context)

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

	
class CoinListView(generic.ListView):
    model = Coin
    queryset = Coin.objects.all() # Get 5 books containing the title war
    template_name = 'aladdin/coin_list.html'  # Specify your own template name/location
