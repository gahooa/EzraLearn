# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  self.UI.Title = 'Zech and Joe make a club '

  self.UI.Body('''

    <h3>Once a upon a time.</h3> 
    
    
    <p>
    There where to boys one was Zech the other was Joe.
    </p>
      Zech and Joe had a club but they needed to clean their room.     
    <p>
      They cleaned their room and made it a club room and calld there club J&Z.
    </p>
    
   <p>
     They had enemies there club was the MCC.
   </p>
      The MCC were not nice they stole the J&Z name tags. 
    <p>   
      Zech wrote a letter to Joe It said:Dear Joe I would like to come to your house.  Love Zech       
    </p>
      They had to defeat the MCC,so they called the GCC for reinforcemets. 
    <p>
      The GCC where there reinforcmets. 
    </p>
      
    <p>
      The GCC had a helcopter that would drop water bombs.
    </p>

    <p>
    They made maps to find out where enemies were.       
    </p>
      The GCC had one of the maps.
    <p>
      The J&Z are grond troops the GCC are air troops.
    </p>

    <p>
      The J&Z and GCC beat the MCC and put the MCC to jail. 
    </p>
      The J&Z got their name tags back. 
    <p>
      The end
    </p>
   
    


''')

  yield self.UI


