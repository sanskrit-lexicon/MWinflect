""" decline_file.py
"""
import sys,re,codecs
sys.path.append('../pysanskrit')
import decline # from pysanskrit
import decline_f # from pysanskrit
#import decline_pco # from pysanskrit
#import decline_2stem # from pysanskrit
#import decline_3stem # from pysanskrit
#import decline_1stem # from pysanskrit
class DeclRec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.model,self.key2,self.refs) = line.split('\t')
  self.key1 = self.key2.replace('-','')
  self.inflection = None
  self.sups = None
  self.inflect()
 def inflect(self):
  if self.model == 'ind':
   decl = decline.Decline_ind(self.key1,self.key2)
  elif self.model == 'm_a':
   decl = decline.Decline_m_a(self.key1,self.key2)
  elif self.model == 'n_a':
   decl = decline.Decline_n_a(self.key1,self.key2)
  elif self.model == 'f_A':
   decl = decline.Decline_f_A(self.key1,self.key2)
  elif self.model == 'f_I':
   decl = decline.Decline_f_I(self.key1,self.key2)
  elif self.model == 'f_U':
   decl = decline.Decline_f_U(self.key1,self.key2)
  elif self.model == 'm_i':
   decl = decline.Decline_m_i(self.key1,self.key2)
  elif self.model == 'm_u':
   decl = decline.Decline_m_u(self.key1,self.key2)
  elif self.model == 'f_i':
   decl = decline.Decline_f_i(self.key1,self.key2)
  elif self.model == 'f_u':
   decl = decline.Decline_f_u(self.key1,self.key2)
  elif self.model == 'n_i':
   decl = decline.Decline_n_i(self.key1,self.key2)
  elif self.model == 'n_u':
   decl = decline.Decline_n_u(self.key1,self.key2)
  elif self.model in ['m_o','f_o']:  
   # masculine same as feminine. There is no neuter,
   # since the stem for neuter ending in o is changed to stem ending in u
   # by stem_model.py in inputs/nominals.
   decl = decline.Decline_f_o(self.key1,self.key2)
  elif self.model in ['m_O','f_O']:  
   # masculine same as feminine. There is no neuter,
   # since the stem for neuter ending in O is changed to stem ending in u
   # by stem_model.py in inputs/nominals.
   decl = decline.Decline_f_O(self.key1,self.key2)
  elif self.model in ['m_e']:  
   # Assume feminine and neuter stems replace 'e' with 'i';
   # This is done in stem_model.py in inputs/nominals
   decl = decline.Decline_m_e(self.key1,self.key2)
  elif self.model in ['m_E','f_E']:  
   # Masculine and feminine the same 
   decl = decline.Decline_m_E(self.key1,self.key2)
  elif self.model in ['n_E']:  
   decl = decline.Decline_n_E(self.key1,self.key2)
  elif self.model in ['m_F','f_F']:  
   # Masculine and feminine the same 
   decl = decline.Decline_m_F(self.key1,self.key2)
  elif self.model in ['m_x','f_x']:  
   # Masculine and feminine the same 
   decl = decline.Decline_m_x(self.key1,self.key2)
  elif self.model == 'm_f':
   decl = decline_f.Decline_m_f(self.key1,self.key2)
  elif self.model == 'f_f':
   decl = decline_f.Decline_f_f(self.key1,self.key2)
  elif self.model == 'n_f':
   decl = decline_f.Decline_n_f(self.key1,self.key2)

  elif self.model == 'm_in':
   decl = decline.Decline_m_in(self.key1,self.key2)
  elif self.model == 'n_in':
   decl = decline.Decline_n_in(self.key1,self.key2)
  elif self.model == 'f_in_I': # alias for f_I
   decl = decline.Decline_f_I(self.key1,self.key2)

  elif self.model == 'm_vat':
   decl = decline.Decline_m_vat(self.key1,self.key2)
  elif self.model == 'n_vat':
   decl = decline.Decline_n_vat(self.key1,self.key2)
  elif self.model == 'f_vat_I': # alias for f_I
   decl = decline.Decline_f_I(self.key1,self.key2)

  elif self.model == 'm_Iyas':
   decl = decline.Decline_m_Iyas(self.key1,self.key2)
  elif self.model == 'n_Iyas':
   decl = decline.Decline_n_Iyas(self.key1,self.key2)
  elif self.model == 'f_Iyas_I': # alias for f_I
   decl = decline.Decline_f_I(self.key1,self.key2)

  elif self.model == 'm_as':
   decl = decline.Decline_m_as(self.key1,self.key2)
  elif self.model == 'n_as':
   decl = decline.Decline_n_as(self.key1,self.key2)
  elif self.model == 'f_as': # same as m_as 
   decl = decline.Decline_f_as(self.key1,self.key2)

  elif self.model == 'm_vas':
   decl = decline.Decline_m_vas(self.key1,self.key2)
   self.base1 = decl.base1
   self.base2 = decl.base2
  elif self.model == 'n_vas':
   decl = decline.Decline_n_vas(self.key1,self.key2)
   self.base1 = decl.base1
   self.base2 = decl.base2
  elif self.model == 'f_vas_I': # alias for f_I
   decl = decline.Decline_f_I(self.key1,self.key2)

  elif self.model == 'm_pron':
   decl = decline_pco.Decline_m_pron(self.key1,self.key2)
  elif self.model == 'f_pron':
   decl = decline_pco.Decline_f_pron(self.key1,self.key2)
  elif self.model == 'n_pron':
   decl = decline_pco.Decline_n_pron(self.key1,self.key2)
  elif self.model == 'm_card':
   decl = decline_pco.Decline_m_card(self.key1,self.key2)
  elif self.model == 'f_card':
   decl = decline_pco.Decline_f_card(self.key1,self.key2)
  elif self.model == 'n_card':
   decl = decline_pco.Decline_n_card(self.key1,self.key2)
   """
  elif self.model == 'm_mat':
   decl = decline_2stem.Decline_m_matvat(self.key1,self.key2)
  elif self.model == 'n_mat':
   decl = decline_2stem.Decline_n_matvat(self.key1,self.key2)
  elif self.model == 'm_vat':
   decl = decline_2stem.Decline_m_matvat(self.key1,self.key2)
  elif self.model == 'n_vat':
   decl = decline_2stem.Decline_n_matvat(self.key1,self.key2)
   """
  elif self.model == 'm_an':
   decl = decline_3stem.Decline_m_an(self.key1,self.key2)
  elif self.model == 'n_an':
   decl = decline_3stem.Decline_n_an(self.key1,self.key2)
  elif self.model == 'f_an':
   decl = decline_3stem.Decline_f_an(self.key1,self.key2)

  # Do all in 1 class. Pass the gender to class constructor
  elif self.model == 'm_1stem':
   decl = decline_1stem.Decline_1stem('m',self.key1,self.key2,)
  elif self.model == 'n_1stem':
   decl = decline_1stem.Decline_1stem('n',self.key1,self.key2)
  elif self.model == 'f_1stem':
   decl = decline_1stem.Decline_1stem('f',self.key1,self.key2)
  else:
   print('DeclRec unimplemented model',self.model,self.key2)
   exit(1)
  self.sups = decl.getsups()
  if not decl.status:
   print('DeclRec error',self.model,self.key2)
   inflection = ['' for x in range(0,24)]
  else:
   inflection = decl.table
  self.inflection = self.list_to_string(inflection)
 # static method
 def list_to_string(self,a):
  b = []
  for x in a:
   if isinstance(x,list):
    y = '/'.join(x)
   else:
    y = x
   b.append(y)
  return ':'.join(b)

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 with codecs.open(filein,"r","utf-8") as f:
  nrec = 0
  with codecs.open(fileout,"w","utf-8") as fout:
   for line in f:
    if line.startswith(';'):
     continue # skip comment
    rec = DeclRec(line)
    out = '%s\t%s\t%s' %(rec.model,rec.key2,rec.inflection)
    fout.write(out+'\n')
    nrec = nrec + 1
    if nrec == 1000000:
     print('debug quit after',nrec,'cases')
     break
 print(nrec,"records from",filein,"processed and written to",fileout)


