# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *


@Expose
def Request(self):
  yield
  
  self.UI.Title = 'Age of the programers and famly'

  self.UI.Body('''
    
    <table class="List">
      <tr>
        <th>Name</th>
        <th>age</th>
        <th>Date</th>
      ``<th>Month</th>
      </tr>
      <tr>
        <td>Lesli</td>
        <td>unkown</td>
        <td>unknow</td>
        <itd>unknow</td>
      </tr>
      <tr>
        <td>Jason</td>
        <td>31</td>
        <td>1981</td>
        <td>July</td>
      </tr>
      <tr>
        <td>Jenn</td>
        <td>31</td>
        <td>1981</td>
        <td>unknow</td>
      </tr>
      <tr>
        <td>Isaac</td>
        <td>10</td>
        <td>2002</td>
        <td>February</td>
      </tr>
      <tr>
        <td>Eli</td>
        <td>10</td>
        <td>2002</td>
        <td>August</td>
      </tr>
      <tr>
        <td>Ezra</td>
        <td>8</td>
        <td>2004</td>
        <td>July</td>
      </tr>
      <tr>
        <td>Zech</td>
        <td>6</td>
        <td>2006</td>
        <td>December</td>
      </tr>
        <tr>
          <td>Anna</td>
          <td>4</td>
          <td>2008</td>
          <td>January</td>
      </tr>
      <tr>
         <td>Iryna</td>
         <td>1</td>
         <td>2012</td>
         <td>August</td>
       </tr>
    </table>
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ''')

  yield self.UI


