# vim:encoding=utf-8:ts=2:sw=2:expandtab
"""
App Instance:
  Instance holds all data
  Attributes are all per-thread
  Class attributes are read-only


"""
from AppStruct.Util import *
from AppStruct.WSGI.Util import *

import AppStruct.Application
import AppStruct.Util
import AppStruct.WSGI.Util
import AppStruct.Database.PostgreSQL
import AppStruct.Database.Redis
import AppStruct.Date
import AppStruct.Data.Validator

import locale
from decimal import Decimal
import re



###############################################################################
# Global Utility Functions


# Date Long Text
def DLT(DateObject, NoneText='None'):
  return DateObject.strftime('%b %d, %Y') if DateObject else NoneText

# Time Long Text
def TLT(DateTimeObject, NoneText='None'):
  return DateTimeObject.strftime('%b %d, %Y %I:%M %p %z') if DateTimeObject else NoneText

# Decimal format for input
def DFI(Num):
  Num = re.sub('[^0-9.]', '', str(Num))
  return ('0.00' if Num == '' else "%.2f" % Decimal(Num))

# Decimal signed format for input
def DSFI(Num):
  Num = re.sub('[^0-9.-]', '', str(Num))
  return ('0.00' if Num == '' else "%.2f" % Decimal(Num))

# Output Decimal Value
def DFO(Num):
  locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
  Num = str(Num).strip()
  return locale.format("%.2f",(0.00 if Num == '' else Decimal(Num)),grouping=True)

# Integer format for input
def IFI(Num):
  Num = re.sub('[^0-9.]', '', str(Num))
  return "%.0f" % (0.00 if Num == '' else Decimal(Num))

# Output Integer Value
def IFO(Num):
  locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
  Num = str(Num).strip()
  return locale.format("%.0f",(0.00 if Num == '' else Decimal(Num)),grouping=True)

# Output currency value
def CUR(Num):
  locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
  return ('$0.00' if str(Num).strip() == '' else locale.currency(Decimal(Num),grouping=True))

def ELIP(string, length):
  string = str(string).strip()
  length = int(length)

  return (string if len(string) <= length else (string[0:int(length - 3)] + '...'))


###############################################################################

@ConvertToInstance
class App(AppStruct.Application.ThreadedApp):
  from EzraLearn_Local import Path, DevLevel, Identifier
  from EzraLearn_Local import URL_HTTP, URL_HTTPS, CacheTime
  from EzraLearn_Local import Database
  
  
  #============================================================================
  
  Date = AppStruct.Date.DateIO()  # This is threadsafe
  
  #============================================================================
  
  Setting = aadict()  # This is to be read-only outside of the initial load

  #============================================================================
  def __init__(self):
    """
    Due to the fact that this is a threading.Local instance, this is called once
    in each thread.
    """
    print("App Init caled on {0}".format(self))
    super().__init__()

    self._DB = None
    self._Redis = None
    self._SC = None
    self._Opened = False

  #============================================================================
  def Open(self):
    self._SC = None

#    # Create Database Connection
#    if self._DB == None or self._DB.state in ('closed', ):
#      self._DB = AppStruct.Database.PostgreSQL.Open(
#        host = self.Database['Host'],
#        user = self.Database['Username'],
#        password = self.Database['Password'],
#        database = self.Database['Database'],
#        )
#
#      self._DB.Execute('''set search_path = "Main" ''');
#
#    if self._Redis == None:
#      self._Redis = AppStruct.Database.Redis.Redis(db=App.DevLevel)
    
    self._Opened = True

  #============================================================================
  def Close(self):
    self._Opened = False
    self._SC = None


#  #============================================================================
#  @property
#  def DB(self):
#    if not self._Opened:
#      raise RuntimeError("App has not been opened with App.Open()")
#    if not self._DB:
#      raise RuntimeError("Database Connection Not Available.  Create one with App.Open().")
#    return self._DB
  
#  #============================================================================
#  @property
#  def Redis(self):
#    if not self._Opened:
#      raise RuntimeError("App has not been opened with App.Open()")
#    if not self._Redis:
#      raise RuntimeError("Redis Connection Not Available.  Create one with App.Open().")
#    return self._Redis



###############################################################################
# Load the settings


###############################################################################
# Define all of the gloabls that will be imported with *

__all__ = \
  AppStruct.Util.__all__ + \
  AppStruct.WSGI.Util.__all__ + \
  (
    'App',
    'DLT',
    'TLT',
    'DFI',
    'DFO',
    'IFI',
    'IFO',
    'CUR',
    'ELIP',
  )



