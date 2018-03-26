
class UserReview:
	def __init__(self, helpfulness, text):
		self.helpfulness=helpfulness
		self.text=text
		self.commentbasedrating = 0.5
		CalcCommentbasedrating()
		
	def CalcCommentbasedrating():
		for word in text.split().lower():
			if (word=='awesome'):
				self.commentbasedrating+=0.2
			elif (word=='great'):
				self.commentbasedrating+=0.1
			elif (word=='good'):
				self.commentbasedrating+=0.05
			elif (word=='bad'):
				self.commentbasedrating-=0.5
			elif (word=='awful'):
				self.commentbasedrating-=0.15
			if (commentbasedrating < 0):
				commentbasedrating=0
			if (commentbasedrating > 1):
				commentbasedrating=1