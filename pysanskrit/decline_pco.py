""" decline_pco.py
  Declensions of pronouns, cardinals
  Rather than orchestrating an algorithm joining of bases and suffixes,
  these classes read information from data files:
  decline_pron_data.txt, decline_card_data.txt
"""
import sys,re
import codecs

class PcoData(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  key,self.inflectionstr = line.split('\t')
  self.key = key
  m = re.search(r'^(.*?),([mfn])_(.*)$',key)
  self.headword = m.group(1)
  self.gender = m.group(2)
  self.lexid = m.group(3)
  # deserialize
  a = self.inflectionstr.split(':')
  assert len(a)==24
  b = []
  for x in a:
   y = x.split('/')
   if len(y) == 1:
    b.append(x)
   else:
    b.append(y)
  self.inflections = b

def init_pron_data(filein):
 import os 
 dir_path = os.path.dirname(os.path.realpath(__file__))
 pathin = '%s/%s' % (dir_path,filein)
 with codecs.open(pathin,"r","utf-8") as f:
  recs = [PcoData(x) for x in f if not x.startswith(';')]
 d = {}
 for rec in recs:
  d[rec.key] = rec
 return d 

class Decline_m_pron(object):
 """ declension table for pronouns in masculine gender
 """
 # class variable
 d = init_pron_data('decline_pron_data.txt')
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  datakey = '%s,%s' %(self.key2,'m_pron')
  d = Decline_m_pron.d
  if datakey in d:
   self.status = True
   rec = d[datakey]
   self.table = rec.inflections # list form
  else:
   self.status = False
   self.table = None

class Decline_f_pron(object):
 """ declension table for pronouns in feminine gender
 """
 # class variable
 d = init_pron_data('decline_pron_data.txt')
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  datakey = '%s,%s' %(self.key2,'f_pron')
  d = Decline_f_pron.d
  if datakey in d:
   self.status = True
   rec = d[datakey]
   self.table = rec.inflections
  else:
   self.status = False
   self.table = None

class Decline_n_pron(object):
 """ declension table for pronouns in neuter gender
 """
 # class variable
 d = init_pron_data('decline_pron_data.txt')
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  datakey = '%s,%s' %(self.key2,'n_pron')
  d = Decline_n_pron.d
  if datakey in d:
   self.status = True
   rec = d[datakey]
   self.table = rec.inflections
  else:
   self.status = False
   self.table = None

def init_card_data(filein):
 import os 
 dir_path = os.path.dirname(os.path.realpath(__file__))
 pathin = '%s/%s' % (dir_path,filein)
 with codecs.open(pathin,"r","utf-8") as f:
  recs = [PcoData(x) for x in f if not x.startswith(';')]
 d = {}
 for rec in recs:
  d[rec.key] = rec
 return d 

class Decline_m_card(object):
 """ declension table for cardinal numbers in masculine gender
 """
 # class variable
 d = init_card_data('decline_card_data.txt')
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  datakey = '%s,%s' %(self.key2,'m_card')
  d = Decline_m_card.d
  if datakey in d:
   self.status = True
   rec = d[datakey]
   self.table = rec.inflections # list form
   return
  # Word not directtly in the data file.
  # compute it as a compound
  head,base = self.splitkey2()
  datakey = '%s,%s' %(base,'m_card')
  if datakey in d:
   rec = d[datakey]
   table = rec.inflections # list form of base
   # concatenate head with table entries
   table1 = []
   for x in table:
    if x == '':
     item = ''
    elif isinstance(x,str):
     item = head + x
    else: # alternates, in list
     item = [(head+y) for y in x]
    table1.append(item)
   self.table = table1
   self.status = True
   return
  if self.key2 == 'saptAzwan':
   # same as previous, but take into account sandhi
   head = 'saptA'
   base = 'azwan'
   datakey = '%s,%s' %(base,'m_card')
   rec = d[datakey]
   table = rec.inflections # list form of base
   # concatenate head with table entries
   table1 = []
   for x in table:
    if x == '':
     item = ''
    elif isinstance(x,str):
     item = head + x[1:]  # saptA + zwa, for example
    else: # alternates, in list
     item = [(head+y[1:]) for y in x]
    #print('chk: x=',x,'item=',item)
    table1.append(item)
   self.table = table1
   self.status = True
   return
  # no luck   
  self.status = False
  self.table = None
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_f_card(object):
 """ declension table for cardinal numbers in feminine gender
 """
 # class variable
 d = init_card_data('decline_card_data.txt')
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  datakey = '%s,%s' %(self.key2,'f_card')
  d = Decline_f_card.d
  if datakey in d:
   self.status = True
   rec = d[datakey]
   self.table = rec.inflections
   return
  # Word not directtly in the data file.
  # compute it as a compound
  head,base = self.splitkey2()
  datakey = '%s,%s' %(base,'f_card')
  if datakey in d:
   rec = d[datakey]
   table = rec.inflections # list form of base
   # concatenate head with table entries
   table1 = []
   for x in table:
    if x == '':
     item = ''
    elif isinstance(x,str):
     item = head + x
    else: # alternates, in list
     item = [(head+y) for y in x]
    table1.append(item)
   self.table = table1
   self.status = True
   return
  # no luck
  self.status = False
  self.table = None
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_n_card(object):
 """ declension table for cardinal numbers in neuter gender
 """
 # class variable
 d = init_card_data('decline_card_data.txt')
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  datakey = '%s,%s' %(self.key2,'n_card')
  d = Decline_n_card.d
  if datakey in d:
   self.status = True
   rec = d[datakey]
   self.table = rec.inflections
  else:
   self.status = False
   self.table = None

