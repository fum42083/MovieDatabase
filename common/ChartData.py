from common.UserReview import UserReview

class ChartData:
	def __init__(self, reviews):
		self.DataHelpfulness = {'very helpful': 0, 'helpful': 0, 'not helpful': 0}
		self.DataCommentbasedrating = {'very good': 0, 'good': 0, 'ok': 0, 'bad': 0}
		setDataHelpfulness(reviews)
		setDataCommentbasedrating(reviews)
	
	def SetDataHelpfulness(reviews):
		for review in reviews:
			if(review.helpfulness >= 0.8):
				self.DataHelpfulness['very helpful']+=1
			elif(review.helpfulness >= 0.4):
				self.DataHelpfulness['helpful']+=1
			else:
				self.DataHelpfulness['not helpful']+=1
	
	def SetDataCommentbasedrating(reviews):
		for review in reviews:
			if(review.commentbasedrating >= 0.8):
				self.DataCommentbasedrating['very good']+=1
			elif(review.commentbasedrating >= 0.6):
				self.DataCommentbasedrating['good']+=1
			elif(review.commentbasedrating >= 0.4):
				self.DataCommentbasedrating['ok']+=1
			else:
				self.DataCommentbasedrating['bad']+=1
	