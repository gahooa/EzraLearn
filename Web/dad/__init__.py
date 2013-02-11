# vim:encoding=utf-8:ts=2:sw=2:expandtab

def Init(self):
  yield
  self.UI.Nav2.Add('/dad/boxes', Name='Boxes')
  self.UI.Nav2.Add('/dad/boxes_history', Name='Boxes History')
  self.UI.Nav2.Add('/dad/xp2xm', Name='xp2xm')
  yield
