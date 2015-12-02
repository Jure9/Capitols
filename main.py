#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class Mesto():
    mesto=""
    slika=""
    drzava=""

    def __init__(self, city, picture, state):
        self.mesto=city
        self.slika=picture
        self.drzava=state

class MainHandler(BaseHandler, Mesto):

    def get(self):
        ljubljana=Mesto("Ljubljana", "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSr1oXhPsNr-zn1jqiBlYH3DJDUKiRL0myVZVVeJ22aMvtJdIug", "Slovenije")
        damask=Mesto("Damask", "http://www.b92.net/news/pics/2006/10/178485400452453eea0b3b272538944_extreme.jpg", "Sirije")
        kampala=Mesto("Kampala", "http://www.capitasymonds.co.uk/images/kampala_web.jpg", "Ugande")
        funafuti=Mesto("Funafuti", "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS6s8fxAAFJDtyon9fao5N26Yjcnb1c6nVrageUj6Mh16wuLScXmQ", "Tuvale")
        p={"lj": ljubljana, "dam": damask, "kamp": kampala, "fun": funafuti}
        return self.render_template("hello.html", params=p)

    def post(self):
        slo=self.request.get("odgovor1").lower()
        sir=self.request.get("odgovor2").lower()
        uga=self.request.get("odgovor3").lower()
        tuv=self.request.get("odgovor4").lower()
        ljubljana=Mesto("ljubljana", "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSr1oXhPsNr-zn1jqiBlYH3DJDUKiRL0myVZVVeJ22aMvtJdIug", "Slovenije")
        damask=Mesto("damask", "http://www.b92.net/news/pics/2006/10/178485400452453eea0b3b272538944_extreme.jpg", "Sirije")
        kampala=Mesto("kampala", "http://www.capitasymonds.co.uk/images/kampala_web.jpg", "Ugande")
        funafuti=Mesto("funafuti", "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS6s8fxAAFJDtyon9fao5N26Yjcnb1c6nVrageUj6Mh16wuLScXmQ", "Tuvale")
        p={"lj": ljubljana, "dam": damask, "kamp": kampala, "fun": funafuti}
        if(len(slo)>0):
            if(slo==ljubljana.mesto):
                p["picture1"]="http://blog.m2sys.com/wp-content/uploads/2010/09/GreenCheck.jpg"
            else:
                p["picture1"]="http://www.scottdawson.ca/wp-content/uploads/2011/10/delete_icon.png"
        elif(len(sir)>0):
            if(sir==damask.mesto):
                p["picture2"]="http://blog.m2sys.com/wp-content/uploads/2010/09/GreenCheck.jpg"
            else:
                p["picture2"]="http://www.scottdawson.ca/wp-content/uploads/2011/10/delete_icon.png"
        elif(len(uga)>0):
            if(uga==kampala.mesto):
                p["picture3"]="http://blog.m2sys.com/wp-content/uploads/2010/09/GreenCheck.jpg"
            else:
                p["picture3"]="http://www.scottdawson.ca/wp-content/uploads/2011/10/delete_icon.png"
        elif(len(tuv)>0):
            if(tuv==funafuti.mesto):
                p["picture2"]="http://blog.m2sys.com/wp-content/uploads/2010/09/GreenCheck.jpg"
            else:
                p["picture2"]="http://www.scottdawson.ca/wp-content/uploads/2011/10/delete_icon.png"
        return self.render_template("hello.html", params=p)





app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
