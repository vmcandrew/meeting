from time import gmtime, strftime

class meeting:

	def __init__(self,stime = strftime("%I:%M%p",gmtime()),mname,location,topic,email=[],etime):
		self.stime = stime
		self.mname = mname
		self.location = location
		self.topic = topic
		self.email = email
		self.etima = etime