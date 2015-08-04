from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from website.models import Pharmacie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
	return render(request, 'website/base.html')
	
def pharmacies(request):
	pharma = Pharmacie.objects.all()
	paginator = Paginator(pharma, 10)
	page = request.GET.get('page')
	try:
		pharmacies = paginator.page(page)
	except PageNotAnInteger:
		pharmacie = paginator.page(1)
	except EmptyPage:
		pharmacies = paginator.page(paginator.num_pages)	

	return render_to_response('website/pharmacies.html', {'pharmacies': pharma})
	

def new_home(request):
	return render(request, 'website/layout.html', {})

	
	
