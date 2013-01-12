# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield

  W = self.HTMLResponse()
  
  W('''
    <h1>Welcome to EzraLearn</h1>
    
    <p>
      <a href="/dad/times">Dad's Times Program</a>
    </p>

    <p>
      <a href="/ezra/times0">Ezra's Times Program (0)</a> |
      <a href="/ezra/times1">Ezra's Times Program (1)</a> |
      <a href="/ezra/times2">Ezra's Times Program (2)</a>
    </p>


    ''')

  yield W


