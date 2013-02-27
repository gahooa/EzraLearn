# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  self.UI.Title = 'Stories'

  self.UI.Body('''
    <h2>Eli And Ezra Go Deer Hunting</h2>
    <p>A story about Eli and Ezra going hunting and getting attacked by a bear!  Written by Eli and Ezra.</p>
    <a href="/story/eli_ezra_bear_1">Read the Story</a>
    <hr />
    
    <h2>Eli And Ezra Have A Party</h2>
    <p>A story about Eli and Ezra having a party and a pickpocket comes!  Written by Eli and Ezra.</p>
    <a href="/story/eli_ezra_bear_2">Read the Story</a>
    <hr />
    
    <h2>Zech And Joe Make A Club</h2>
    <p>A story about Zech and Joe Making A Club And Defeating Their Worst Enemy!</p>
    <a href="/story/zech_joe_club_1">Read the Story</a>
    <hr />
   
    <h2>Ezra And The Rest Of The GCC Club</h2>
    <p>A story about Ezra and The GCC club Defeating their worst enemy!</p>
    <a href="/story/ezra_story_club_1">Read the Story</a>
    <hr />
   
    <h2>Eli Story About Police classis</h2>
    <p>A story about Eli takeing police classes with buddies.</p>
    <a href="/story/eli_story_1">Read the Story</a>
    <hr />
     
    <h2>Ezra Story About His Family</h2>
    <p>A story about Ezra family</p>
    <a href="/story/ezra_story_2">Read the Story</a>
    <hr />
 
       
    <h2>Eli Story About trip</h2>
    <p>A story about Eli takeing a trip with buddies and fighting outlaws .</p>
    <a href="/story/eli_story_2">Read the Story</a>
    <hr />

 
 
 ''')

  yield self.UI










