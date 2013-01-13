# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


def ENC(sdata):
  return JE(sdata).encode('utf-8')

def DEC(bdata):
  return JD(bdata.decode('utf-8'))




@Expose
def Request(self):
  yield
  
  if self.Post.Action == 'Box':
    Data = {}
    Data['ID'] = IN_Int(self.Post.ID)
    Data['x'] = IN_Int(self.Post.x)
    Data['y'] = IN_Int(self.Post.y)
    Data['c'] = IN_Str(self.Post.c)
    App.Log("Action=Box: " + str(Data))
    App.Redis.hset('boxes', Data['ID'], ENC(Data))
    yield self.JSONResponse(Data)
  
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
    
    <script>

      var AL = {};
     
      // If passed, data contains ID, x, y, c (color)
      function Create(Data)
      {
        var div, $div;
        
        div = document.createElement('div');
        div.className = 'Box';
        
        if(! Data)
          Data = {ID: Date.now(), x: 0, y:0, c: '#f00'}

        $div = $(div);
        $div.ID = Data.ID;
        $div.css('background-color', Data.c);
        
        AL[$div.ID] = $div;

        $div.append(document.createTextNode($div.ID));

        $div.draggable({
          snap: true,
          stop: function(event, ui) {
            UpdateServer($div, ui.offset.left, ui.offset.top);
          }
        });



        $div.css('position', 'absolute');
        $div.css('left', Data.x + 'px');
        $div.css('top', Data.y + 'px');

        return $div;
      }

      
      function UpdateServer($box, x, y)
      {
        console.log('Updating server--', $box, x, y);

        $.post(
          "", 
          {Action:'Box', ID: $box.ID, x:x, y:y, c:$box.css('background-color')}
        );
      }

      function NewBox(c)
      {
        var $box = Create();
        $box.css('background-color', c);
        UpdateServer($box, 0, 0);
        $('#Container').append($box);
      }



      $(function(){
        
        $.each(''' + HS(JE(Data)) + ''', function(i,v)
        {
          $('#Container').append(Create(v));          
        });
        
      
      
        $('#Add1').click(function(e) { NewBox('red'); e.preventDefault(); } );
        $('#Add2').click(function(e) { NewBox('green'); e.preventDefault(); } );
        $('#Add3').click(function(e) { NewBox('blue'); e.preventDefault(); } );
        $('#Add4').click(function(e) { NewBox('yellow'); e.preventDefault(); } );
        $('#Add5').click(function(e) { NewBox('purple'); e.preventDefault(); } );
        $('#Add6').click(function(e) { NewBox('orange'); e.preventDefault(); } );
        


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



