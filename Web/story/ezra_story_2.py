# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  self.UI.Title = 'Ezra\'s famely.'

  self.UI.Body('''

    <h3>Once a upon a time.</h3> 
    
    
    <p>
     There was a boy named ezra. 
     He had a big family. 
    
       
    <table class="List">
      <tr>
        <th>Name</th>
        <th>last name</th>
        <th>age</th>
      </tr>
      <tr>
        <td>mr.bonkcymcbean</td>
        <td>?bean</td>
        <td>10000099</td>
      </tr>
        
     <p>  
      
    </p>

    <p>
      
    </p>
    
    <p>
  
   </p>

    


''')

  yield self.UI


