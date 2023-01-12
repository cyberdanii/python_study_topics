
from django.shortcuts import render
from django.conf import settings
import datetime
import requests
import json

character = 'character/'
episode = 'episode/'
location = 'location/'
pages = '?pages='


def index(request):
	url = settings.REST_API + character
	response =  requests.get(url)
	contenido = json.loads(response.content)
	adicional = {"contenido":contenido}
	return render(request,'index.html')

def characters(request):
	response_body = {"results":[]}
	url = settings.REST_API + character
	
	while True:
		response =  requests.get(url)
		contenido = json.loads(response.content)
		if contenido['info']['next'] != None:
			response_body["results"].extend(contenido['results'])
			url = contenido['info']['next']
		else:
			break

	adicional = {"contenido":response_body}
	return render(request,'personajes.html',adicional)

def planets(request):
	response_body = {"results":[]}
	url = settings.REST_API + location
	
	while True:
		response =  requests.get(url)
		contenido = json.loads(response.content)
		response_body["results"].extend(contenido['results'])
		if contenido['info']['next'] == None:
			break
		else:
			url = contenido['info']['next']
	adicional = {"contenido":response_body}
	return render(request,'personajes.html',adicional)

def chapters(request):
	response_body = {"results":[]}
	url = settings.REST_API + episode
	
	while True:
		response =  requests.get(url)
		contenido = json.loads(response.content)
		response_body["results"].extend(contenido['results'])
		if contenido['info']['next'] == None:
			break
		else:
			url = contenido['info']['next']
	adicional = {"contenido":response_body}
	return render(request,'personajes.html',adicional)
