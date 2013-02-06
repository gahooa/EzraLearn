# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  Quarts = IN_Int(self.Get.Quarts)
  Pints = Quarts * 2
  Gallons = Quarts / 4

  self.UI.Title = 'Quarts to Pints'

  self.UI.Body('''
    
    <form method="get" action=''' + QA(self.Env.ScriptPath) + '''>
      
      <input type="text" name="Quarts" value=''' + QA(Quarts) + ''' /> Quarts <br />
      
      <input type="submit" value="Convert!" />

    </form>

    <hr />

    <h3>''' + HS(PLUR(Quarts, 'Quart')) + ''' is the same as ...</h3>
    <p>''' + HS(PLUR(Gallons, 'Gallon')) + '''</p>
    <p>''' + HS(PLUR(Pints, 'Pint')) + '''</p>
  
    
    ''')

  yield self.UI


