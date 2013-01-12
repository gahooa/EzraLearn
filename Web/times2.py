# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


htmlstart = '''
<!DOCTYPE html>
<html>
  <head>
    <style>
      html, body, div, form, fieldset, legend, label {margin: 0; padding: 0; }
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
        vertical-algin: middle;
      }
    </style>
  </head>
  <body>
'''

htmlend = '''
  </body>
  <script>


  </script>
</html>
'''


@Expose
def Request(self):
  yield
  
  W = self.HTMLResponse()
  W(htmlstart)
      
  W('<table>')

  for y in range(1,1001):
    W('<tr>')
    
    for x in range(1,13):
      W('<td>')
      W(str(x*y))
      W('</td>')
    
    W('</tr>')
  

  W('</table>')

  W(htmlend)

  yield W



