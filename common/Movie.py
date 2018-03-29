from imdbpie import Imdb
from common.UserReview import UserReview
from common.ChartData import ChartData

class Movie:
	def __init__(self):
		self.imdb = Imdb()
		self.reviews = None
		self.chartdata = None
		self.director = None
		self.commentbasedrating = 0
		self.title= None
		self.poster= None
		self.durationMin=None
		self.rating= 0
		self.id=None
		self.summary=None
		self.outline=None
		self.cast=None
		self.directors=None

	def SetAfterInit(self, dict):
		self.dict = dict
		self.id=dict['base']['id'].split('/')[2]
		
		if 'base' in self.dict:
			if 'title' in self.dict['base']:
				self.title=self.dict['base']['title']
			if 'runningTimeInMinutes' in self.dict['base']:
				self.durationMin=self.dict['base']['runningTimeInMinutes']
			if 'image' in self.dict['base']:
				if 'url' in self.dict['base']['image']:
					self.poster=self.dict['base']['image']['url']
		if 'ratings' in self.dict:
			if 'rating' in self.dict['ratings']:
				self.rating=float(self.dict['ratings']['rating'])
		if 'plot' in self.dict:
			if 'outline' in self.dict['plot']:
				if 'text' in self.dict['plot']['outline']:
					self.outline= self.dict['plot']['outline']['text']
			if 'summaries' in self.dict['plot']:
				if len(self.dict['plot']['summaries']) > 0:
					self.summary = self.dict['plot']['summaries'][0]['text']

	def SetAfterSearch(self, dict):
		self.id=dict['id']
		self.title=dict['title']
		self.poster= dict['poster']
		self.durationMin=dict['durationMin']
		self.rating=dict['rating']
		self.outline=dict['outline']
		self.summary=dict['summary']
				
	def AnalyzeReviews(self):
		self.GetReviews()
		if self.reviews!=None:
			self.SetCommentbasedrating()
			self.GenerateChartData()
	
	def GetReviews(self):
		
		reviews_temp_load = self.imdb.get_title_user_reviews(self.id)
		if 'reviews' in reviews_temp_load:
			reviews_temp=reviews_temp_load['reviews']
			self.reviews = []
			for review in reviews_temp:
				review_temp = UserReview(review['helpfulnessScore'], review['reviewText'])
				self.reviews.append(review_temp)
		
	def SetCommentbasedrating(self):
		scoreSum=0
		for review in self.reviews:
			scoreSum+=review.commentbasedrating
		self.commentbasedrating=scoreSum/len(self.reviews)
		
	def GenerateChartData(self):
		cd=ChartData(self.reviews)
		cd.SetDataHelpfulness(self.reviews)
		cd.SetDataCommentbasedrating(self.reviews)
		self.chartdata=cd
		
	def SetCast(self):
		dict=self.imdb.get_title_credits(self.id)
		if 'credits' in dict:
			if 'cast' in dict['credits']:
				self.cast=dict['credits']['cast']
			if 'director' in dict['credits']:
				self.directors=dict['credits']['director']
		
	def GetJSONSearch(self):
		
		listReviews = []
		if self.reviews!=None:
			for review in self.reviews:
				listReviews.append(review.GetJSON())
		
		cd={}
		if self.chartdata!=None:
			cd=self.chartdata.GetJSON()
		
		dict={
		"id": self.id,
		"title": self.title,
		"poster": self.poster,
		"durationMin": self.durationMin,
		"rating": self.rating,
		"outline": self.outline,
		"summary": self.summary,
		"cast": self.cast,
		"directors": self.directors,
		"reviews": listReviews,
		"commentbasedrating": self.commentbasedrating,
		"chartdata": cd
		}
		return dict
	



		
	