# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  self.UI.Title = 'Stories'

  self.UI.Body('''
    <h2>Eli And Ezra Go Deer Hunting</h2>
    <p>A story about Eli and Ezra going hunting and getting attacked by a bear!  Written by Eli and Ezra.</p>
    <a href="/story/eli_ezra_bear_1">Read the Story</a>
    <hr />
    
    ''')

  yield self.UI


