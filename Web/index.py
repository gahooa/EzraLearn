# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield

  W = self.HTMLResponse()
  
  W('''
    <!DOCTYPE html>
    <html>
      <head>
        <title>Ezra's Learning Program</title>
        <style>
          body {font-family: verdana; }
        </style>
      </head>
      <body>

        <h1>Welcome to EzraLearn</h1>

        <hr />
        
        <h3>Dad's Stuff</h3>
        <p>
          <a href="/dad/times">Times Table</a> | 
          <a href="/dad/boxes">Color Boxes</a> 
          <br />
          <img src="/dad/boxes.png" />
        </p>

        <hr />

        <h3>Ezra's Stuff</h3>
        <p>
          <a href="/ezra/times0">Ezra's Times Program (0)</a> |
          <a href="/ezra/times1">Ezra's Times Program (1)</a> |
          <a href="/ezra/times2">Ezra's Times Program (2)</a>
        </p>
       </body>
     </html>

    ''')

  yield W


