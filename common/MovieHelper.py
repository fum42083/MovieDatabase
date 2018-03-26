from MovieDatabase.tasks import APIGetTitle
from imdbpie import Imdb
from common.Movie import Movie
from celery import group
import time

def SearchMovies(value):
	imdb = Imdb()
	dict=imdb.search_for_title(value)
	dictsAsync = []
	movies_result = []
	for m in dict:
		if (m['type']!=None):
			dictsAsync.append(APIGetTitle.s(m['imdb_id']))
	groupDictsAsync = group(dictsAsync)
	result = groupDictsAsync.apply_async()
	while result.ready()==False:
		time.sleep(1)
	for m in result.get():
		mov=Movie()
		mov.SetAfterInit(m)
		movies_result.append(mov)
	return movies_result