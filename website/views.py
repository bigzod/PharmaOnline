from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'website/base.html')
	
def pharmacies(request):
	pharmacie = Pharmacie.objects.all()
	return render(request, 'app/pharmacies.html', {'RX': pharmacie})
	
