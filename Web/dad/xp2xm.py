# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *
import xp2xm


###############################################################################
@Expose
def Request(self):
  yield
 
  data = self.Post.data
  output = None

  for _ in ONCEIF(self.Post):
    try:
      output = xp2xm.convert(data.split("\n"))
    except Exception as e:
      self.UI.Error.Add(e)
  
  
  #============================================================================
  self.UI.Title = 'xp2xm UI'
  
  #============================================================================
  W = self.UI.Body('''
    <p>    
      This is a script based on the xp2xm library at <a href="https://github.com/appcove/xp2xm">https://github.com/appcove/xp2xm</a>.
    </p>

    <hr />

    <form name="F" method="post">
      <p>
        <strong>X-Path Expressions (one per line):</strong><br />
        <textarea name="data" rows="15" cols="60">''' + HS(data) + '''</textarea>
      </p>
      <p>
        <input type="submit" value="Convert" />
        or <a href=''' + QA(self.Env.ScriptPath) + '''>reset</a>
      </p>
    </form>

    ''' + ('''
      <hr />
      <h2>Output:</h2>
      <pre>''' + HS(output) + '''</pre>
    ''' if output else '') + '''

    ''')

  yield self.UI

  #============================================================================


