# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  W = self.TextResponse()

  for y in range(1,1001):
    for x in range(1,13):
      W("{0:6} ".format(x*y))
    W("\n\n\n")
  

  yield W


