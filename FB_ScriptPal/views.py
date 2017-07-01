# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.views import generic

# Create your views here.

def home(request):
	return HttpResponse("Hello world.")

def BotView(request):
	if request.method == 'GET':
		if request.GET['hub.verify_token'] == '709337517':
			return HttpResponse(request.GET['hub.challenge'])
		else:
			return HttpResponse('Error, invalid token')
	if request.method == 'POST':
		incoming_message = json.loads(request.body.decode('utf-8'))
		# Facebook recommends going through every entry since they might send
		# multiple messages in a single call during high load
		for entry in incoming_message['entry']:
			for message in entry['messaging']:
				# Check to make sure the received call is a message call
				# This might be delivery, optin, postback for other events 
				if 'message' in message:
					# Print the message to the terminal
					pprint(message)
		return HttpResponse()

