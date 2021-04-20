from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
	all_cusip = Trade.objects.all()
	one_cusip = Trade.objects.get(pk=1)
	name = Trade.objects.name
	context = {'cusipok': all_cusip,
	'one': one_cusip }
	return render(request, 'aladdin/home.html', context)
	