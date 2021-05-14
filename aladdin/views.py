from django.shortcuts import render, redirect
from .models import Transaction, Portfolio, Coin
from django.views import generic
from .forms import RegistrationForm, AddTransactionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
def my_portfolio(request):
	filtered = Transaction.objects.filter(portfolio__user=request.user)
	context = {'transactions': filtered,}
	return render(request, 'aladdin/page_for_user.html', context)

@login_required	
def add_trade(request):
	if request.method == 'POST':
		f = AddTransactionForm(request.POST, initial={"number_of_coins": 10})
		if f.is_valid():
			f.save(commit=False)
			
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
