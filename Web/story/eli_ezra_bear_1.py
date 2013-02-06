# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  self.UI.Title = 'Eli And Ezra Go Deer Hunting'

  self.UI.Body('''

    <h3>Once a upon a time.</h3> 
    <p>
      There where too, boys one named Ezra and the other was Eli.
      Thay where hunting for deer.
    </p>
      
    <img src="http://upload.wikimedia.org/wikipedia/en/thumb/c/c2/White-tail_deer.jpg/220px-White-tail_deer.jpg" />

    <p>
      And then a big bad bear atacked them. 
    </p>

    <img src="http://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Medved_mzoo.jpg/220px-Medved_mzoo.jpg" />

    <p>

      luckle Eli had his glok knife out and he stabed the bear.
    </p>
   


    <img src="http://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Glock_Feldmesser_FM_78.JPG/300px-Glock_Feldmesser_FM_78.JPG" />

    <p>
      Then Ezra and Eli skined the bear and took it home. 
    </p>


    <img src="http://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Ranch_style_home_in_Salinas%2C_California.JPG/200px-Ranch_style_home_in_Salinas%2C_California.JPG" />

  <p>
    The next day Ezra and Eli went hunting for deer agan and thay got one! 
  </p>



<img src="http://upload.wikimedia.org/wikipedia/en/thumb/c/c2/White-tail_deer.jpg/220px-White-tail_deer.jpg" />



    <p>
      Eli and Ezra took the deer home and skined it.
    </p>

      <img src="http://upload.wikimedia.org/wikipedia/en/thumb/c/c2/White-tail_deer.jpg/220px-White-tail_deer.jpg" />


    <p>
     The next day thay sesend the bear and deer. 
    </p>
    
    

    <img src="http://upload.wikimedia.org/wikipedia/en/thumb/c/c2/White-tail_deer.jpg/220px-White-tail_deer.jpg" />


    <img src="http://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Medved_mzoo.jpg/220px-Medved_mzoo.jpg" />

    <p>
      After the deer and bear finshd being sesend Eli and Ezra had a party.
      The end
    </p>






''')

  yield self.UI


