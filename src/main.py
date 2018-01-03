from views import ShowEvents, NewEvent, EditEvent, DeleteEvent, ViewEvent
import webapp2

app = webapp2.WSGIApplication([
        ('/', ShowEvents), 
        ('/new', NewEvent), 
        ('/edit/([\d]+)', EditEvent),
        ('/delete/([\d]+)', DeleteEvent),
        ('/view/([\d]+)', ViewEvent),
        ],
        debug=True)
