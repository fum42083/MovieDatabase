from imdbpie import Imdb
from common.UserReview import UserReview
from common.ChartData import ChartData

class Movie:
	def __init__(self):
		#self.actors = None
		self.reviews = None
		self.chartdata = None
		self.director = None
		self.commentbasedrating = None
		self.title= None
		self.poster= None
		self.durationMin=None
		self.rating=None
		self.id=None
		self.imdb = Imdb()

	def SetAfterInit(self, dict):
		self.dict = dict
		#dictDirector=imdb.get_title_top_crew(id)
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
				self.rating=self.dict['ratings']['rating']
		
	def SetAfterSearch(self, dict):
		self.id=dict['id']
		self.title=dict['title']
		self.poster= dict['poster']
		self.durationMin=dict['durationMin']
		self.rating=dict['rating']
				
	def AnalyseReviews():
		self.GetReviews()
		self.SetCommentbasedrating()
		self.GenerateChartData()
	
	def GetReviews(self, id):
		reviews_temp = self.imdb.get_title_user_reviews(id)['reviews']
		self.reviews = []
		for review in reviews_temp:
			review_temp = UserReview(review['helpfulnessScore'], review['reviewText'])
			review_temp.calcCommentbasedrating()
			reviews.append(review_temp)
		
	def SetCommentbasedrating():
		scoreSum=0
		for review in self.reviews:
			scoreSum+=review.commentbasedrating
		self.commentbasedrating=scoreSum/len(self.reviews)
		
	def GenerateChartData():
		self.chartdata=ChartData(self.reviews)
		
	def GetJSONSearch(self):
		dict={
		"id": self.id,
		"title": self.title,
		"poster": self.poster,
		"durationMin": self.durationMin,
		"rating": self.rating
		}
		return dict
	



		
	