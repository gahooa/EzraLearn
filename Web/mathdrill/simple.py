# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


###############################################################################
@Expose
def Request(self):
  yield
 
  w1 = IN_Int(self.Get.w1) or 1
  w2 = IN_Int(self.Get.w2) or 12
  h1 = IN_Int(self.Get.h1) or 1
  h2 = IN_Int(self.Get.h2) or 12

 
  #============================================================================
  self.UI.Title = 'Simple Math Drill'
  
  #============================================================================
  self.UI.Style('''


    ''')
  #============================================================================
  self.UI.Script('''

    ''')
  
  #============================================================================
  W = self.UI.Body('''
    
    <div id="Left">
      <div class="_num">2</div>
      <div class="_op">+</div>
      <div class="_den">3</div>
      <div class="_ans">5</div>
    </div>




    ''')

  yield self.UI

  #============================================================================


