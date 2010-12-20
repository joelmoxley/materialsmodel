import logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.dist import use_library

use_library('django', '1.1')
from google.appengine.ext.webapp import template


class FetchLMECobaltPrice(webapp.RequestHandler):
    def get(self):
        """docstring for get"""
        from cobalt.utils import mechanize_fetch_cobalt_price_page
        from models import CachedIMEPage
        content = mechanize_fetch_cobalt_price_page()
        if 'Sorry, an error has occurred' in content:
            logging.info('Bad timing...LME returned bum response')
        else:
            p = CachedIMEPage(content=content)
            p.put()
        self.response.out.write(content)
        

        
        

class MainPage(webapp.RequestHandler):
    def get(self):
        
        context = {
            'foo' : 1,
            'bar' : 'kyle',
        }
        markup = template.render('templates/index.html', context)
        self.response.out.write(markup)

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                     ('/cron/cobalt/', FetchLMECobaltPrice),
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()