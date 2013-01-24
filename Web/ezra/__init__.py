# vim:encoding=utf-8:ts=2:sw=2:expandtab

def Init(self):
  yield
  self.UI.Nav2.Add('/ezra/plus1', Name='Plus Table')
  self.UI.Nav2.Add('/ezra/minus1', Name='Minus Table')
  self.UI.Nav2.Add('/ezra/times1', Name='Times Table')
  self.UI.Nav2.Add('/ezra/divide1', Name='Divide Table')
  yield
