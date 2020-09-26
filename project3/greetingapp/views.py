from django.shortcuts import render

from django.http import HttpResponse
import datetime
# Create your views here.

#function based view
def welcome_clients(request):
	date=datetime.datetime.now()
	hour=int(datetime.datetime.now().hour)
	msg='<h1>Hi Students'

	if hour>0 and hour<12:
		msg=msg+'<h1>Good Morning</h1>'
	elif hour>12 and hour<16:
		msg=msg+'<h1>Good Afternoon</h1>'
	elif hour>16 and hour<21:
		msg=msg+'<h1>Good Evening</h1>'
	else:
		msg=msg+'Good Night'
	msg=msg+'</h1><hr>'

	msg=msg+'<h1>the server time is: '+str(date)+'</h1> '

	return HttpResponse(msg)