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

class Decline_n_a(object):
 """ declension table for neuter nouns ending in 'a'
sup-n-a=am:e:Ani:am:e:Ani:ena:AByAm:Es:Aya:AByAm:eByas:At:AByAm:eByas:asya:ayos:AnAm:e:ayos:ezu:a:e:Ani
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2

  self.sup = 'am:e:Ani:am:e:Ani:ena:AByAm:EH:Aya:AByAm:eByaH:At:AByAm:eByaH:asya:ayoH:AnAm:e:ayoH:ezu:a:e:Ani' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # for n_a, our sups assume final 'a' is removed from the base
  base1 = base[0:-1]
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

class Decline_f_A(object):
 """ declension table for feminine nouns ending in 'A'
sup-f-A=A:e:AH:Am:e:AH:ayA:AByAm:ABiH:AyE:AByAm:AByaH:AyAH:AByAm:AByaH:AyAH:ayoH:AnAm:AyAm:ayoH:Asu:e:e:AH

 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'A:e:AH:Am:e:AH:ayA:AByAm:ABiH:AyE:AByAm:AByaH:AyAH:AByAm:AByaH:AyAH:ayoH:AnAm:AyAm:ayoH:Asu:e:e:AH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
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

class Decline_f_I(object):
 """ declension table for feminine nouns ending in 'I'
sup-f-I=I:yO:yaH:Im:yO:IH:yA:IByAm:IBiH:yE:IByAm:IByaH:yAH:IByAm:IByaH:yAH:yoH:InAm:yAm:yoH:Izu:i:yO:yaH

 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'I:yO:yaH:Im:yO:IH:yA:IByAm:IBiH:yE:IByAm:IByaH:yAH:IByAm:IByaH:yAH:yoH:InAm:yAm:yoH:Izu:i:yO:yaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
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

class Decline_f_U(object):
 """ declension table for feminine nouns ending in 'U'
sup-f-U=UH:vO:vaH:Um:vO:UH:vA:UByAm:UBiH:vE:UByAm:UByaH:vAH:UByAm:UByaH:vAH:voH:UnAm:vAm:voH:Uzu:u:vO:vaH
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'UH:vO:vaH:Um:vO:UH:vA:UByAm:UBiH:vE:UByAm:UByaH:vAH:UByAm:UByaH:vAH:voH:UnAm:vAm:voH:Uzu:u:vO:vaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
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

class Decline_m_i(object):
 """ declension table for masculine nouns ending in 'i'
sup-m-i=iH:I:ayaH:im:I:In:inA:iByAm:iBiH:aye:iByAm:iByaH:eH:iByAm:iByaH:eH:yoH:InAm:O:yoH:izu:e:I:ayaH
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'iH:I:ayaH:im:I:In:inA:iByAm:iBiH:aye:iByAm:iByaH:eH:iByAm:iByaH:eH:yoH:InAm:O:yoH:izu:e:I:ayaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
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

class Decline_f_i(object):
 """ declension table for feminine nouns ending in 'i'
sup-f-i=iH:I:ayaH:im:I:IH:yA:iByAm:iBiH:yE,aye:iByAm:iByaH:yAH,eH:iByAm:iByaH:yAH,eH:yoH:InAm:yAm,O:yoH:izu:e:I:ayaH
 This declension has alternative endings.
 It forms the table from the base inflections by prepend_head method,
    which generalizes string concatenation used in previous algorithms.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'iH:I:ayaH:im:I:IH:yA:iByAm:iBiH:yE/aye:iByAm:iByaH:yAH/eH:iByAm:iByaH:yAH/eH:yoH:InAm:yAm/O:yoH:izu:e:I:ayaH' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
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
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

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

  
