from time import gmtime, strftime

class meeting:

	def __init__(self,mname,location,topic,etime=None,stime = strftime("%I:%M%p",gmtime()),email=[]):
		self.stime = stime
		self.mname = mname
		self.location = location
		self.topic = topic
		self.email = [email]
		self.etime = etime

	def add_email(self, email):
		self.email.append(email)

