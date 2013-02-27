# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  self.UI.Title = ''

  self.UI.Body('''

    <h3>Once a upon a time.</h3> 
    
    <hr />
    
    <p>
      There were four kids named Eli, Ezra, Anya, and Daniella.  
      They were going on a trip to texis. 
    </p>
    
    <p>
    
    </p>
    
    <table class="List">
      <tr>
        <th>Name</th>
        <th>Age</th>
        <th>Position</th>
      </tr>
      
      <tr>
        <td>Eli</td>
        <td>10</td>
        <td>Member</td>
      </tr>
      
      <tr>
        <td>Daniella</td>
        <td>10</td>
        <td>Member</td>
      </tr>
      
      <tr>
        <td>Ezra</td>
        <td>8</td>
        <td>Leder</td>
      </tr>
    
      <tr>
        <td>Anya</td>
        <td>7</td>
        <td>Member</td>
      </tr>
    
    </table>
       
    <p>
    
    </p>
     
     <p> 
    
    </p>
     
     <p>
     
     </p>
    
    <p>
    
    </p>
   
    <p>
    
    </p>
''')

  yield self.UI


