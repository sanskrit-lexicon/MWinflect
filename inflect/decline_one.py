""" decline_one.py
    Program dones one declension, printing declension table.
"""
from decline_file import DeclRec
import sys
def test(model,key2):
 key1 = key2.replace('-','')
 line = '%s\t%s\t%s' %(model,key2,'')
 decl = DeclRec(line)
 inflectionTable = decl.inflection  # string format
 #print inflectionTable
 if inflectionTable == None:
  print("Problem with declension of",model,key2)
  exit(1)
 table = inflectionTable.split(':')
 print("Declension of %s %s " %(model,key2))
 outarr = []
 for icell in range(0,24,3):
  a = []
  case = (icell // 3) + 1
  a.append('Case %d: ' % case)
  for i in range(0,3):
   x = table[icell+i]
   #if isinstance(x,list):
   # y = '/'.join(x)
   #else:
   # y = x
   #a.append(y)
   a.append(x)
  out = ' '.join(a)
  outarr.append(out)
 for out in outarr:
  print(out)

def test_md(model,key2):
 # generate a markdown table
 key1 = key2.replace('-','')
 line = '%s\t%s\t%s' %(model,key2,'')
 decl = DeclRec(line)
 inflectionTable = decl.inflection  # string format
 #print inflectionTable
 if inflectionTable == None:
  print("Problem with declension of",model,key2)
  exit(1)
 table = inflectionTable.split(':')
 print("Declension of %s %s " %(model,key2))
 outarr = []
 outarr.append('')
 outarr.append('|Case|S|D|P|')
 outarr.append('|-|-|-|-|')
 casenames = ['Nominative','Accusative','Instrumental',
  'Dative','Ablative','Genitive','Locative','Vocative']
 for icell in range(0,24,3):
  a = []
  case = (icell // 3) + 1
  #a.append('Case %d: ' % case)
  a.append(casenames[case-1])
  for i in range(0,3):
   x = table[icell+i]
   #if isinstance(x,list):
   # y = '/'.join(x)
   #else:
   # y = x
   #a.append(y)
   a.append(x)
  out = '|'.join(a)
  out = '|' + out + '|'
  outarr.append(out)
 for out in outarr:
  print(out)

def md1_explain(x,base,sup):
 " returns a string. x is the declined form"
 cat = base + sup
 if x == cat:
  ans = "%s + %s = **%s**" %(base,sup,x)
 else:
  ans = "%s + %s = %s -> **%s**" %(base,sup,cat,x)
 return ans

def md1_explain_alts(x,base,supstr):
 """ returns a string. x is the declined form
  assumes supstr contains alternates, separated by '/'
 """
 sups = supstr.split('/')
 cats = [base + sup for sup in sups]
 cat = '/'.join(cats)
 if x == cat:
  ans = "%s + %s = **%s**" %(base,supstr,x)
 else:
  ans = "%s + %s = %s -> **%s**" %(base,supstr,cat,x)
 return ans

def test_md1(model,key2):
 # generate a markdown table with explanations
 # This is implemented with only certain models
 if not model in ['m_a','n_a','f_A','f_I','f_U',
        'm_i','f_i','n_i', 'm_u','f_u','n_u', 'm_f','f_f','n_f',
        'f_o','m_o','f_O','m_O','m_e','m_E','f_E','n_E']:
  print('md1 not implemented for model=',model)
  return
 
 key1 = key2.replace('-','')
 line = '%s\t%s\t%s' %(model,key2,'')
 decl = DeclRec(line)
 inflectionTable = decl.inflection  # string format
 #print inflectionTable
 if inflectionTable == None:
  print("Problem with declension of",model,key2)
  exit(1)
 table = inflectionTable.split(':')
 print("Declension of %s %s " %(model,key2))
 outarr = []
 outarr.append('')
 outarr.append('|Case|S|D|P|')
 outarr.append('|-|-|-|-|')
 casenames = ['Nominative','Accusative','Instrumental',
  'Dative','Ablative','Genitive','Locative','Vocative']
 sups = decl.sups
 base = key1[0:-1] # drop last character -- only for certain models
 for icell in range(0,24,3):
  a = []
  case = (icell // 3) + 1
  #a.append('Case %d: ' % case)
  a.append(casenames[case-1])
  for i in range(0,3):
   x = table[icell+i]
   sup=sups[icell+i]
   if '/' not in sup:
    explain = md1_explain(x,base,sup)
   else:
    explain = md1_explain_alts(x,base,sup)
   a.append(explain)
  out = '|'.join(a)
  out = '|' + out + '|'
  outarr.append(out)
 for out in outarr:
  print(out)

if __name__ == "__main__":
 model = sys.argv[1]
 key2 = sys.argv[2]
 try:
  format = sys.argv[3]
 except:
  format = None
 if format == None:
  test(model,key2)
 elif format == 'md':
  test_md(model,key2)
 elif format == 'md1':
  test_md1(model,key2)
 else:
  print('Unknown format option',format)
  print('The format options are: md, md1')


