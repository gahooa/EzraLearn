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
        <th>Age</th>
        <th>age order</th>
      </tr>
      <tr>
        <td>Lesli</td>
        <td>?</td>
        <td>?</td>
      </tr>
      <tr>
        <td>Jason</td>
        <td>31</td>
        <td>2</td>
      </tr>
      <tr>
        <td>Jenn</td>
        <td>31</td>
        <td>3</td>
      </tr>
      <tr>
        <td>Eli</td>
        <td>11</td>
        <td>4</td>
      </tr>
      <tr>
        <td>Ezra</td>
        <td>9</td>
        <td>5</td>
      </tr>
      <tr>
        <td>zech</td>
        <td>6</td>
        <td>6</td>
      </tr>
      <tr>
        <td>Anna</td>
        <td>4</td>
        <td>7</td>
      </tr>
      <tr>
        <td>Iryna</td>
        <td>2</td>
        <td>8</td>
      </tr>
      <tr>
        <td>Lilia</td>
        <td>0</td>
        <td>9</td>
      </tr>
    </table

    <p>   
      They were on vacation.
      They were at france.
    </p>

    <p>
      The eiffel tower was big!
    </p>
    
    <p>
      They Missed ther grandparints.
    </p>

    <p>
      They were haveing a good time. 
    </p>
       
    <p>
      Wen it was time to go they were happy!
      The end
    </p>
   

    


''')

  yield self.UI


