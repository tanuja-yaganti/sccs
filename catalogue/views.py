from django.shortcuts import render
from django.views.generic import ListView
from .models import Component

# Create your views here.
def component_list(request):
	search_term = ''
	components = Component.objects.all()
	if 'search' in request.GET:
		search_term = request.GET['search']
		components = components.filter(keywords__icontains=search_term)
	context = {'components':components, 'search_term':search_term}
	return render(request, 'catalogue/index.html', context)
		