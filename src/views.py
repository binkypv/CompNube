from datetime import datetime
import os
import webapp2
import jinja2

from google.appengine.ext import db

from models import Events, Comment

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


class BaseHandler(webapp2.RequestHandler):

    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))


class ShowEvents(BaseHandler):
    
    def get(self):
        events = Events.all()
        self.render_template('events.html', {'events': events})
        
class NewEvent(BaseHandler):

    def post(self):
        event = Events(author = self.request.get('inputAuthor'),
                       title = self.request.get('inputTitle'),
                       description = self.request.get('inputDescription'),
                       type = self.request.get('inputType'),
                       #location = self.request.get('inputLocation'),
                       date = datetime.strptime(self.request.get('inputDate'), '%Y-%m-%dT%H:%M')
                       )
        event.put()
        return webapp2.redirect('/')

    def get(self):
        actualDate = datetime.now().strftime('%Y-%m-%dT%H:%M')
        self.render_template('new.html', {'actualDate': actualDate})


class EditEvent(BaseHandler):

    def post(self, event_id):
        iden = int(event_id)
        event = db.get(db.Key.from_path('Events', iden))
        event.author = self.request.get('inputAuthor')
        event.title = self.request.get('inputTitle')
        event.description = self.request.get('inputDescription')
        event.type = self.request.get('inputType')
        #event.location = self.request.get('inputLocation')
        event.date = datetime.strptime(self.request.get('inputDate'), '%Y-%m-%dT%H:%M')
        event.put()
        return webapp2.redirect('/')

    def get(self, event_id):
        iden = int(event_id)
        event = db.get(db.Key.from_path('Events', iden))
        date = event.date.strftime('%Y-%m-%dT%H:%M')
        actualDate = datetime.now().strftime('%Y-%m-%dT%H:%M')
        self.render_template('edit.html', {'event': event, 'date': date , 'actualDate': actualDate})


class DeleteEvent(BaseHandler):

    def get(self, event_id):
        iden = int(event_id)
        event = db.get(db.Key.from_path('Events', iden))
        db.delete(event)
        return webapp2.redirect('/')

class ViewEvent(BaseHandler):

    def get(self, event_id):
        comments = Comment.gql("WHERE event_id = :event_id", event_id=int(event_id))
        iden = int(event_id)
        event = db.get(db.Key.from_path('Events', iden))
        date = event.date.strftime('%Y-%m-%dT%H:%M')
        self.render_template('view.html', {'event': event, 'date': date ,'comments':comments})

    def post(self, event_id):
        comment = Comment(text=self.request.get('inputCommentText'),
                          event_id=int(event_id),
                          author=self.request.get('inputCommentAuthor'),
                          date=datetime.now())
        comment.put()
        return webapp2.redirect('/')

