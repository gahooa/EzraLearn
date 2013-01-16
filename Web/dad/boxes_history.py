# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


#############################################################################
#############################################################################

def ENC(sdata):
  return JE(sdata).encode('utf-8')

def DEC(bdata):
  return JD(bdata.decode('utf-8'))




@Expose
def Request(self):
  yield
  
  Data = []

  for bdata in App.Redis.lrange('boxes_history', 0, -1):
    Data.append(DEC(bdata))

  W = self.HTMLResponse()
  
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
        background-color: #ccc;
      }

      div.Box
      {
        text-align: center;
        width: 48px;
        height: 48px;
        border: 1px solid black;
        background-color: red;
        font-size: 5px;
      }

    </style>
    
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script> 
    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.9.2/jquery-ui.min.js"></script> 

    <script>

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

        $box.css('position', 'absolute');
        $box.css('left', x + 'px');
        $box.css('top', y + 'px');

        $('#Container').append($box);
        
        return ID;
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
      
      
      var Data = ''' + HS(JE(Data)) + ''';
      var Data_i = 0;
      var $Count;  //set on ready

      function Next()
      {
        var data = Data[Data_i];
        if(! data)
          return;

        Data_i += 1;
        
        SetBox(data.ID, data.x, data.y, data.c);
        $Count.text('Move #' + Data_i);
                
        setTimeout(Next, 1000/15);
      }




      $(function(){
        
        $Count = $('#Count');
      
        $('#Reload').click(function(e)
        {
          window.location.reload();
          e.preventDefault();
        });
        
        Next();
     
      });
    </script>
  
  
  </head>
  <body>
    <div style="position: fixed; right: 10px; top: 10px;">
      <strong>History of Boxes</strong> | 
      <span id="Count"></span> | 
      <a href="#" id="Reload">Reload</a>
    </div>

    <div id="Container">

    </div>
  </body>
</html>
    ''')   
  
  yield W



