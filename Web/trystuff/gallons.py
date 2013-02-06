# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  Gallons = IN_Int(self.Get.Gallons)
  Quarts = Gallons * 4

  self.UI.Title = 'Gallons to Quarts'

  self.UI.Body('''
    
    <form method="get" action=''' + QA(self.Env.ScriptPath) + '''>
      
      <input type="text" name="Gallons" value=''' + QA(Gallons) + ''' /> Gallons<br />
      
      <input type="submit" value="Convert!" />

    </form>

    <hr />

    <h2>Result</h2>
    ''' + HS(PLUR(Gallons, 'Gallon')) + ''' 
    is the same as 
    ''' + HS(PLUR(Quarts, 'Quart')) + '''.
  
    
    ''')

  yield self.UI


