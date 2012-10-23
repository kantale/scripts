
import webapp2

from time import gmtime, strftime

from google.appengine.ext import db

class Log_item(db.Model):
	user = db.StringProperty()
	message = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)

#def log_key(log_name=None):
#	return db.Key.from_path('Molgenislog', log_name or 'default_log')


def now():
	return strftime("%a, %d %b %Y %H:%M:%S", gmtime())


class MainPage(webapp2.RequestHandler):
	def get(self):
	#	self.response.headers['Content-Type'] = 'text/plain'

		message = self.request.get('msg')
		user = self.request.get('user')
		action = self.request.get('action')

		if action == 'store':
			#Store message:
			log_item = Log_item()
			log_item.message = message
			log_item.user = user
			log_item.put()

			self.response.headers['Content-Type'] = 'text/plain'
			self.response.write('ok')

		if action == 'view':
			log_items = db.GqlQuery("SELECT * "
				"FROM Log_item "
				"WHERE user = :1 "
				"ORDER BY date DESC LIMIT 10 ",
				user
			    )

			self.response.write('<html><body>')
			self.response.write('<ul>')
			for log_item in log_items:
				self.response.write('<li>%s. %s</li>' % (log_item.date, log_item.message))
			self.response.write('</ul>')
				
			self.response.write('</body></html>')


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

