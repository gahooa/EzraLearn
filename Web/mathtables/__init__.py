# vim:encoding=utf-8:ts=2:sw=2:expandtab

def Init(self):
  yield
  self.UI.Nav2.Add('/mathtables/plus', Name='Plus Table')
  self.UI.Nav2.Add('/mathtables/minus', Name='Minus Table')
  self.UI.Nav2.Add('/mathtables/times', Name='Times Table')
  self.UI.Nav2.Add('/mathtables/divide', Name='Divide Table')
  yield
