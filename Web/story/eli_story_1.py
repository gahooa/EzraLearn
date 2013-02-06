# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  self.UI.Title = 'Ezra Eli Daniella and Anya take spy classes'

  self.UI.Body('''

    <h3>Once a upon a time.</h3> 
    
    <hr />
    
    <p>
      There where for kids named Eli and Ezra and Anya and Daniella.  
      They where takeing ploice classis. 
    </p>
    
    <p>
      Thay started a club calld GCC            
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
       
      <table class="List">
      <tr>
        <th>Name</th>
        <th>Age</th>
        <th>Position</th>
      </tr>
    
      <tr>   
        <td>Eli</td>
        <td>M4</td>
        <td>Grond troop</td>
        </tr>  
      <tr>
        <td>Daniella</td>
        <td>M4</td>
        <td>Grond troop</td>
      </tr>
       
      <tr>
        <td>Ezra</td>
        <td>driver</td>
        <td>arey troop</td>
      </tr>
      
     <p>   
      <td>Anya</td>
      <td>Miny gun</td>
      <td>arey troop</td>
     </tr>
    <p>
      Thay got a nufe munny to by beebee gunes.
      Now that thay got beebee gunes thay will defet there worst anmy.
    </p>
       
    <p>
    
    </p>

    <p>
    
    </p>
    
    <p>
    
    </p>
   
    


''')

  yield self.UI


