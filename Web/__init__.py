# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *

from AppStruct.WSGI.Handler.Point import PointHandler
from AppStruct.WSGI.Plugin import QueryString, PostForm, Cookie, SessionToken

import AppStruct.UI.CoolBlue 


###############################################################################
# Instances of this become the Req object.
class application(PointHandler, QueryString, PostForm, SessionToken, Cookie):
  PointHandler_ImportStrip = 0

  # Instance variables

  # Instance Settings

  # Beginning of Request handler
  def RequestStart(self):
    App.Open()
    App.Log = self.Env.Log
    App.Log("SessionToken:"+self.SessionToken+"; IsNew:"+str(self.SessionToken_IsNew)+';')
  
  # Uncaught exception handler
  def RequestError(self, e):
    if isinstance(e, AuthorizationError):
      return self.HTMLResponse('''
        <!DOCTYPE html>
        <html>
          <head>
            <title>Access Denied</title>
          </head>
          <body>
            <h1>Access Denied</h1>
            <a href="#" onclick="window.history.go(-1); return false;">Go Back</a>
          </body>
        </html>
        ''')
    else:
      return

  # End of Request handler
  def RequestEnd(self):
    del(App.Log)
    App.Close()


  # Session code
  def _SK(self, name):
    return name + "@" + self.SessionToken

  def SessionSetString(self, name, value):
    App.Redis.SetString(self._SK(name), value)

  def SessionGetString(self, name):
    return App.Redis.GetString(self._SK(name))
  
  def SessionSetInteger(self, name, value):
    App.Redis.SetInteger(self._SK(name), value)

  def SessionGetInteger(self, name):
    return App.Redis.GetInteger(self._SK(name))

  def SessionDelete(self, name):
    App.Redis.delete(self._SK(name))
    

###############################################################################

def Init(self):
  
  yield
  self.UI = self.Response(AppStruct.UI.CoolBlue.Desktop)
  
  self.UI.CSS.Add('/assets/Site.css?' + App.CacheTime)
  self.UI.JS.Add('/assets/Site.js?' + App.CacheTime)
  
  self.UI.TitlePrefix = 'learn.gahooa.com'
  
  self.UI.Nav1.Add('/', Name='Home') 
  self.UI.Nav1.Add('/mathtables/times', Name='Math Tables') 
  self.UI.Nav1.Add('/mathdrill/simple', Name='Math Drill') 
  self.UI.Nav1.Add('/dad/boxes', Name='Boxes') 
  self.UI.Nav1.Add('/dad/boxes_history', Name='Boxes History') 
  self.UI.Nav1.Add('/story/', Name='Stories') 
  self.UI.Nav1.Add('/trystuff/', Name='Try Stuff') 

  if App.DevLevel == 0:
    self.UI.Script('''
      var _gauges = _gauges || [];
      (function() {
      var t   = document.createElement('script');
      t.type  = 'text/javascript';
      t.async = true;
      t.id    = 'gauges-tracker';
      t.setAttribute('data-site-id', '51147057108d7b16a4000049');
      t.src = '//secure.gaug.es/track.js';
      var s = document.getElementsByTagName('script')[0];
      s.parentNode.insertBefore(t, s);
      })();
      ''')


  yield


