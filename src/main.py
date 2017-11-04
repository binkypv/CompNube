from views import ShowAdds, NewAdd, DeleteAdd, EditAdd, ViewAdd
import webapp2

app = webapp2.WSGIApplication([
        ('/', ShowAdds), 
        ('/new', NewAdd), 
        ('/edit/([\d]+)', EditAdd),
        ('/delete/([\d]+)', DeleteAdd),
        ('/view/([\d]+)', ViewAdd),
        ],
        debug=True)
