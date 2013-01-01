# vim:encoding=utf-8:ts=2:sw=2:expandtab


###############################################################################
# Create the project
Project = Instance.Project.Add('EzraLearn')

# THIS IS ACTUALLY POSTGRES
Project.MySQL.Password = 'sdkfsaldjfsldkjf324r234'

Project.OtherData['FileServer_Host']     = 'file.izrm.net'
Project.OtherData['FileServer_Database'] = Project.MySQL.Database

Project.OtherData['JM_Username'] = 'appcove'
Project.OtherData['JM_Password'] = '???'

# Setup HTTP/HTTPS
VH1 = Project.VirtualHost.Add('http:ezralearn')
VH1.ServerName = 'ezralearn'
VH1.DocumentRoot = './Web'
VH1.IP = '127.0.0.1'
VH1.Port = 8125

Project.OtherData['URL_HTTP'] = VH1.URL

if Instance.DevLevel == 0:
  Project.OtherData['URL_HTTPS'] = VH1.URL.replace('http:', 'https:')
else:
  Project.OtherData['URL_HTTPS'] = VH1.URL

WSGI_Daemon_Name = 'Port{0}'.format(VH1.Port)

threads = ('1' if Instance.DevLevel == 0 else '1')
processes = ('1' if Instance.DevLevel == 0 else '1')

Instance.Apache.Conf += [
  'Listen 127.0.0.1:{0}'.format(VH1.Port),
  'NameVirtualHost 127.0.0.1:{0}'.format(VH1.Port),
  'WSGIDaemonProcess ' + WSGI_Daemon_Name + ' processes=' + processes + ' threads=' + threads + ' python-path=' + abspath('./Python')
  ]

# When mixing RewriteRule with WSGI, and NOT using [R], you need to use the [PT,L] directive
# http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html  -- search for [PT]

extra = [
  'AddDefaultCharset UTF-8',
  
  'RewriteEngine on',
  

  # CRITICAL: just to prevent the posiblity of revealing python code in the document root
  'RewriteRule \.(py|pyc|pyo|wsgi)$  -  [F]', 
  
  # WSGI Settings
  'WSGIScriptAlias / '                  + abspath('./Web/index.wsgi'),
  'WSGIProcessGroup '                   + WSGI_Daemon_Name,
  ]

if Instance.DevLevel > 0:
  extra += [
    'LogLevel info',
    'ErrorLog ' + abspath('./apache-error.log'),
    ]

VH1.Extra += extra


###############################################################################
# Specify what _Auto files to run (later)
AutoConf('_Auto.py', Project=Project)



