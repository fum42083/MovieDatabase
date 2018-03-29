
class UserReview:
	def __init__(self, helpfulness, text):
		self.helpfulness=helpfulness
		self.text=text
		self.commentbasedrating = 5
		self.CalcCommentbasedrating()
		
	def CalcCommentbasedrating(self):
		for word in self.text.split():
			word=word.lower()
			if (word=='awesome'):
				self.commentbasedrating+=2
			elif (word=='great'):
				self.commentbasedrating+=1
			elif (word=='good'):
				self.commentbasedrating+=0.5
			elif (word=='bad'):
				self.commentbasedrating-=0.5
			elif (word=='awful'):
				self.commentbasedrating-=1.5
			if (self.commentbasedrating < 0):
				self.commentbasedrating=0
			if (self.commentbasedrating > 10):
				self.commentbasedrating=10
	
	def GetJSON(self):
		dict={
		"helpfulness": self.helpfulness,
		"text": self.text,
		"commentbasedrating": self.commentbasedrating,
		}
		return dict