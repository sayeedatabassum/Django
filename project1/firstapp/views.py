from django.shortcuts import render

#importng HTTP response to provide the response for the end user
from django.http import HttpResponse

# Create your views here.
def display_data(request):
	data='<h1 style="color:teal">Hello, welcome to peacefull world!</h1>'
	return HttpResponse(data)