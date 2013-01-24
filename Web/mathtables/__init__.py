# vim:encoding=utf-8:ts=2:sw=2:expandtab

def Init(self):
  yield
  self.UI.Nav2.Add('/mathtables/plus1', Name='Plus Table')
  self.UI.Nav2.Add('/mathtables/minus1', Name='Minus Table')
  self.UI.Nav2.Add('/mathtables/times1', Name='Times Table')
  self.UI.Nav2.Add('/mathtables/divide1', Name='Divide Table')
  yield
