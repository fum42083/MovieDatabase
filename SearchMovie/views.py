# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from imdbpie import Imdb
from common.Movie import Movie
from common.MovieHelper import SearchMovies
import ast

#def index(request):
#	imdb = Imdb()
#	return HttpResponse(imdb.search_for_title('titanic'))

def index(request):
	return render(request, 'SearchMovie/home.html')
	
def list(request):
	#imdb = Imdb()
	#dictlist = imdb.search_for_title(request.POST.__getitem__("search"))
	movies = SearchMovies(request.POST.__getitem__("search"))
	moviesDict=[]
	for m in movies:
		
		moviesDict.append(m.GetJSONSearch())
	#return HttpResponse(movies[0].title)
	return render(request, 'SearchMovie/listmovies.html', {'movies': moviesDict})

def show(request):
	movie=Movie()
	dict=ast.literal_eval(request.POST.__getitem__("movie"))
	movie.SetAfterSearch(dict)
	#return HttpResponse(movie.GetJSONSearch()['rating'])
	return render(request, 'SearchMovie/showmovie.html', {'movie': movie.GetJSONSearch()})