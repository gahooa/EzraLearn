# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
 
  W = self.HTMLResponse()

  W('Hey <strong>There</strong>')

  yield W



