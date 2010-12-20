from google.appengine.ext import db

class CachedIMEPage(db.Model):
    datetime_added = db.DateTimeProperty(auto_now_add=True)
    last_changed = db.DateTimeProperty(auto_now_add=True)
    content = db.TextProperty()
