from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from website.models import Pharmacie

# Create your views here.
def home(request):
	return render(request, 'website/base.html')
	
def pharmacies(request):
	pharmacie = Pharmacie.objects.all()
	return render(request, 'website/pharmacies.html', {'RX': pharmacie})
	
	
