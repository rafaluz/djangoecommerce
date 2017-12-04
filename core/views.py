from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#return HttpResponse('Hello World')
	#textos = ['rafael 1', 'rafael 2', 'rafael 3']
	#context = {
	#	'title': 'django e-commerce',
	#	'textos' : textos
	#} 
	return render(request, 'index.html')


def contact(request):
	return render(request, 'contact.html')

def product_list(request):
	return render(request, 'product_list.html')

def product(request):
	return render(request, 'product.html')	