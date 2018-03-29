from common.UserReview import UserReview

class ChartData:
	def __init__(self, reviews):
		self.DataHelpfulness = {'very_helpful': 0, 'helpful': 0, 'not_helpful': 0}
		self.DataCommentbasedrating = {'very_good': 0, 'good': 0, 'ok': 0, 'bad': 0}
		#self.setDataHelpfulness(reviews)
		#self.setDataCommentbasedrating(reviews)
	
	def SetDataHelpfulness(self, reviews):
		for review in reviews:
			if(review.helpfulness >= 0.9):
				self.DataHelpfulness['very_helpful']+=1
			elif(review.helpfulness >= 0.4):
				self.DataHelpfulness['helpful']+=1
			else:
				self.DataHelpfulness['not_helpful']+=1
	
	def SetDataCommentbasedrating(self, reviews):
		for review in reviews:
			if(review.commentbasedrating >= 8):
				self.DataCommentbasedrating['very_good']+=1
			elif(review.commentbasedrating >= 6):
				self.DataCommentbasedrating['good']+=1
			elif(review.commentbasedrating >= 4):
				self.DataCommentbasedrating['ok']+=1
			else:
				self.DataCommentbasedrating['bad']+=1
	
	def GetJSON(self):
		dict={
		"DataHelpfulness": self.DataHelpfulness,
		"DataCommentbasedrating": self.DataCommentbasedrating
		}
		return dict