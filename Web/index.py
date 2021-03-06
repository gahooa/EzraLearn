# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield

  self.UI.Body('''
    <h1>Welcome to EzraLearn</h1>

    <h2>Save the Princess</h2>
    <p>A new short video ...</p>
    <iframe width="420" height="315" src="http://www.youtube.com/embed/WMV5hKCchUo" frameborder="0" allowfullscreen></iframe>

    <hr />

    <h2>A new video on a new drill!</h2>
    <iframe width="560" height="315" src="http://www.youtube.com/embed/Wd6pRQgrqnk" frameborder="0" allowfullscreen></iframe>
    
    
    <hr />
    
    <h3>Dad's Stuff</h3>
    <p>
      <a href="/dad/times">Times Table</a> &bull;
      <a href="/dad/boxes">Color Boxes</a> &bull;
      <a href="/dad/boxes_history">Color Boxes History</a> 
      <br />
      <img src="/assets/boxes.png" />
    </p>

    <hr />

    <h3>Ezra's Stuff</h3>
    <p>
      <a href="/ezra/times0">Ezra's Times Program (0)</a> 
      &bull;
      <a href="/ezra/times1">Ezra's Times Program (1)</a> 
      &bull;
      <a href="/ezra/plus1">Ezra's Plus Program (1)</a> 
      &bull;
      <a href="/ezra/minus1">Ezra's Minus Program (1)</a>
      &bull;
      <a href="/ezra/divide1">Ezra's Divide Program (1)</a>
    </p>

    ''')

  yield self.UI


