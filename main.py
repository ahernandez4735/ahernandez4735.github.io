#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import logging
import webapp2
import os
from google.appengine.api import app_identity
from google.appengine.api import mail


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('home.html')
        self.response.write(template.render())
    def post(self):
        name = self.request.get("Name")
        email = self.request.get("Email")
        content = self.request.get("Message")

        mail.send_mail(sender='ahernandez4735@gmail.com',
                   to="ahernandez4735@gmail.com",
                   subject="New Mariachi Message From " + name,
                   body= name + """ wrote:

""" + content + """

Customers email is: """ + email)

        mail.send_mail(sender='ahernandez4735@gmail.com', to= email, subject= "Thank you for your inquiry! - Mariachi Cuerdas De Oro",
        body="Hello " + name + """,

My name is Alejandro and I'm a member of Mariachi Cuerdas De Oro. We have received your inquiry and will be in contact with you as soon as possible. If it is something urgent please call us at (510) 694-9309.

Thanks,

Alejandro""")


        self.redirect('/')



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
