from django.shortcuts import render
from django.http import HttpResponse
#from catalog.models import Category

from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.views.generic import View, TemplateView, CreateView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import get_user_model
from django.core.urlresolvers import reverse_lazy
User = get_user_model()

class IndexView(TemplateView):
	template_name = 'index.html'

index = IndexView.as_view()



def contact(request):
	success = False
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.send_mail()
		success = True
	context = {
		'form': form,
		'success': success,
	}
	return render(request, 'contact.html', context)

class RegisterView(CreateView):

	form_class = UserCreationForm
	template_name = 'register.html'
	model = User
	success_url = reverse_lazy('login')

register = RegisterView.as_view()
