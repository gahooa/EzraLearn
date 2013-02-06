# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  self.UI.Title = 'Eli And Ezra Have A Pary'

  self.UI.Body('''

    <h3>Once a upon a time.</h3> 
    
    <p>
      There were two boys: one named Ezra and the other named Eli.
      Thay where having a party .
    </p>
      
    <p>
      Eli and Ezra had <big>pies</big> and <span style="color: red;">bear meat</span> and deer meet.
    </p>
   
   <p>
      But with out anebody noticing a pickpocket sneeks in!
   </p>

    <p>   
      The pickpocket stole a few girls wallets and a few boys wallets!!
    </p>
    
    <p>
      They did not notec!
    </p>
      
    <p>
      Eli noticed his wallet was gone. He gathered he checked evry body but nobody had his wallet.
    </p>

    <p>
      So he figured whene any body found out he or she wold cleer out of the place.
    </p>

    <p>
      Eli got Ezra and a girl named Anya and a nothere named Daniella to set up cameras above all shops and thay did. 
    </p>

    <p>
      So thay all had radios and camera video pads. 
    </p>

    <p>
      Eli Ezra Daniella and Anya had spy class so thay where spys.
    </p>

    <p>
      Finely thay cote the thef <span style="color: red;">red handed!</span> 
    </p>

    <p>
      The end.
    </p>






''')

  yield self.UI


