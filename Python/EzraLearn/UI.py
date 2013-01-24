# vim:encoding=utf-8:ts=2:sw=2:expandtab

from EzraLearn import *

from AppStruct.UI.Lib import StringBuilder, SimpleMenu, ErrorList, InfoList, CSSList, JSList
from AppStruct.WSGI.Response import LayoutResponse


###############################################################################
class Desktop(LayoutResponse):

  #============================================================================
  def __init__(self, *, Header):
    # Remember, Header, Status, and Buffer are reserved by the baseclass

    super().__init__(self, Header=Header)
    
    self.TitlePrefix = ''
    self.Title = ''
    self.FooterHTML = ''
  
    self.Error = ErrorList()
    self.Info = InfoList()
    self.Nav1 = SimpleMenu()
    self.Nav2 = SimpleMenu()

    self.Head = StringBuilder()
    self.Body = StringBuilder()
    self.Tail = StringBuilder()
    self.Script = StringBuilder()
    self.Style = StringBuilder()

    self.CSS = CSSList()
    self.JS = JSList()

    
  #============================================================================
  def Process(self):
    self.Buffer.write('''
<!DOCTYPE html>
<html>
<head>
  <title>''' + HS(self.TitlePrefix + (' > ' + self.Title if self.Title else '')) + '''</title>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
  ''' + self.CSS.HTML() + '''
  <style>''' + self.Style.Value + '''</style>
  ''' + self.Head.Value + '''
</head>
<body>
  <div id="UI_Header">
    <div id="UI_Title">''' + HS(self.TitlePrefix + (' > ' + self.Title if self.Title else '')) + '''</div>
    <!-- <img src="/assets/....png" class="Logo" /> -->
  </div>
  
  ''' + ('''
    <div id="UI_Nav1">
    ''' + (''.join(('<a href=' + QA(MI.URL) + '>' + HS(MI.Name) + '</a>' for MI in self.Nav1))) + '''
    </div>
  ''' if len(self.Nav1) else '') + '''
  
  ''' + ('''
    <div id="UI_Nav2">
    ''' + (''.join(('<a href=' + QA(MI.URL) + '>' + HS(MI.Name) + '</a>' for MI in self.Nav2))) + '''
    </div>
  ''' if len(self.Nav2) else '') + '''
  
  <div id="UI_Content">
    ''' + ('''
      <div id="UI_Error">
        <div>Error Message:</div>
        <ul>''' + self.Error.HTML() + '''</ul>
      </div>
    ''' if len(self.Error) else '') + '''
    
    ''' + ('''
      <div id="UI_Info">
        <div>Information:</div>
        <ul>''' + self.Info.HTML() + '''</ul>
      </div>
    ''' if len(self.Info) else '') + '''

    <div id="UI_Body">''' + self.Body.Value + '''</div>
    
    <div style="clear: both;"></div>

  </div>
 
  <div id="UI_Footer">''' + self.FooterHTML + '''</div>
  
  ''' + self.Tail.Value + '''
  ''' + self.JS.HTML() + '''
  <script>''' + self.Script.Value + '''</script>
</body>
</html>
    ''')


