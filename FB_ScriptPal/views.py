# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.views import generic

# Create your views here.

def home(request):
	return HttpResponse("Hello world.")

def BotView(request):
	if request.GET['hub.verify_token'] == '709337517':
		return HttpResponse(request.GET['hub.challenge'])
	else:
		return HttpResponse('Error, invalid token')

