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
  sups = self.getsups()
 def getsups(self):
  return self.sup.split(':') 

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

class Decline_n_i(object):
 """ declension table for neuter nouns ending in 'i'
sup-n-i=i:inI:Ini:i:inI:Ini:inA:iByAm:iBiH:ine:iByAm:iByaH:inaH:iByAm:iByaH:inaH:inoH:InAm:ini:inoH:izu:i,e:inI:Ini
 This declension has alternative endings.
 It forms the table from the base inflections as in Decline_f_i
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'i:inI:Ini:i:inI:Ini:inA:iByAm:iBiH:ine:iByAm:iByaH:inaH:iByAm:iByaH:inaH:inoH:InAm:ini:inoH:izu:i/e:inI:Ini'  
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

class Decline_m_u(object):
 """ declension table for masculine nouns ending in 'u'
sup-m-u=uH:U:avaH:um:U:Un:unA:uByAm:uBiH:ave:uByAm:uByaH:oH:uByAm:uByaH:oH:voH:UnAm:O:voH:uzu:o:U:avaH
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'uH:U:avaH:um:U:Un:unA:uByAm:uBiH:ave:uByAm:uByaH:oH:uByAm:uByaH:oH:voH:UnAm:O:voH:uzu:o:U:avaH'
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

class Decline_f_u(object):
 """ declension table for feminine nouns ending in 'u'
sup-f-u=uH:U:avaH:um:U:UH:vA:uByAm:uBiH:vE,ave:uByAm:uByaH:vAH,oH:uByAm:uByaH:vAH,oH:voH:UnAm:vAm,O:voH:uzu:o:U:avaH
 This declension has alternative endings.
 It forms the table from the base inflections by prepend_head method.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'uH:U:avaH:um:U:UH:vA:uByAm:uBiH:vE/ave:uByAm:uByaH:vAH/oH:uByAm:uByaH:vAH/oH:voH:UnAm:vAm/O:voH:uzu:o:U:avaH' 
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

class Decline_n_u(object):
 """ declension table for neuter nouns ending in 'u'
sup-n-u=u:unI:Uni:u:unI:Uni:unA:uByAm:uBiH:une:uByAm:uByaH:unaH:uByAm:uByaH:unaH:unoH:UnAm:uni:unoH:uzu:u,o:unI:Uni
 This declension has alternative endings.
 It forms the table from the base inflections as in Decline_f_i
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'u:unI:Uni:u:unI:Uni:unA:uByAm:uBiH:une:uByAm:uByaH:unaH:uByAm:uByaH:unaH:unoH:UnAm:uni:unoH:uzu:u/o:unI:Uni' 
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

class Decline_f_o(object):
 """ declension table for feminine nouns ending in 'o'
 declension for masculine nouns ending in 'o' is same.
 The code allows for alternate endings, though currently none are found
 It forms the table from the base inflections by prepend_head method.
Os:AvO:Avas:Am:AvO:As:avA:oByAm:oBis:ave:oByAm:oByas:os:oByAm:oByas:os:avos:avAm:avi:avos:ozu:Os:AvO:Avas 
"""
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'OH:AvO:AvaH:Am:AvO:AH:avA:oByAm:oBiH:ave:oByAm:oByaH:oH:oByAm:oByaH:oH:avoH:avAm:avi:avoH:ozu:OH:AvO:AvaH'  
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  # although known examples need to nR sandhi, we use it (via 
  # declension_join_simple).
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

class Decline_f_O(object):
 """ declension table for feminine nouns ending in 'O'
 declension for masculine nouns ending in 'O' is same.
 The code allows for alternate endings, though currently none are found;
 It forms the table from the base inflections by prepend_head method.
Os:AvO:Avas:Avam:AvO:Avas:AvA:OByAm:OBis:Ave:OByAm:OByas:Avas:OByAm:OByas:Avas:Avos:AvAm:Avi:Avos:Ozu:Os:AvO:Avas 
"""
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'OH:AvO:AvaH:Avam:AvO:AvaH:AvA:OByAm:OBiH:Ave:OByAm:OByaH:AvaH:OByAm:OByaH:AvaH:AvoH:AvAm:Avi:AvoH:Ozu:OH:AvO:AvaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  # although known examples need to nR sandhi, we use it (via 
  # declension_join_simple).
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

class Decline_m_e(object):
 """ declension table for masculine nouns ending in 'e'
 The code allows for alternate endings, though currently none are found;
 It forms the table from the base inflections by prepend_head method.
"""
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'eH:ayO:ayaH:ayam:ayO:ayaH:ayA:eByAm:eBiH:aye:eByAm:eByaH:eH:eByAm:eByaH:eH:ayoH:ayAm:ayi:ayoH:ezu:e:ayO:ayaH'  
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  # although known examples need to nR sandhi, we use it (via 
  # declension_join_simple).
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

  
