"""decline.py
"""
from declension_join_simple import declension_join_simple
class Decline_ind(object):
 """ Makes a 1-table entry for indeclineables.
     Of course indeclineables are not declined,
     so this is just for making the indeclineables formally similar
     to declineables.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = ''
  self.status = True
  self.table = [self.key1]

class Decline_m_a(object):
 """ declension table for masculine nouns ending in 'a'
 sup-m-a=as:O:As:am:O:An:ena:AByAm:Es:Aya:AByAm:eByas:At:AByAm:eByas:asya:ayos:AnAm:e:ayos:ezu:a:O:As
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  #self.sup = 'as:O:As:am:O:An:ena:AByAm:Es:Aya:AByAm:eByas:At:AByAm:eByas:asya:ayos:AnAm:e:ayos:ezu:a:O:As'
  self.sup = 'aH:O:AH:am:O:An:ena:AByAm:EH:Aya:AByAm:eByaH:At:AByAm:eByaH:asya:ayoH:AnAm:e:ayoH:ezu:a:O:AH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  #print('Decline_m_a. init.',key1,key2)
   # for m_a, our sups assume final 'a' is removed from the base
  base1 = base[0:-1]
  #print('  head,base,base1 =',head,base,base1)
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base


# --------------------------------------
def test_m_a(key1,key2):
 decl = Decline_m_a(key1,key2)
 if not decl.status :
  print("Problem with declension of",key1,key2)
  exit(1)
 print("Decline_m_a(%s,%s) ->\n%s" %(key1,key2,decl.table))

if __name__ == "__main__":
 import sys
 key1 = sys.argv[1]
 if len(sys.argv) > 2:
  key2 = sys.argv[2]
 else:
  key2 = None
 test_m_a(key1,key2)

  
