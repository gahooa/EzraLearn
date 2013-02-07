# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *

import decimal


@Expose
def Request(self):
  yield
  
  try:
    Value = decimal.Decimal(self.Get.Value)
  except decimal.InvalidOperation:
    Value = decimal.Decimal(0)

  Unit = self.Get.Unit

  if Unit == '':
    Converted = False
  
  elif Unit == 'Feet':
    Converted = True
    Feet = Value
    Yards = Feet / 3
    Miles = Feet / 5280

  elif Unit == 'Yards':
    Converted = True
    Yards = Value
    Feet = Yards * 3
    Miles = Yards * 3 / 5280

  else:
    Converted = False
    self.UI.Error.Add('Please select a Unit...')


  self.UI.Title = 'Length/Distance Conversions'

  self.UI.Body('''
    
    <form method="get" action=''' + QA(self.Env.ScriptPath) + '''>
      
      <input type="text" name="Value" value=''' + QA(Value) + ''' /> 

      <select name="Unit">
        ''' + HS_Option('', Label='(Select Unit)', Selected=Unit=='') + '''
        ''' + HS_Option('Feet', Label='Feet', Selected=Unit=='Feet') + '''
        ''' + HS_Option('Yards', Label='Yards', Selected=Unit=='Yards') + '''
      </select>
      
      <input type="submit" value="Convert!" />

    </form>
    
    ''' + ('''
      <hr />

      <h2>''' + HS(Value) + ' ' + HS(Unit) + ''' is the same as:</h2>
      
      <p>''' + HS(PLUR(Feet, 'Foot', 'Feet')) + '''</p>
      <p>''' + HS(PLUR(Yards, 'Yard')) + '''</p>
      <p>''' + HS(PLUR(Miles, 'Mile')) + '''</p>
    
    ''' if Converted else '') + '''
    


    ''')

  yield self.UI


