# vim:encoding=utf-8:ts=2:sw=2:expandtab
#
# Copyright 2013 AppCove, Inc.                                                
#                                                                            
# Licensed under the Apache License, Version 2.0 (the "License");            
# you may not use this file except in compliance with the License.           
# You may obtain a copy of the License at                                    
#                                                                            
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

'''
Sample input data:
  
  /data/customer/name
  /data/customer/address
  /data/customer/city
  /data/customer/state
  /data/customer/zip
  /data/customer/phone/residential
  /data/customer/phone/comercial
  /data/file/createdate
  /data/file/deleted
  /data/file/deletedate

Sample output data:
  
  <data>
    <customer>
      <name/>
      <address/>
      <city/>
      <state/>
      <zip/>
      <phone>
        <residential/>
        <comercial/>
      </phone>
    </customer>
    <file>
      <createdate/>
      <deleted/>
      <deletedate/>
    </file>
  </data>

'''
import re
from collections import OrderedDict
from xml.etree import ElementTree as ET
from xml.dom import minidom as MD

def _xml(element, data):
  for k,v in data.items():
    _xml(ET.SubElement(element, k), v)

def convert(lines,*, Output='prettyxml', Limit=100000, PartRegex='^[a-zA-Z0-9_-]{1,64}$', RootName='document', IgnoreParts=1):
  
  if Output not in('xml', 'prettyxml', 'dict'):
    raise ValueError('Parameter `Output` is invalid: {0}'.format(Output))  
  
  i = 0
  
  matcher = re.compile(PartRegex)

  root = OrderedDict()

  for line in lines:
    line = line.strip()
    if line == '':
      continue

    parts = line.split('/')[IgnoreParts:]
    
    d = root
    for part in parts:
      i += 1
      if i > Limit:
        raise ValueError('Input exceeded {0} parts.'.format(Limit))
      
      if not matcher.match(part):
        raise ValueError('Input error: xpath name is does not match /{0}/: {1}'.format(PartRegex, part))      

      if part not in d:
        d[part] = OrderedDict()
      d = d[part]

  if Output == 'dict':
    return root
  
  doc = ET.Element(RootName)

  _xml(doc, root)
  
  xmlstring = ET.tostring(doc, encoding='unicode', method="xml")

  if Output == 'xml':
    return xmlstring
  
  if Output == 'prettyxml':
    return str(MD.parseString(xmlstring).toprettyxml())






