# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


#############################################################################
#############################################################################
from http.client import HTTPConnection
import time, hashlib, hmac, base64

try:
    import json
except ImportError:
    import simplejson as json


host    = 'api.pusherapp.com'
port    = 80
app_id  = 35272
key     = '8bcfbfc504b757614e2d'  #EzraLearn/dad/boxes
secret  = 'e650eb0f7b1ffb911d68'

class Pusher(object):
    def __init__(self, app_id=None, key=None, secret=None, host=None, port=None):
        _globals = globals()
        self.app_id = app_id or _globals['app_id']
        self.key = key or _globals['key']
        self.secret = secret or _globals['secret']
        self.host = host or _globals['host']
        self.port = port or _globals['port']
        self._channels = {}

    def __getitem__(self, key):
        if key not in self._channels:
            return self._make_channel(key)
        return self._channels[key]

    def _make_channel(self, name):
        self._channels[name] = channel_type(name, self)
        return self._channels[name]

class Channel(object):
    def __init__(self, name, pusher):
        self.pusher = pusher
        self.name = name
        self.path = '/apps/%s/channels/%s/events' % (self.pusher.app_id, self.name)

    def trigger(self, event, data={}, socket_id=None):
        json_data = json.dumps(data)
        status = self.send_request(self.signed_query(event, json_data, socket_id), json_data)
        if status == 202:
            return True
        elif status == 401:
            raise AuthenticationError
        elif status == 404:
            raise NotFoundError
        else:
            raise Exception("Unexpected return status %s" % status)

    def signed_query(self, event, json_data, socket_id):
        query_string = self.compose_querystring(event, json_data, socket_id)
        string_to_sign = "POST\n%s\n%s" % (self.path, query_string)
        signature = hmac.new(bytes(self.pusher.secret.encode('utf8')), string_to_sign.encode('utf8'), hashlib.sha256).hexdigest()

        return "%s&auth_signature=%s" % (query_string, signature)

    def compose_querystring(self, event, json_data, socket_id):
        hasher = hashlib.md5()
        hasher.update(json_data.encode('utf8'))
        hash_str = hasher.hexdigest()
        ret = "auth_key=%s&auth_timestamp=%s&auth_version=1.0&body_md5=%s&name=%s" % (self.pusher.key, int(time.time()), hash_str, event)
        if socket_id:
            ret += "&socket_id=" + unicode(socket_id)
        return ret

    def send_request(self, query_string, data_string):
        signed_path = '%s?%s' % (self.path, query_string)
        http = HTTPConnection(self.pusher.host, self.pusher.port)
        http.request('POST', signed_path, data_string)
        return http.getresponse().status

    def authenticate(self, socket_id, custom_data=None):
        if custom_data:
            custom_data = json.dumps(custom_data)

        auth = self.authentication_string(socket_id, custom_data)
        r = {'auth': auth}

        if custom_data:
            r['channel_data'] = custom_data

        return r

    def authentication_string(self, socket_id, custom_string=None):
      if not socket_id:
          raise Exception("Invalid socket_id")

      string_to_sign = "%s:%s" % (socket_id, self.name)

      if custom_string:
        string_to_sign += ":%s" % custom_string

      signature = hmac.new(bytes(self.pusher.secret.encode('utf8')), string_to_sign.encode('utf8'), hashlib.sha256).hexdigest()

      return "%s:%s" % (self.pusher.key,signature)

class GoogleAppEngineChannel(Channel):
    def send_request(self, query_string, data_string):
        from google.appengine.api import urlfetch
        absolute_url = 'http://%s/%s?%s' % (self.pusher.host, self.path, query_string)
        response = urlfetch.fetch(
            url=absolute_url,
            payload=data_string,
            method=urlfetch.POST,
            headers={'Content-Type': 'application/json'}
        )
        return response.status_code

class AuthenticationError(Exception):
    pass

class NotFoundError(Exception):
    pass

channel_type = Channel


#############################################################################
#############################################################################

def ENC(sdata):
  return JE(sdata).encode('utf-8')

def DEC(bdata):
  return JD(bdata.decode('utf-8'))




@Expose
def Request(self):
  yield
  if self.Post.Action == 'SetBox':
    Data = {}
    Data['ID'] = IN_Int(self.Post.ID)
    Data['x'] = IN_Int(self.Post.x)
    Data['y'] = IN_Int(self.Post.y)
    Data['c'] = IN_Str(self.Post.c)
    App.Log("Action={0}: {1}".format(self.Post.Action, str(Data)))
    App.Redis.hset('boxes', Data['ID'], ENC(Data))
    App.Redis.rpush('boxes_history', Data['ID'], ENC(Data))

    P = Pusher()
    P['boxes'].trigger('SetBox', Data)
    
    yield self.JSONResponse(JE({'Success': True}))
  
  W = self.HTMLResponse()

  Data = []
  
  for bdata in App.Redis.hvals('boxes'):
    Data.append(DEC(bdata))

  W('''
<!DOCTYPE html>
<html>
  <head>
    <style>
      html, body, div, form, fieldset, legend, label {margin: 0; padding: 0; font-family: verdana;}
      table {border-collapse: collapse; border-spacing: 0; }
      th, td {text-align: left; vertical-align: top; }
      h1, h2, h3, h4, h5, h6, th, td, caption { font-weight:normal; }
      img { border: 0; }
      
     
      body
      {
        margin: 0px;
      }

      div.Box
      {
        text-align: center;
        width: 48px;
        height: 48px;
        border: 1px solid black;
        cursor: move;
        background-color: red;
        font-size: 5px;
      }

    </style>
    
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script> 
    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.9.2/jquery-ui.min.js"></script> 
    <script src="http://js.pusher.com/1.12/pusher.min.js"></script>

    <script>
      // Enable pusher logging - don't include this in production
      Pusher.log = function(message) {
        if (window.console && window.console.log) window.console.log(message);
      };

      var pusher = new Pusher(''' + HS(JE(key)) + ''');  
      var channel = pusher.subscribe('boxes');
      channel.bind('SetBox', function(data) {
        console.log(data);
        
        SetBox(data.ID, data.x, data.y, data.c);

      });

      var AL = {};
     
      // Create and add a box object to the document
      // Return the ID
      function MakeBoxObject(ID, x, y, c)
      {
        var div, $box;
        
        div = document.createElement('div');
        div.className = 'Box';
        
        if(! ID) 
          ID = Date.now();
        
        if(typeof(x) === "undefined") 
          x = 0;
        
        if(typeof(y) === "undefined") 
          y = 0;
        
        if(typeof(c) === "undefined") 
          c = "#000";

        $box = $(div);
        $box.ID = ID;
        $box.css('background-color', c);
       
        if(ID in AL)
          AL[ID].remove();
        
        AL[$box.ID] = $box;

        $box.append(document.createTextNode(ID));

        $box.draggable({
          snap: true,
          stop: function(event, ui) {
            UpdateServer($box.ID, ui.offset.left, ui.offset.top, $box.css('background-color'));
          }
        });

        $box.css('position', 'absolute');
        $box.css('left', x + 'px');
        $box.css('top', y + 'px');

        $('#Container').append($box);
        
        return ID;
      }

      
      function UpdateServer(ID, x, y, c)
      {
        if(! ID in AL)
        {
          throw "Error: Box ID " + ID + " not found.";
          return;
        }

        console.log('Updating server--', ID, x, y, c);

        $.post(
          "", 
          {Action:'SetBox', ID:ID, x:x, y:y, c:c}
        );
      }

      // Set a box to this location and color.  Create if needed.
      function SetBox(ID, x, y, c)
     {
        var $box;
        if(ID in AL)
        {
          $box = AL[ID];
          $box.animate({left: x+"px", top: y+"px", "background-color": c});
        }
        else
        {
          ID = MakeBoxObject(ID, x, y, c);
        }
      }
      
      function NewBox(x, y, c)
      {
        var ID = MakeBoxObject(ID, x, y, c);
        UpdateServer(ID, x, y, c);
      }


      $(function(){
        
        $.each(''' + HS(JE(Data)) + ''', function(i,data)
        {
          MakeBoxObject(data.ID, data.x, data.y, data.c);
        });
              
      
        $('#Add1').click(function(e) { NewBox(0,0,'red'); e.preventDefault(); } );
        $('#Add2').click(function(e) { NewBox(0,0,'green'); e.preventDefault(); } );
        $('#Add3').click(function(e) { NewBox(0,0,'blue'); e.preventDefault(); } );
        $('#Add4').click(function(e) { NewBox(0,0,'yellow'); e.preventDefault(); } );
        $('#Add5').click(function(e) { NewBox(0,0,'purple'); e.preventDefault(); } );
        $('#Add6').click(function(e) { NewBox(0,0,'orange'); e.preventDefault(); } );
        

        $('#Reload').click(function(e)
        {
          window.location.reload();
          e.preventDefault();
        });
     
      });
    </script>
  
  
  </head>
  <body>
    <div style="position: fixed; right: 10px; top: 10px;">
      <a href="#" id="Add1">Add Red</a> |
      <a href="#" id="Add2">Add Green</a> |
      <a href="#" id="Add3">Add Blue</a> |
      <a href="#" id="Add4">Add Yellow</a> |
      <a href="#" id="Add5">Add Purple</a> |
      <a href="#" id="Add6">Add Orange</a> |
      <a href="#" id="Reload">Reload</a>
    </div>

    <div id="Container">

    </div>
  </body>
</html>
    ''')   
  
  yield W



