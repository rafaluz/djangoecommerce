from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Category

def index(request):
	#return HttpResponse('Hello World')
	#textos = ['rafael 1', 'rafael 2', 'rafael 3']
	#context = {
	#	'title': 'django e-commerce',
	#	'textos' : textos,
	#	'categories': Category.objects.all(),
	#}
	return render(request, 'index.html')


def contact(request):
	return render(request, 'contact.html')

