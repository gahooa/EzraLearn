# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


htmlstart = '''
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
        margin: 10px;
      }

      table td
      { 
        padding: 5px;
        border: 2px solid #666;
        border-collapse: collapse;
        text-align: center;
        vertical-align: middle;
        width: 60px;
        height: 60px;
        font-family: 'courier new';
        font-size: 12pt;
      }

      div.Box
      {
        position: absolute;
        top: 10px;
        right: 10px;
        width: 100px;
        height: 100px;
        background-color: orange;
        border: 1px solid black;
      }

    </style>
  </head>
  <body>
'''

htmlend = '''
    <div class="Box"></div>
    <div class="Box"></div>
    <div class="Box"></div>
    <div class="Box"></div>
    <div class="Box"></div>
    <div class="Box"></div>
    <div class="Box"></div>
    <div class="Box"></div>
    <div class="Box"></div>
    <div class="Box"></div>
    
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script> 
    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.9.2/jquery-ui.min.js"></script> 
    
    <script>
      $(function(){
        $('div.Box').draggable();
      });

    </script>
  </body>
</html>
'''


@Expose
def Request(self):
  yield
 
  w1 = IN_Int(self.Get.w1) or 1
  w2 = IN_Int(self.Get.w2) or 12
  h1 = IN_Int(self.Get.h1) or 1
  h2 = IN_Int(self.Get.h2) or 12

  W = self.HTMLResponse()
  W(htmlstart)
      
   
  
  W('''
    <h1>Ezra minus program</h1>
    <form name="F" method="get">
      Width (start, end): 
      <input type="text" name="w1" value=''' + QA(w1) + ''' />
      <input type="text" name="w2" value=''' + QA(w2) + ''' />
      <br />
      Height (start, end): 
      <input type="text" name="h1" value=''' + QA(h1) + ''' />
      <input type="text" name="h2" value=''' + QA(h2) + ''' />
      <br />
      <input type="submit" value="Update!" />
      or <a href="?">Reset</a>
    </form>

    <br />
    <br />
  
    <table>
    ''')

  W('<tr>\n')
  W('<td><strong style="font-size: 200%;">-</strong></td>')
    
  for x in range(w1,w2+1):
    W('<td><strong>' + str(x) + '</strong></td>\n')
    
  W('</tr>\n')
  
  i = 0
  
  for y in range(h1,h2+1):
    W('<tr>\n')
    
    W('<td><strong>' + str(y) + '</strong></td>\n')
    
    for x in range(w1,w2+1):
      W('<td>' + str(x-y) + '</td>\n')
      i += 1
      if i > 10000:
        raise Exception('TOO BIG')
          
    W('</tr>\n')

  W('</table>\n')
  
  W(htmlend)

  yield W



