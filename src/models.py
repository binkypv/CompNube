from google.appengine.ext import db


class Events(db.Model):

    title = db.StringProperty()
    author = db.EmailProperty()
    description = db.TextProperty()
    type = db.StringProperty()
    location = db.GeoPtProperty()
    #image = images.Image()
    date = db.DateTimeProperty(auto_now_add = True)
    
class Comment(db.Model):
    
    author = db.StringProperty()
    event_id = db.IntegerProperty()
    text = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)