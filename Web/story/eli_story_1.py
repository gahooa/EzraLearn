# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  self.UI.Title = 'Ezra Eli Daniella and Anya take ploice classes'

  self.UI.Body('''

    <h3>Once a upon a time.</h3> 
    
    <hr />
    
    <p>
      There were four kids named Eli, Ezra, Anya, and Daniella.  
      They were taking police classes. 
    </p>
    
    <p>
      Thay started a club calld GCC.            
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
        <td>Member</td>
      </tr>
    
      <tr>
        <td>Anya</td>
        <td>7</td>
        <td>Leder</td>
      </tr>
    
    </table>
       
      <table class="List">
      <tr>
        <th>Name</th>
        <th>Gun</th>
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
        <td>air troop</td>
      </tr>
      
     <p>   
      <td>Anya</td>
      <td>Miny gun</td>
      <td>air troop</td>
     </tr>
    <p>
      They got a enough money to by BB guns.
      Now that they got BB guns teay will defeat their worst enemy.
    </p>
      Their worst enemy were the DER. 
      They stole all the GCC's money.
     <p> 
      They went to the castle of DER.
      Daniella and Eli snuk into the castle of DER. 
    </p>
     
     <p>
      Eli and Daniella captured some of the guards.
      They threw the guards out side. 
     </p>
      Mean wile Anya and Ezra made the castle of DER give up.
    <p>
      The GCC wone the war!
    </p>
   
    <p>
      The GCC got there money back. 
      The End
    </p>
''')

  yield self.UI


