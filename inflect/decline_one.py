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
 else:
  print('Unknown format option',format)
  print('The format options are: md')


