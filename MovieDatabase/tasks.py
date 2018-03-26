from __future__ import absolute_import, unicode_literals
from .celery import app
from imdbpie import Imdb

@app.task
def APIGetTitle(id):
	imdb = Imdb()
	dict = imdb.get_title(id)
	return dict