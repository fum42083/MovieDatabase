# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from imdbpie import Imdb

#def index(request):
#	imdb = Imdb()
#	return HttpResponse(imdb.search_for_title('titanic'))

def index(request):
	return render(request, 'SearchMovie/home.html')
	
def list(request):
	imdb = Imdb()
	dictlist = imdb.search_for_title(request.POST.__getitem__("search"))
	return render(request, 'SearchMovie/listmovies.html', {'dictlist': dictlist})
