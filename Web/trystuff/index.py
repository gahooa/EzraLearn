# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  self.UI.Title = 'Try Stuff'

  self.UI.Body('''
    Look at the menu :)   
  
    
    ''')

  yield self.UI


