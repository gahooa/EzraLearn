# vim:encoding=utf-8:ts=2:sw=2:expandtab

def Init(self):
  yield
  self.UI.Nav2.Add('/trystuff/table', Name='Table')
  self.UI.Nav2.Add('/trystuff/quarts', Name='Quarts')
  self.UI.Nav2.Add('/trystuff/gallons', Name='Gallons')
  yield
