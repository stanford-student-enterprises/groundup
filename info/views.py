from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Barista, MenuItem

def home(request):
    return HttpResponse("hello world")

def baristas(request):
	baristas = Barista.objects.all()

	return render_to_response('info/baristas.html', {
			'baristas':baristas
		})

def menu(request):
	items = MenuItem.objects.all()

	return render_to_response('info/menu.html', {
			'items':items
		})