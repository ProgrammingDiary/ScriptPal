# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.views import generic
#import apiai

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json, pprint

#ai = apiai.ApiAI('f97f736a12164e548a3b33a90b2dfe0e')

# Create your views here.

def home(request):
	return HttpResponse("Hello world.")

def post_facebook_message(fbid, recevied_message):           
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAABozjY7nEwBAMzuKslGAYkB2CWiH8jAGfyhqzo7uOaFB1bSEjDNoCzdQ3hKx3RpZAXXTAtyK1LpsGUMhvMVJ3A43DsEq97PSlZAQ3LDp0AdkYhqZCZBrS1ZAz5ZCoTkZCNjZAUWNSOp4LZBSe4oZC8iZBCjju2ob0UJlIHri6DExBPjQZDZD' 
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint.pprint(status.json())

class BotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'scriptpalrocks':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                if 'message' in message:
                    # Print the message to the terminal
                    pprint.pprint(message) 
                    post_facebook_message(message['sender']['id'], message['message']['text'])    
        return HttpResponse()


